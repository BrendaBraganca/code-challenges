def triangPascal(qtdLinhas):
  mat = []
  acc = 2
  mat.append([1])
  while(acc <= qtdLinhas):
    vetLinha = []
    for i in range(0, acc):
      vetLinha.append(0)

    vetLinha[0] = 1
    vetLinha[-1] = 1
    i = 0
    j = acc -1
    while(j-i > 1):
      vetLinha[i+1] = mat[acc-2][i] + mat[acc-2][i+1]
      i+=1

    mat.append(vetLinha)
    acc+=1
  return mat