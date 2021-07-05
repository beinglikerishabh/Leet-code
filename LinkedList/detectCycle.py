""" Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""


def cycle(self):
    fastptr = self.head
    slowptr = self.head
    # ensure the list is not empty  somewhere ahead.
    while(fastptr and slowptr):
        fastptr = fastptr.next  # fast pointer takes first step
        if fastptr == slowptr:
            return True  # both pointer match means there is a loop
        if fastptr is None:
            return False  # there is no loop as List terminated.
        fastptr = fastptr.next  # second step of the fast pointer
        if fastptr == slowptr:
            return True  # both pointer match means there is a loop
        slowptr = slowptr.next  # first step of slow pointer
