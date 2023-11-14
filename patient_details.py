mport tkinter as tk
import mysql.connector

# Function to save patient details to the database
def save_patient_details():
    patient_name = patient_name_entry.get()
    age = age_entry.get()
    medical_record_number = medical_record_entry.get()
    # Save the details to the database
    cursor.execute("INSERT INTO patients (name, age, medical_record_number) VALUES (?, ?, ?)",
            (patient_name, age, medical_record_number))
    connection.commit()

    # You can also clear the input fields if needed
    patient_name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    medical_record_entry.delete(0, tk.END)
    # Proceed to the next step
    next_step()

    # Function to implement the next step
    def next_step():
        next_button.config(state=tk.NORMAL)  # Enable the "Next" button

        # Function to proceed to the next step
        def proceed_to_next_step():
            next_button.config(state=tk.DISABLED)  # Disable the "Next" button again
            # You can define the actions for the next step here
            # Function to access patient details from the database
            def access_patient_details():
                access_window = tk.Toplevel(root)
                access_window.title("Access Patient Details")

                # Create and add content to the access window
                cursor.execute("SELECT * FROM patients")
                patient_details = cursor.fetchall()

                for idx, patient in enumerate(patient_details):
                    details_label = tk.Label(access_window, text=f"Patient {idx+1} - Name: {patient[0]}, Age: {patient[1]}, Medical Record Number: {patient[2]}")
                    details_label.pack()

                    # Create a database and a patients table
                    connection = mysql.connector.connect(
                            host="your_mysql_host",
                            user="your_mysql_username",
                            password="your_mysql_password",
                            database="your_database_name"
                            )

                    cursor = connection.cursor()

                    # Create the main window
                    root = tk.Tk()
                    root.title("Patient Details Input")

                    # Create and place input fields and labels
                    tk.Label(root, text="Patient Name:").pack()
                    patient_name_entry = tk.Entry(root)
                    patient_name_entry.pack()

                    tk.Label(root, text="Age:").pack()
                    age_entry = tk.Entry(root)
                    age_entry.pack()

                    tk.Label(root, text="Medical Record Number (if available):").pack()
                    medical_record_entry = tk.Entry(root)
                    medical_record_entry.pack()

                    # Create a button to save patient details
                    save_button = tk.Button(root, text="Save Patient Details", command=save_patient_details)
                    save_button.pack()

                    next_button = tk.Button(root, text="Next", state=tk.DISABLED, command=proceed_to_next_step)
                    next_button.pack()

                    access_button = tk.Button(root, text="Access Patient Details", command=access_patient_details)
                    access_button.pack()

                    # Start the GUI main loop
                    root.mainloop()
