# Definition for singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        tam = 0
        temp = head
        while(temp):
            tam+=1
            temp = temp.next
        meio = tam//2
        i = 0
        temp = head
        while(i < meio -1):
            temp = temp.next
            i+=1
        aux = temp.next
        temp.next = aux.next
        return head