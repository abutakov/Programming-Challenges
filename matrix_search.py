#   Instructions from your teacher:
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
#   Example:
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]

# Given target = 3, return 1 ( 1 corresponds to true )

# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
def matrix_search(matrix, target):
  num_rows = len(matrix)
  num_columns = len(matrix[0])
  print (num_rows)   # prints number of rows
  print(num_columns) # prints number of columns

  target_row = -1

  # finding in which row our target could be, by comparing it to the last element in the row
  for x in range(0, num_rows):
    if target <= matrix[x][num_columns-1]:
      target_row = x
      break
  
  if target_row == -1:
    return 0
  else:
    for x in range(0, num_columns):
      if target == matrix[target_row][x]:
        return 1

  return 0


matrix = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
target = 30
print(matrix_search(matrix, target))