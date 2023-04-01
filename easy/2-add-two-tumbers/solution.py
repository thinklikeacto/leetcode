class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize a dummy head node to hold the sum
    dummy = ListNode(0)
    # Initialize current node to the dummy head
    current = dummy
    # Initialize carry to 0
    carry = 0

    # Iterate over the two linked lists until at least one is empty
    while l1 or l2:
      # Get the value of the current node in each linked list, or 0 if empty
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      # Calculate the sum of the two values and the carry from the previous digit
      sum = val1 + val2 + carry
      # Update the carry for the next iteration
      carry = sum // 10
      # Create a new node with the least significant digit of the sum
      current.next = ListNode(sum % 10)
      # Move to the next node in each linked list, or None if at the end
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
      # Move to the next node in the sum linked list
      current = current.next

    # If there's still a carry left over after adding all the digits, create a new node for it
    if carry > 0:
      current.next = ListNode(carry)

    # Return the next node after the dummy head, which holds the sum
    return dummy.next
