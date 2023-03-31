The problem asks us to find two numbers in the input list that add up to a target sum, and return their indices in the list. We can solve this problem by iterating through the input list and checking if the target minus the current number has been seen before.

To keep track of previously seen numbers and their indices, we can use a dictionary. For each number in the list, we check if the target minus the number has been seen before by looking it up in the dictionary. If it has, we return the current index and the index of the complement. If it hasn't, we add the current number and its index to the dictionary.

This approach has a time complexity of O(n), where n is the length of the input list. We only need to iterate through the list once, and each dictionary lookup takes constant time on average.



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
