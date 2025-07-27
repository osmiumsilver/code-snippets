def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)  # 初始化所有数字为 True (可能是素数)
    primes[0] = primes[1] = False  # 0 和 1 不是素数

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:  # 如果 i 是素数
            for multiple in range(i * i, limit + 1, i):  # 将 i 的倍数标记为 False
                primes[multiple] = False

    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

# 示例
primes = sieve_of_eratosthenes(100)
print(primes)  # 输出小于等于 100 的所有素数