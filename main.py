def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    # 先处理数字2（仅添加一次）
    primes.append("2")
    # 遍历3到N-1的所有奇数（因为偶数除了2都不是质数）
    for num in range(3, N, 2):
        is_prime = True
        # 判断num是否为质数，只需要检查到其平方根
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 以空格分隔输出，末尾无空格
    return ' '.join(primes)

# 测试示例
print(PrimeList(10))  # 输出：2 3 5 7
print(PrimeList(3))   # 输出：2
print(PrimeList(2))   # 输出：""
