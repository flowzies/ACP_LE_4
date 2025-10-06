import os


doc_path = os.path.expanduser("~/Documents")


if not os.path.exists(doc_path):
    os.makedirs(doc_path)



def register_student():
    print("\n=== REGISTER STUDENT ===")
    student_no = input("Student No.: ")
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    middle_initial = input("Middle Initial: ")
    program = input("Program: ")
    age = input("Age: ")
    gender = input("Gender: ")
    birthday = input("Birthday: ")
    contact_no = input("Contact No.: ")


    data = [
        f"Student No.: {student_no}",
        f"Full Name: {last_name}, {first_name} {middle_initial}.",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birthday}",
        f"Contact No.: {contact_no}"
    ]


    file_name = f"{student_no}.txt"
    file_path = os.path.join(doc_path, file_name)
    try:
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        print(f"\nStudent record for {student_no} saved successfully!")
    except Exception as e:
        print(f"Error saving record: {e}")


def open_student_record():
    print("\n=== OPEN STUDENT RECORD ===")
    student_no = input("Enter Student No.: ")
    file_name = f"{student_no}.txt"
    file_path = os.path.join(doc_path, file_name)


    try:
        with open(file_path, "r") as f:
            print("\n--- STUDENT RECORD ---")
            for line in f:
                print(line.strip())
            print("-----------------------\n")
    except FileNotFoundError:
        print("Student record not found.")
    except Exception as e:
        print(f"Error reading file: {e}")



def main():
    while True:
        print("\n===== STUDENT RECORD MENU =====")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            open_student_record()
        elif choice == "3":
            print("\nGoodbye! Thank you for using the system.\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
