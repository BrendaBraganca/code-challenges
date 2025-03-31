class Solution(object):
    def decodeString(self, s):
        pilha = []
        for c in s:
            if c != "]":
                pilha.append(c)
            else:
                atual = ""
                while pilha and pilha[-1] != "[":
                    atual = pilha.pop() + atual
                pilha.pop()
                qtd = ""
                while pilha and pilha[-1].isdigit():
                    qtd = pilha.pop() + qtd
                pilha.append(atual * int(qtd))
        return "".join(pilha)