-- ENUM Types
CREATE TYPE affordability_level AS ENUM ('$', '$$', '$$$');
CREATE TYPE order_status AS ENUM ('Pending', 'Preparing', 'On the Way', 'Delivered', 'Cancelled');
CREATE TYPE payment_method AS ENUM ('Cash', 'Card');
CREATE TYPE payment_status AS ENUM ('Pending', 'Completed', 'Failed');
CREATE TYPE menu_category AS ENUM ('Starter', 'Food Item', 'Beverage', 'Dessert');

-- 1. Customers Table
CREATE TABLE Customers (
    customer_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_num VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- 2. Addresses Table
CREATE TABLE Addresses (
    address_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id INTEGER REFERENCES Customers(customer_id) ON DELETE CASCADE,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    label VARCHAR(50) DEFAULT 'Home' -- e.g., 'Home', 'Work'
);

-- 3. Restaurants Table
CREATE TABLE Restaurants (
    restaurant_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    rating DECIMAL(2, 1) CHECK (rating >= 1 AND rating <= 5),
    affordability affordability_level
);

-- 4. Menu Items Table
CREATE TABLE Menu_Items (
    item_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    restaurant_id INTEGER REFERENCES Restaurants(restaurant_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category menu_category NOT NULL
);

-- 5. Coupons Table
CREATE TABLE Coupons (
    coupon_code VARCHAR(50) PRIMARY KEY,
    discount_amount DECIMAL(10, 2) NOT NULL,
    expiry_date DATE NOT NULL,
    min_order_value DECIMAL(10, 2) DEFAULT 0
);

-- 6. Orders Table
CREATE TABLE Orders (
    order_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id INTEGER REFERENCES Customers(customer_id),
    restaurant_id INTEGER REFERENCES Restaurants(restaurant_id),
    address_id INTEGER REFERENCES Addresses(address_id),
    coupon_code VARCHAR(50) REFERENCES Coupons(coupon_code),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    delivery_time TIMESTAMP,
    status order_status DEFAULT 'Pending',
    special_instructions TEXT
);

-- 7. Order Items Table (Junction for M:N between Orders and Menu Items)
CREATE TABLE Order_Items (
    order_id INTEGER REFERENCES Orders(order_id) ON DELETE CASCADE,
    item_id INTEGER REFERENCES Menu_Items(item_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price_at_purchase DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, item_id)
);

-- 8. Payments Table
CREATE TABLE Payments (
    payment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id INTEGER UNIQUE REFERENCES Orders(order_id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    method payment_method NOT NULL,
    status payment_status DEFAULT 'Pending'
);

-- 9. Reviews Table
CREATE TABLE Reviews (
    review_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id INTEGER REFERENCES Customers(customer_id),
    restaurant_id INTEGER REFERENCES Restaurants(restaurant_id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. Delivery Drivers Table
CREATE TABLE Delivery_Drivers (
    driver_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(20) NOT NULL,
    vehicle_type VARCHAR(50),
    rating DECIMAL(2, 1) DEFAULT 5.0
);

-- 11. Deliveries (Tracks which driver is handling which order)
CREATE TABLE Deliveries (
    order_id INTEGER PRIMARY KEY REFERENCES Orders(order_id),
    driver_id INTEGER REFERENCES Delivery_Drivers(driver_id),
    pickup_time TIMESTAMP,
    delivery_time TIMESTAMP
);

