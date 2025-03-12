class Solution(object):
    def compress(self, chars):
        indLer = 0
        indEsc = 0

        while(indLer < len(chars)):
            letra = chars[indLer]
            qtdRep = 0

            while indLer < len(chars) and chars[indLer] == letra:
                indLer+=1
                qtdRep+=1
            
            chars[indEsc] = letra
            indEsc+=1

            if qtdRep>1:
                for algarismo in str(qtdRep):
                    chars[indEsc] = algarismo
                    indEsc+=1

        return indEsc