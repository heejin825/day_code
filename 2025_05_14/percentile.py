import numpy as np

def calculate_percentile(data,p):
    '''
    백분위수를 계산하는 함수
    : param data: 리스트의 형태의 숫자 데이터  
    : param p   : 백분위
    : return    : 백분위수 값
    '''
    
    # 1. 데이터 정렬(오름차순)
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # 2. 위치 계산
    position = n * p
    
    # 3-1. nxp가 정수인 경우우
    if position.is_integer():
        pos = int(position)
        # 두 값의 평균균
        percentile_value = (sorted_data[pos - 1] + sorted_data[pos]) / 2
    else:
        # 3-2. nxp가 정수가 아닌 경우
        pos = int(np.ceil(position)) # 올림하여 위치 결정 
        percentile_value = sorted_data[pos - 1]
        
    return percentile_value

# 테스트 데이터 (학생 점수)
scores = [52, 55, 58, 60, 63, 65]

# 백분위수 계산
percentiles = [0.25, 0.50, 0.75]
print('백분위수 계산 결과:')
for p in percentiles:
    result = calculate_percentile(scores, p)
    print(f"{int(p*100)}th Percentile: {result}")