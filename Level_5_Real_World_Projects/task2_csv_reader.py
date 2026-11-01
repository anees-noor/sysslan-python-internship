import csv

filename = input("Enter CSV file name: ")

try:
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        print("\nCSV File Contents:")

        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found.")