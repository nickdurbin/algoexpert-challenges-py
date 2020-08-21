# Solution One in O(n^2)
# Use two for loops to iterate over the array
# Store each value in a variable
# See if the first and second variables add up to target value
# If so, return them in a list
# If not, return an empty arrays

def twoNumberSum(array, targetSum):
  for i in range(len(array)-1):
    a = array[i]
    for j in range(i+1, len(array)):
      b = array[j]
      if a + b == targetSum:
        return [a, b]
  return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))