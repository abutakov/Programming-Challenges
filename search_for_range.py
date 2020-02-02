# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
#   Example:
# Given [5, 7, 7, 8, 8, 10]
# and target value 8,
# return [3, 4].
def search_for_range(array, target):
  start_index = -1
  end_index = 1

  for i in range(0, len(array)):
    if array[i] == target:
      start_index = i
      while array[i] == target:
        end_index = i
        i += 1

    if start_index != -1:
      break

  return [start_index, end_index]

      

target = 8
arr = [5,7,7,8,8,10]
print(search_for_range(arr, target))
