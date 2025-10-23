def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    for num in range(2, N):
        is_prime = True
        if num > 2 and num % 2 == 0:
            continue
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))

    if N > 2:
        primes.insert(0, "2")
    return ' '.join(primes)

# 测试示例
print(PrimeList(10))  
print(PrimeList(3))   
print(PrimeList(2))   
