from backend.server import SessionLocal, Customer, Restaurant, MenuItem, Order, Base, engine
from sqlalchemy import text
import datetime

def seed_data():
    print("🌱 Starting Intelligent Seed...")
    session = SessionLocal()
    
    try:
        # 1. Create a Customer if not exists
        cust = session.query(Customer).filter(Customer.email == "john@example.com").first()
        if not cust:
            cust = Customer(name="John Doe", email="john@example.com", phone_num="03001234567")
            session.add(cust)
            session.flush()
            print("👤 Customer created.")
        else:
            print("👤 Customer already exists.")

        # 2. Create Restaurants if not exists
        res_names = ["Lush Leaf", "Green Grill", "The Salad Bar"]
        for name in res_names:
            exists = session.query(Restaurant).filter(Restaurant.name == name).first()
            if not exists:
                res = Restaurant(name=name, location="Downtown", rating=4.5, affordability="$$")
                session.add(res)
                session.flush()
                # Add Menu Items
                items = [
                    ("Classic Caesar", "Fresh Romaine and croutons", 12.99, "Food Item"),
                    ("Green Smoothie", "Spinach and Apple", 6.50, "Beverage"),
                    ("Fruit Plate", "Seasonal fruits", 8.00, "Dessert")
                ]
                for n, d, p, c in items:
                    mi = MenuItem(restaurant_id=res.restaurant_id, name=n, description=d, price=p, category=c)
                    session.add(mi)
                print(f"🏠 Restaurant '{name}' created.")
        
        session.commit()
        print("✅ Seeding Complete!")
    except Exception as e:
        session.rollback()
        print(f"❌ Seed Failed: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()
