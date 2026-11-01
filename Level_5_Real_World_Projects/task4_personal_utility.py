while True:
    print("\n===== PERSONAL UTILITY TOOL =====")
    print("1. Check Even or Odd")
    print("2. Calculate Square")
    print("3. Calculate Factorial")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

    elif choice == "2":
        num = int(input("Enter a number: "))
        print("Square:", num ** 2)

    elif choice == "3":
        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = 1

            for i in range(1, num + 1):
                factorial *= i

            print("Factorial:", factorial)

    elif choice == "4":
        print("Thank you for using the utility tool!")
        break

    else:
        print("Invalid choice!")