numbers = []

try:
    with open("numbers.txt", "r") as file:
        for line in file:
            number = float(line.strip())
            numbers.append(number)

    if len(numbers) > 0:
        total = sum(numbers)
        average = total / len(numbers)
        maximum = max(numbers)

        print("Numbers:", numbers)
        print("Total:", total)
        print("Average:", average)
        print("Maximum:", maximum)

    else:
        print("The file is empty.")

except FileNotFoundError:
    print("File not found.")

except ValueError:
    print("Invalid data in file.")
