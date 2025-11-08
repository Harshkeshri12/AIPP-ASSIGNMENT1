import hashlib
import json
import os

class LoginSystem:
    def __init__(self):
        self.users_file = 'users.json'
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump({}, f)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        with open(self.users_file, 'r') as f:
            users = json.load(f)
        
        if username in users:
            return False, "Username already exists"
        
        hashed_password = self.hash_password(password)
        users[username] = hashed_password
        
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
        
        return True, "Registration successful"

    def login(self, username, password):
        with open(self.users_file, 'r') as f:
            users = json.load(f)
        
        if username not in users:
            return False, "Invalid username"
        
        hashed_password = self.hash_password(password)
        if users[username] != hashed_password:
            return False, "Invalid password"
        
        return True, "Login successful"

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_system.register(username, password)
            print(message)
            
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_system.login(username, password)
            print(message)
            
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
