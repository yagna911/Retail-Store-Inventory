# Customer business logic
import sqlite3

class CustomerManager:
    def __init__(self, db_path="Data/database.db"):
        self.db_path = db_path

    def get_all_customers(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, phone, address, created_at, updated_at FROM customers")
        customers = cursor.fetchall()
        conn.close()
        return customers

    def add_customer(self, name, email, phone, address):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?)", (name, email, phone, address))
        conn.commit()
        conn.close()

    def update_customer(self, customer_id, name, email, phone, address):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE customers SET name=?, email=?, phone=?, address=? WHERE id=?
        """, (name, email, phone, address, customer_id))
        conn.commit()
        conn.close()

    def delete_customer(self, customer_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id=?", (customer_id,))
        conn.commit()
        conn.close()
