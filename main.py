#Linear time Complexity: O(n)

def func(n):
    iteration = 0
    sum = 0

    for i in range(1, n+1):
        sum = sum + i
        iteration += 1

    print(f"For input size {n}, the iteration {iteration}")
    return sum

print(func(5))
print(func(100))
print(func(500))
