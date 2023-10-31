# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversed_numbers(self, node: Optional[ListNode]):
        numbers = str()
        while node:
            numbers += str(node.val)
            node = node.next
        return int(numbers[::-1])
    
    
    def create_linked_list(self, elements):
        node: ListNode
        for index in range(len(elements)):
            if index == 0:
                node = ListNode(int(elements[index]), None)
            else:
                node = ListNode(int(elements[index]), node)
        return node
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_numbers = self.reversed_numbers(l1) + self.reversed_numbers(l2)
        return self.create_linked_list(str(sum_numbers))