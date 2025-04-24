def max_product_brute_force(arr):
    max_product = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            max_product = max(max_product, product)
    return max_product

arr = [1, 3, 5, 6, 9]
print("완전탐색", max_product_brute_force(arr))

def max_product_greedy(arr):
    return arr[-1] * arr[-2]

arr = [1, 3, 5, 6, 9]
print("그리디:", max_product_greedy(arr))