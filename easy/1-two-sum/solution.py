class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store previously seen numbers and their indices
    seen = {}

    # Iterate through the input list
    for i, num in enumerate(nums):
      # Check if the target minus the current number has been seen before
      complement = target - num
      if complement in seen:
        # If the complement has been seen, return the current index and the complement's index
        return [seen[complement], i]
      else:
        # If the complement has not been seen, add the current number and its index to the dictionary
        seen[num] = i
