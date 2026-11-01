# Task 3: Calculate the sum of each row

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_number = 1

for row in grid:

    total = 0

    for number in row:
        total = total + number

    print("Row", row_number, "sum =", total)

    row_number = row_number + 1