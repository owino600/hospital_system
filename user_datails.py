#!/usr/bin/python3
"""dictionary for store user credentials (username and password)"""
class usercredentials:
     # Function to validate user credentials
 def __init__(self, username, password):
     self.username = username
     self.password = pasword
     username = input("ENTER USERNAME: ")
     password = input("Enter Password")
     user = usercredentials(username, password)
     # Function to create a new account
     def create_account(username, password):
         if username not in user_credentials:
             user_credentials[username] = password
             print("Account created successfully.")
         else:
             print("Username already exists. Please choose a different username.")
             # Main program loop
             while True:
                 print("Welcome to the login system")
                 print("1. Log in")
                 print("2. Create an account")
                 choice = input("Enter your choice (1/2): ")
                 if choice == "1":
                     username = input("Enter your username: ")
                     password = input("Enter your password: ")
                     if login(username, password):
                         print("Login successful!")
                         break
                     else:
                         print("Login failed. Please try again.")
                         if choice == "2":
                             username = input("Enter a new username: ")
                             passwod = input("Enter a new password: ")
                             create_account(username, password)
                         else:
                             print("Invalid choice. Please select 1 or 2.")
