import json
import os

# File to save the passwords
PASSWORD_FILE = 'passwords.json'

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)

def add_password(passwords, account, password):
    passwords[account] = password
    save_passwords(passwords)
    print(f"Password for '{account}' added.")

def get_password(passwords, account):
    return passwords.get(account, "Account not found.")

def update_password(passwords, account, password):
    if account in passwords:
        passwords[account] = password
        save_passwords(passwords)
        print(f"Password for '{account}' updated.")
    else:
        print("Account not found.")

def delete_password(passwords, account):
    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print(f"Password for '{account}' deleted.")
    else:
        print("Account not found.")

def main():
    passwords = load_passwords()

    while True:
        print("\nPassword Locker Menu")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            add_password(passwords, account, password)
        elif choice == '2':
            account = input("Enter the account name: ")
            print(f"Password for '{account}': {get_password(passwords, account)}")
        elif choice == '3':
            account = input("Enter the account name: ")
            password = input("Enter the new password: ")
            update_password(passwords, account, password)
        elif choice == '4':
            account = input("Enter the account name: ")
            delete_password(passwords, account)
        elif choice == '5':
            print("Exiting Password Locker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

