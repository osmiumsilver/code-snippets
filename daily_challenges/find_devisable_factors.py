def find_devisable_factors(number):
    """
    分解质因数函数
    输入:  num (要分解的整数)
    输出:  包含质因数的列表
    """
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    divisor =3
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number /= divisor
            divisor += 2
    if number> 1: factors.append(number)




    return factors
factors = find_devisable_factors(630)
print(factors)