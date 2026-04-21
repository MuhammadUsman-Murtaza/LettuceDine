import streamlit as st

class AppState:
    @staticmethod
    def initialize():
        if "role" not in st.session_state:
            st.session_state.role = "Customer" # Default
        if "current_restaurant" not in st.session_state:
            st.session_state.current_restaurant = None
        if "cart" not in st.session_state:
            st.session_state.cart = {}
        if "customer_id" not in st.session_state:
            st.session_state.customer_id = 1 
        if "selected_address" not in st.session_state:
            st.session_state.selected_address = None
        if "page" not in st.session_state:
            st.session_state.page = "Explore"

    @property
    def role(self):
        return st.session_state.role
    
    @role.setter
    def role(self, val):
        st.session_state.role = val
        # Reset page when switching roles
        if val == "Customer": st.session_state.page = "Explore"
        elif val == "Vendor": st.session_state.page = "Dashboard"
        elif val == "Admin": st.session_state.page = "Control Panel"

    @property
    def current_restaurant(self):
        return st.session_state.current_restaurant
    
    @current_restaurant.setter
    def current_restaurant(self, val):
        st.session_state.current_restaurant = val

    @property
    def cart(self):
        return st.session_state.cart

    @property
    def customer_id(self):
        return st.session_state.customer_id

    @property
    def selected_address(self):
        return st.session_state.selected_address

    @selected_address.setter
    def selected_address(self, val):
        st.session_state.selected_address = val

    def add_to_cart(self, item):
        cart = st.session_state.cart
        if item.item_id in cart:
            cart[item.item_id]['quantity'] += 1
        else:
            cart[item.item_id] = {'item': item, 'quantity': 1}
        st.session_state.cart = cart

    def get_cart_total(self):
        return sum(details['item'].price * details['quantity'] for details in st.session_state.cart.values())

    def clear_cart(self):
        st.session_state.cart = {}

state = AppState()
