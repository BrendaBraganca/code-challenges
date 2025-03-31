class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:  
            return head
        aux1 = head
        aux2 = head.next
        temp = head.next
        while(aux2 and aux2.next):
            aux1.next = aux2.next
            aux1 = aux1.next
            aux2.next = aux1.next
            aux2 = aux2.next
        aux1.next = temp
        return head