filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print("\nFile Content:")

        for line in file:
            print(line, end="")

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("Permission denied.")