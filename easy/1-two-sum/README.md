This solution uses a dictionary to keep track of previously seen numbers and their indices. For each number in the list, it calculates the complement needed to reach the target sum and checks if that complement has been seen before. If so, it returns the indices of the two numbers that add up to the target sum. If not, it adds the number to the dictionary of seen numbers and moves on to the next number.


## Frequently Asked Questions

**Q: What is the time complexity of the brute-force approach to solving the Two Sum problem?**  
A: The brute-force approach involves checking every possible pair of numbers in the input list to see if they add up to the target sum. This takes O(n^2) time, where n is the length of the input list.

**Q: What is the time complexity of the optimal approach to solving the Two Sum problem?**  
A: The optimal approach involves using a hash table to keep track of previously seen numbers and their indices. This takes O(n) time, where n is the length of the input list.

**Q: Can the input list contain duplicates?**  
A: Yes, the input list can contain duplicates.

**Q: Can the input list contain negative numbers?**  
A: Yes, the input list can contain negative numbers.

**Q: What happens if there are multiple pairs of numbers that add up to the target sum?**  
A: The problem statement only requires returning any one valid pair of indices. If there are multiple pairs of numbers that add up to the target sum, the optimal approach will return the indices of the first valid pair it encounters.
