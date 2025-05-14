import numpy as np

def calculate_cv(data):
   """
   변동계수(cv)를 계산하는 함수
   : param data : 숫자형 리스트 또는 배열
   : return     : 평균, 표준편차, 변동계수수
   """
   
   # 평균 계산
   mean = np.mean(data)
   # 표준편차 계산
   std_dev = np.std(data)
   # 변동계수 계산
   cv = (std_dev / mean) * 100
   return mean, std_dev, cv

# 테스트 데이터1 : 학생 성적(변동이 적음)
scores = [80, 82, 79, 81, 83]

# 테스트 데이터2 : 주식 수익률(변동이 큼)
returns = [5, -3, 10, 8, -2]

# 변동계수 계산 및 출력
print("변동계수 계산 결과")

# 학생 성적 변동계수
mean1, std_dev1, cv1, = calculate_cv(scores)
print(f"\n학생 성적: {scores}")
print(f"평균: {mean1:.2f}, 표준편차: {std_dev1:.2f}, 변동계수 {cv1:.2f}%")

# 주식 수익률 변동계수수
mean2, std_dev2, cv2 = calculate_cv(returns)
print(f"\n주식 수익률: {returns}")
print(f"평균: {mean2:.2f}, 표준편차: {std_dev2:.2f}, 변동계수: {cv2:.2f}%")