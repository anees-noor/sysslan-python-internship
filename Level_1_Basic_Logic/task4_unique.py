# Task 4: Check whether all numbers are unique

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 5]
]

# Creating an empty set
seen = set()

# Variable to track duplicates
unique = True

# Checking every element
for row in grid:
    for number in row:

        if number in seen:
            unique = False
            print("Duplicate element found:", number)
            break

        else:
            seen.add(number)

    if not unique:
        break

# Displaying the result
if unique:
    print("All numbers are unique.")
else:
    print("All numbers are not unique.")