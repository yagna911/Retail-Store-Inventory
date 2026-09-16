# Simple PyQt5 GUI for Customer Management
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget, QMessageBox
)
from Customer import CustomerManager

class CustomerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = CustomerManager()
        self.setWindowTitle("Customer Management")
        self.setGeometry(100, 100, 500, 400)
        self.init_ui()
        self.load_customers()

    def init_ui(self):
        layout = QVBoxLayout()

        # List
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Form
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone")
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Address")
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.address_input)
        layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add")
        self.update_btn = QPushButton("Update")
        self.delete_btn = QPushButton("Delete")
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Connect
        self.add_btn.clicked.connect(self.add_customer)
        self.update_btn.clicked.connect(self.update_customer)
        self.delete_btn.clicked.connect(self.delete_customer)
        self.list_widget.itemClicked.connect(self.fill_form_from_list)

    def load_customers(self):
        self.list_widget.clear()
        self.customers = self.manager.get_all_customers()
        for c in self.customers:
            self.list_widget.addItem(f"{c[0]}: {c[1]} | {c[2]} | {c[3]} | {c[4]}")

    def fill_form_from_list(self, item):
        idx = self.list_widget.currentRow()
        c = self.customers[idx]
        self.name_input.setText(c[1])
        self.email_input.setText(c[2])
        self.phone_input.setText(c[3])
        self.address_input.setText(c[4])

    def add_customer(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Input Error", "Name is required.")
            return
        self.manager.add_customer(name, email, phone, address)
        self.load_customers()
        self.clear_form()

    def update_customer(self):
        idx = self.list_widget.currentRow()
        if idx < 0:
            QMessageBox.warning(self, "Select Customer", "Select a customer to update.")
            return
        cid = self.customers[idx][0]
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.text().strip()
        self.manager.update_customer(cid, name, email, phone, address)
        self.load_customers()
        self.clear_form()

    def delete_customer(self):
        idx = self.list_widget.currentRow()
        if idx < 0:
            QMessageBox.warning(self, "Select Customer", "Select a customer to delete.")
            return
        cid = self.customers[idx][0]
        self.manager.delete_customer(cid)
        self.load_customers()
        self.clear_form()

    def clear_form(self):
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.address_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustomerWindow()
    win.show()
    sys.exit(app.exec_())
