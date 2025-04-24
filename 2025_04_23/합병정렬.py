def merge_sort(arr, depth=0):
    print(f"[정렬시작] 배열: {arr}\n")
    
    if len(arr) <= 1:
        print(f" -> 반환 (정렬 완료): {arr}\n")
        return arr
    
    mid = len(arr) //2
    left = merge_sort(arr[:mid], depth +1)
    right = merge_sort(arr[mid:], depth +1)
    
    print(f"병합 시작: {left} + {right}")
    merged = merge(left, right)
    print(f"병합 완료: {merged}")
    print("-" * 40)
    return merged

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:]), result.extend(right[j:])
    return result

arr = [5, 3, 1, 4, 2]
print("초기 배열:", arr), print("="*40)
sorted_arr =merge_sort(arr)
print("=" * 40), print("최종 정렬 결과:", sorted_arr)