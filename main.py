class StudentProfile:
    def __init__(self, student_id, name, pin):
        self.student_id = student_id
        self.name = name
        self.pin = pin
        self.subjects = []

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully.")

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"Added subject: {subject}")
        else:
            print("Subject already exists.")

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"Removed subject: {subject}")
        else:
            print("Subject not found!")

    def view_subjects(self):
        if self.subjects:
            print("Subjects enrolled:")
            for subject in self.subjects:
                print(f"- {subject}")
        else:
            print(" OOPPSS No subjects enrolled yet.")


class StudentPortal:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, student_id, name, pin):
        if student_id not in self.profiles:
            new_profile = StudentProfile(student_id, name, pin)
            self.profiles[student_id] = new_profile
            print("Profile created successfully.")
        else:
            print("Student ID already exists.")

    def delete_profile(self, student_id):
        if student_id in self.profiles:
            del self.profiles[student_id]
            print("Profile deleted successfully.")
        else:
            print("Profile not found.")

    def profile_exists(self, student_id):
        return student_id in self.profiles

    def login(self, student_id, pin):
        if self.profile_exists(student_id):
            profile = self.profiles[student_id]
            if profile.pin == pin:
                return profile
        return None


def main():
    portal = StudentPortal()

    while True:
        print("\n1. Create Profile")
        print("2. Delete Profile")
        print("3. Login")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            pin = input("Enter PIN: ")
            portal.create_profile(student_id, name, pin)

        elif choice == 2:
            student_id = input("Enter student ID to delete: ")
            portal.delete_profile(student_id)

        elif choice == 3:
            student_id = input("Enter student ID: ")
            pin = input("Enter PIN: ")
            profile = portal.login(student_id, pin)
            if profile:
                while True:
                    print("\n1. View Subjects")
                    print("2. Add Subject")
                    print("3. Remove Subject")
                    print("4. Change PIN")
                    print("5. Logout")
                    sub_choice = int(input("Enter your choice: "))

                    if sub_choice == 1:
                        profile.view_subjects()

                    elif sub_choice == 2:
                        subject = input("Enter subject name: ")
                        profile.add_subject(subject)

                    elif sub_choice == 3:
                        subject = input("Enter subject name to remove: ")
                        profile.remove_subject(subject)

                    elif sub_choice == 4:
                        new_pin = input("Enter new PIN: ")
                        profile.change_pin(new_pin)

                    elif sub_choice == 5:
                        break

                    else:
                        print("Invalid choice!")

            else:
                print("Invalid student ID or PIN!")

        elif choice == 4:
            print("Thank you for using the Student Profile System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
