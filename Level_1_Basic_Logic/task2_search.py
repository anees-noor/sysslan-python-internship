# Task 2: Search for a number in a 3x3 grid

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accepting input
num = int(input("Enter a number to search: "))

found = False

# Searching the grid
for row in grid:
    for number in row:

        if number == num:
            found = True
            break

    if found:
        break

# Displaying the result
if found:
    print(num, "exists in the grid.")
else:
    print(num, "does not exist in the grid.")