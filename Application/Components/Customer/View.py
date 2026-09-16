# Customer UI logic (placeholder)
from .Customer import CustomerManager

class CustomerView:
    def __init__(self):
        self.manager = CustomerManager()

    def show_all_customers(self):
        customers = self.manager.get_all_customers()
        for c in customers:
            print(f"ID: {c[0]}, Name: {c[1]}, Email: {c[2]}, Phone: {c[3]}, Address: {c[4]}")

    def add_customer(self, name, email, phone, address):
        self.manager.add_customer(name, email, phone, address)
        print("Customer added successfully.")

    def update_customer(self, customer_id, name, email, phone, address):
        self.manager.update_customer(customer_id, name, email, phone, address)
        print("Customer updated successfully.")

    def delete_customer(self, customer_id):
        self.manager.delete_customer(customer_id)
        print("Customer deleted successfully.")
