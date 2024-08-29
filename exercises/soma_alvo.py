def soma_alvo(nums, alvo):
    lista = []

    for x in nums:
        if (alvo - x) in lista:
            return True
        lista.append(x)

    return False


soma_alvo([1, 2, 3], 5)