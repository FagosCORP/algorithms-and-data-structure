# Quadratic  - O(n ^ 2) - Polynomial
# por exemplo se existir 10 numeros vai ser executado 10 * 10
#
#
def quadratic_func(n):
    for i in n:
        for j in n:
            print(j)


quadratic_func([1, 2, 3, 4])


# O(1) + O(1)  + O(1) + O(n) + O(n)
# O(3) + O(2n) -> O(n)
# O(3) + O(n)
# O(n)
#
def combination_func(n):
    print(n[0])
    for value in range(5):
        print(value)
    for value in range(5):
        print(value)
    for value in range(5):
        print(value)
    print("valores")
    print("valores")
    print("valores")


combination_func([1, 2, 3, 4, 6])
