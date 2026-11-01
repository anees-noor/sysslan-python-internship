# Task 1: Display a 3x3 Number Grid

# Creating a nested list
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Displaying the grid
for row in grid:
    for number in row:
        print(number, end=" ")

    print()