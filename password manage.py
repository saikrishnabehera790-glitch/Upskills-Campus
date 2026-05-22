import random
import string

passwords = {}

# Function to generate strong password
def generate_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(length))

while True:
    print("\n---- PASSWORD MANAGER ----")
    print("1. Store Password")
    print("2. Generate Password")
    print("3. Retrieve Password")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")
        passwords[account] = password
        print("Password saved successfully!")

    elif choice == "2":
        pwd = generate_password()
        print("Generated Password:", pwd)

    elif choice == "3":
        account = input("Enter account name: ")
        if account in passwords:
            print("Password:", passwords[account])
        else:
            print("Account not found!")

    elif choice == "4":
        print("Exiting Password Manager...")
        break

    else:
        print("Invalid choice!")