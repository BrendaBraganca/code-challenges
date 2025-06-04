class Solution(object):
    def intToRoman(self, num):
        hash_tab = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = []
        for vInt, vR in hash_tab:
            if(num == 0): 
                break
            qtd = num//vInt
            res.append(qtd * vR)
            num = num - (qtd * vInt)
        return ''.join(res)