class Solution(object):
    def reverseList(self, head):
        prev = None
        aux = head
        while(aux):
            prox = aux.next
            aux.next = prev
            prev = aux
            aux = prox
        return prev