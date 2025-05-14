class Solution(object):
    def sortColors(self, nums):
        def particiona(lista, esq, di):
            pivot = lista[di]
            i = esq -1
            for j in range(esq, di):
                if lista[j] <= pivot:
                    i+=1
                    lista[i], lista[j] = lista[j], lista[i]
            lista[i+1], lista[di] = lista[di], lista[i+1]
            return i+1
        def quicksort(lista, esq, di):
            if(esq < di):
                p = particiona(lista,esq,di)
                quicksort(lista, esq, p-1)
                quicksort(lista, p+1, di)

        quicksort(nums, 0, len(nums)-1)
        return nums
        