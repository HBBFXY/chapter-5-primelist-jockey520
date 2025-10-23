def PrimeList(N):
    if N <= 2:
        return ""
    
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N, i):
                is_prime[j] = False
    
    primes = [str(i) for i in range(2, N) if is_prime[i]]
    return ' '.join(primes)

# 测试示例
print(PrimeList(10))  # 输出：2 3 5 7
print(PrimeList(3))   # 输出：2
print(PrimeList(2))   # 输出：""
