from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime

# PostgreSQL connection string via pg8000
DATABASE_URL = "postgresql+pg8000://admin:admin1234@localhost:5432/lettucedine-db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Models ---

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    phone_num = Column(String(20), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

class Address(Base):
    __tablename__ = "addresses"
    address_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    street = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)
    label = Column(String(50), default="Home")

class Restaurant(Base):
    __tablename__ = "restaurants"
    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    rating = Column(Numeric(2, 1))
    affordability = Column(String(50)) # '$$'

class MenuItem(Base):
    __tablename__ = "menu_items"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(50), nullable=False)

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    address_id = Column(Integer, ForeignKey("addresses.address_id"))
    order_date = Column(TIMESTAMP, default=datetime.datetime.now)
    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), default="Pending")

class Review(Base):
    __tablename__ = "reviews"
    review_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    rating = Column(Integer)
    comment = Column(Text)
    review_date = Column(TIMESTAMP, default=datetime.datetime.now)

class OrderItem(Base):
    __tablename__ = "order_items"
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Numeric(10, 2), nullable=False)

class Payment(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), unique=True, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    method = Column(String(50), nullable=False)
    status = Column(String(50), default="Pending")

# --- Service Layer ---

def get_all_restaurants():
    with SessionLocal() as db:
        return db.query(Restaurant).all()

def get_menu_for_restaurant(restaurant_id: int):
    with SessionLocal() as db:
        return db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()

def get_customer_profile(customer_id: int):
    with SessionLocal() as db:
        return db.query(Customer).filter(Customer.customer_id == customer_id).first()

def get_customer_addresses(customer_id: int):
    with SessionLocal() as db:
        return db.query(Address).filter(Address.customer_id == customer_id).all()

def add_address(customer_id: int, street: str, city: str, zip_code: str, label: str):
    with SessionLocal() as db:
        addr = Address(customer_id=customer_id, street=street, city=city, zip_code=zip_code, label=label)
        db.add(addr)
        db.commit()
        return addr

def place_order(customer_id: int, restaurant_id: int, address_id: int, cart_items: dict, total_amount: float, payment_method: str):
    with SessionLocal() as db:
        # Create Order
        new_order = Order(
            customer_id=customer_id,
            restaurant_id=restaurant_id,
            address_id=address_id,
            total_amount=total_amount,
            status="Pending",
            order_date=datetime.datetime.now()
        )
        db.add(new_order)
        db.flush() # get order_id
        
        # Add Order Items
        for item_data in cart_items.values():
            it = item_data['item']
            qty = item_data['quantity']
            order_item = OrderItem(
                order_id=new_order.order_id,
                item_id=it.item_id,
                quantity=qty,
                price_at_purchase=it.price
            )
            db.add(order_item)
        
        # Add Payment
        payment = Payment(
            order_id=new_order.order_id,
            amount=total_amount,
            method=payment_method,
            status="Pending"
        )
        db.add(payment)
        
        db.commit()
        return new_order.order_id

def get_customer_orders(customer_id: int):
    with SessionLocal() as db:
        return db.query(Order).filter(Order.customer_id == customer_id).order_by(Order.order_date.desc()).all()

def submit_review(customer_id: int, restaurant_id: int, rating: int, comment: str):
    with SessionLocal() as db:
        review = Review(
            customer_id=customer_id,
            restaurant_id=restaurant_id,
            rating=rating,
            comment=comment,
            review_date=datetime.datetime.now()
        )
        db.add(review)
        db.commit()
        return review
