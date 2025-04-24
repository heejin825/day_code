# 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"\n{i+1}회전 시작: {arr}")
        
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f" -> {arr[j]}와 {arr[j+1]} 교환 -> {arr}")
            else:
                print(f" -> {arr[j]}와 {arr[j+1]} 그대로")
                
    return arr

data = [5, 3, 1, 4, 2]
print("정렬 전:", data)
sorted_data = bubble_sort(data.copy())
print("\n정렬 후:", sorted_data)


