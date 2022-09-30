# Print a grid
# grid = [[0,0,0],
        # [0,0,0]]

num_rows = 2
num_columns = 3
grid = []

for _ in range(num_rows):
    row = []
    for _ in range(num_columns):
        row.append(0)
    grid.append(row)

print(grid)

# using list comprhemsion
grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

# Max
lst = [1,2,-5, 4]
max(1,2,3)

max(lst, key=lambda x: x* x)