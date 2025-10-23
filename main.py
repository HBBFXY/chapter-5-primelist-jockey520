def PrimeList(N):
    if N <= 2:
        return ""
    
    primes = []
    
    # 处理数字2
    if N > 2:
        primes.append("2")
    
    # 从3开始检查所有奇数
    for num in range(3, N, 2):
        is_prime = True
        # 检查到平方根
        sqrt_num = int(num ** 0.5) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    
    return ' '.join(primes)
