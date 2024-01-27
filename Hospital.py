class Hospital:
    def __init__(self, doctor, nurse, patient):
        self.Doctor=doctor
        self.Nurse=nurse
        self.Patient=patient
        category = input("Enter your position (Doctor/Nurse/Patient): ")
        if category == "Doctor":
            print("welcome doctor!")
        elif category == "Nurse":
            print("welcome nurse!")
            #continue
        else:
            print("welcome patient!")
            #continue
        
class User_credentials:
    user_credentials = {}
    
    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.password=password
        
        if User_credentials.user_credentials[email, username] == password:
            print('account exist, logged in successfully!')
        else:
            User_credentials.user_credentials[email, username] = password
            while true:
                print("welcome to your system")
                print("1.")
                print("2.")
                choice = input("Enter choice")
                break
        if choice == "1":
            username = input("ENTER USERNAME: ")
            email = input("ENTER EMAIL ADDRESS: ")
            password = input("ENTER PASSWORD: ")
        if self.login(username, email, password):
            print("Login successful!")
        else:
            print("acount unavailable, please sign up!")
            User_credentials.user_credentials[email, username] = password

class Doctor:
    def __init__(self, prescribe, admit, discharge):
        self.prescribe = prescribe
        self.admit = admit
        self.release = release
        
        patient = input("prescribe, admit, discharge")
        if patient == "prescribe":
            print('Please prescribe the required drugs')
            prescribe = input("")
        elif patient == "admit":
            print('Enter reason to admit')
            admit = input("")
        elif patient == "discharge":
            print('Patient Discharged please send to the accounts')
