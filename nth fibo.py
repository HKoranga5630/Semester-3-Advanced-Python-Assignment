# 1. Tabulation
n = int(input("Enter your number: "))

array = [0] * (n + 1)

if n >= 1:
    array[1] = 1

for i in range(2, n + 1):
    array[i] = array[i - 1] + array[i - 2]

print("Your Fibonacci number:", array[n])
print("Array:", array)
   
   
   
# 2. Memoization
n = int(input("Enter your number: "))

memo = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]

print("Your Fibonacci number:", fibonacci(n))
print("Memo:", memo)