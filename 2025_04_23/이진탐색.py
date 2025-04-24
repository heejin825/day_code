def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    count = 0
    
    while left <= right:
        count += 1
        mid = (left + right) // 2
        print(f"[{count}회차] 중간 인덱스 = {mid}, 값 = {arr[mid]}")
        
        if arr[mid] == target:
            print (f"{count}번 만에 타겟 {target}을 찾았습니다!")
            return mid
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid -1
    
    print(f"{count}번 탐색했지만 타겟 {target}을 찾지 못했습니다.")
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 11

result = binary_search(arr, target)
print("찾은 인덱스:", result)