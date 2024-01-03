class Hospital:
    def __init__(self, doctor, nurse, patient):
        self.doctors=doctor
        self.nurses=nurse
        self.patients=patient
        doctor = input("")
        nurse = input("")
        patient = input("")
        category = Hospital(doctor, nurse, patient)
        if input in Hospital == doctor:
            print("welcome doctor!")
            continue
        elif input in Hospital == nurse:
            print("welcome nurse!")
            continue
        else:
            print("welcome patient!")
            continue
        class User_credentials:
            def __init__(self, username, email, password):
                self.username=username
                self.email=email
                self.password=password
                username = input("ENTER USERNAME: ")
                email = input("ENTER EMAIL ADDRESS: ")
                password = input("ENTER PASSWORD: ")
                user = user_credentials(username, email, password)
                if email in user_credentials == password:
                    print('account exist, logged in successfully!')
                else:
                    user_credentials[email, username] = password
                    while true:
                        print("welcome to your system")
                        print("1.")
                        print("2.")
                        choice = input("Enter choice")
                        if choice == "1":
                            username = input("ENTER USERNAME: ")
                            email = input("ENTER EMAIL ADDRESS: ")
                            password = input("ENTER PASSWORD: ")
                            if login(username, email, password):
                                print("Login successful!")
                            break
                        else:
                            print("acount unavailable, please sign up!")
                            user_credentials[email, username] = password

                            class Doctor:
                                def __init__(self, prescribe, admit, release):
                                    self.prescribe = prescribe
                                    self.admit = admit
                                    self.release = release
                                    patient = Doctor(prescribe, admit, release)
                                    if patient == prescribed:
                                        print('Please prescribe the required drugs')
                                        prescribe = input("")
                                    elif patient == admit:
                                        print('Enter reson to admit')
                                        admit = input("")



