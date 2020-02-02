  # Counts number of zeros in a given array
def count_zeros(arr):
	counter = 0
	
	for i in range(0,len(arr)):
		# counting number of 0's 
		if arr[i] == False: # 0 is the only numeric value that is zero for Python
			counter += 1
	return counter
	
  # Shifts array by one element to the right from a given index
def shift_right(arr, start_index, end_index):

  print("Before: ", arr)

  if end_index >= len(arr):
    print("Error: index out of bound.\nExiting...")
    return -1

  i = end_index
  while i >= start_index:
    arr[i+1] = arr[i]
    arr[i] = 0
    i -= 1

  print("After: ", arr)
  pass

# Requirement: to modify num1 (given array) in-place
def merge_sorted_lists(nums1, nums2):
  len1 = len(nums1)
  len2 = len(nums2)
  len2_nonzero = len1 - count_zeros(nums1)
  
  print("Printing lengths...")
  print("len1 = ", len1, ", len2 = ", len2, "len_nonzero = ", len2_nonzero)

  num1_ptr = 0
  num2_ptr = 0
  for i in range(0,len1):
    if nums1[num1_ptr] <= nums2[num2_ptr]:
      shift_right(nums1, num1_ptr)
      num1_ptr += 1
      num2_ptr += 1


  return
  
arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]

print("Number of zeros in arr1 = ",count_zeros(arr1))
shift_right(arr1, 1,3)

#merge_sorted_lists(arr1, arr2)

