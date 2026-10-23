
def trier(L):
    n = 0

    for nombre in L:
        n = n + 1

    for tour in range(n):
        i = 0

        while i < n - 1:
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp

            i = i + 1

    return L


print(trier([8, 3, 5, 1]))