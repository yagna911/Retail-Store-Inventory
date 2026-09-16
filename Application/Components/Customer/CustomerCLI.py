# Simple CLI for Customer Management
from Customer import CustomerManager

def main():
    manager = CustomerManager()
    while True:
        print("\nCustomer Management")
        print("1. List all customers")
        print("2. Add customer")
        print("3. Update customer")
        print("4. Delete customer")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            customers = manager.get_all_customers()
            for c in customers:
                print(f"ID: {c[0]}, Name: {c[1]}, Email: {c[2]}, Phone: {c[3]}, Address: {c[4]}")
        elif choice == '2':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            manager.add_customer(name, email, phone, address)
            print("Customer added.")
        elif choice == '3':
            cid = int(input("Customer ID to update: "))
            name = input("New Name: ")
            email = input("New Email: ")
            phone = input("New Phone: ")
            address = input("New Address: ")
            manager.update_customer(cid, name, email, phone, address)
            print("Customer updated.")
        elif choice == '4':
            cid = int(input("Customer ID to delete: "))
            manager.delete_customer(cid)
            print("Customer deleted.")
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
