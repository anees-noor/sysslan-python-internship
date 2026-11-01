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
        print("Record added successfully!")

    elif choice == "2":
        if len(records) == 0:
            print("No records found.")
        else:
            for record in records:
                print(record)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")