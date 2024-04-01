class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0  # There are no prime numbers less than 2
        primes = [True] * n
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        return sum(primes)

# Driver code
print("Enter a number : ")
n=int(input())
sol=Solution()
print(sol.countPrimes(n))