# /* 
#   Given an array of strings
#   return the number of times each string occurs (a frequency / hash table)
# */
{'a': 3}
arr1 = ["a", "a", "a"]
expected1 = {
  'a': 3,
}

arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"]
expected2 = {
  'a': 2,
  'b': 1,
  'c': 3,
  'B': 1,
  'd': 1,
}

arr3 = []
expected3 = {}

# /**
#  * Builds a frequency table based on the given array.
#  * - Time: O(?).
#  * - Space: O(?).
#  * @param {Array<string>} arr
#  * @returns {Object<string, number>} A frequency table where the keys are items
#  *    from the given arr and the values are the amnt of times that item occurs.
#  */
# def makeFrequencyTable(arr):
#   freq_table = {}
#   for i in range(len(arr)):
#     if arr[i] in freq_table:
#       freq_table[arr[i]] += 1
#     else:
#       freq_table[arr[i]] = 1
#   return freq_table

def makeFrequencyTable(arr):
  freq_table = {}
  count = 0
  for i in range(len(arr)):
    if arr[i] not in freq_table:
      freq_table[arr[i]] = 1
    else:
      freq_table[arr[i]] += 1
  return freq_table

print(makeFrequencyTable(arr1))
print(makeFrequencyTable(arr2))