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

# Solution Two in O(n) time | O(n) space
# We create a dict
# Create a variable to store the difference between the num and targetSum
# When we subtract we store this value in the variable
# Then simply search to see if this number exists
# If this number exists we take our num and this
# variable and store them in the array/dict
# if not, we simply return the empty array as suggested.

def twoNumberSum2(array, targetSum):
  nums = {}
  for num in array:
    possibleNum = targetSum - num
    if possibleNum in nums:
      return [possibleNum, num]
    else: nums[num] = True
  return []