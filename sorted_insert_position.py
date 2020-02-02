def find_index(sorted_list, target):
  print(sorted_list, " ", target)

  if target <= sorted_list[0]:
    return 0

  for i in range(0, len(sorted_list) - 1):
    if target == sorted_list[i]:
      return i
    elif target >= sorted_list[i] and target <= sorted_list[i+1]:
      return i+1
    else:
      pass

  return len(sorted_list)
  

arr = [1,3,5,6]
target = 0
print(find_index(arr, target))