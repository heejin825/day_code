compare_count = 0
pivot_history = []

def quick_sort(arr):
    global compare_count, pivot_history
    print(f"정렬할 배열: {arr}\n")
    
    if len(arr) <= 1:
        print(f"반환: {arr}")
        return arr
    
    pivot = arr[0]
    pivot_history.append(pivot)
    
    left = []
    right = []
    
    for x in arr[1:]:
        compare_count += 1
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    
    print(f"피벗: {pivot}")
    print(f"작은 값들: {left}"), print(f"큰 값들: {right}")
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    
    result = sorted_left + [pivot] + sorted_right
    print(f"병합 결과: {result}")
    return result


arr = [5, 3, 1, 4, 2]
print(f"초기 배열:", arr)

sorted_arr = quick_sort(arr)
print("\n최종 정렬 결과:", sorted_arr)
print(f"총 비교 횟수: {compare_count}")
print(f"피벗 선택 순서: {pivot_history}")
    