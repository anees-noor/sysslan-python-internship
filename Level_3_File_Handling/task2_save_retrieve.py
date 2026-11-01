import json

records = []

while True:
    print("\n1. Add Record")
    print("2. Display Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        record = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        records.append(record)

        with open("records.json", "w") as file:
            json.dump(records, file, indent=4)

        print("Record saved successfully!")

    elif choice == "2":
        try:
            with open("records.json", "r") as file:
                records = json.load(file)

            for record in records:
                print(record)

        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")