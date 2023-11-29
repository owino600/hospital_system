#!/usr/bin/python3
class PatientSystem:
    def __init__(self, db_file='hospital_system.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        def add_patient(self, name, dob, contact):
            self.cursor.execute('INSERT INTO patients (name, dob, contact) VALUES (?, ?, ?)', (name, dob, contact))
            self.conn.commit()
            print("Patient added successfully.")

            def schedule_appointment(self, patient_id, doctor, date):
                self.cursor.execute('INSERT INTO appointments (patient_id, doctor, date) VALUES (?, ?, ?)',
                        (patient_id, doctor, date))
                self.conn.commit()
                print("Appointment scheduled successfully.")

                def add_to_queue(self, patient_id, position):
                    self.cursor.execute('INSERT INTO queue (patient_id, position) VALUES (?, ?)', (patient_id, position))
                    self.conn.commit()
                    print("Patient added to the queue successfully.")

                    def prescribe_medication(self, patient_id, doctor, medication, instructions):
                        self.cursor.execute('INSERT INTO prescriptions (patient_id, doctor, medication, instructions) '
                                'VALUES (?, ?, ?, ?)', (patient_id, doctor, medication, instructions))
                        self.conn.commit()
                        print("Prescription added successfully.")
                        def close_connection(self):
                            self.conn.close()

