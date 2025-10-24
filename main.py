import math

def PrimeList(N):

    if N <= 2:
        return ""
    
    is_prime = [True] * N
    is_prime[0] = False 
    is_prime[1] = False 
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    primes = [str(num) for num in range(2, N) if is_prime[num]]
    
    return " ".join(primes)

def main():    
    while True:
        user_input = input("请输入一个整数 : ").strip()
        if not user_input.isdigit():
            print("错误：请输入一个有效的正整数！\n")
            continue
        
        N = int(user_input)
        
        if N <= 0:
            print("错误：请输入一个大于0的正整数！\n")
            continue
        
        result = PrimeList(N)
        
        if result:
            print(f"小于 {N} 的所有质数为:")
            print(result)
        else:
            print(f"小于 {N} 的质数不存在")
        
        print() 

if __name__ == "__main__":
    main()
