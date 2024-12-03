import numpy as np
import pandas as pd
from scipy.optimize import minimize

# CSV 파일에서 데이터 부르기
file_path = '/Users/master/ososo21101231/midTerm/circle.csv'  # 파일 경로
data = pd.read_csv(file_path, header=None)  # header 없는 경우 처리
points = data.to_numpy()

# 각 영역에 따라 정의된 거리의 제곱합을 계산하는 함수 정의
def calculate_squared_distances(params, points):
    a, b, r = params
    total_distance = 0  # 총 거리 초기화
    
    for x, y in points:
        # 거리 계산
        vertical_distance = abs(np.sqrt((x - a)**2 + (y - b)**2) - r)  # Blue 영역
        horizontal_distance = abs(x - a)  # Green 영역
        fixed_distance = 100  # Red 영역
        
        # 영역 결정, reference) chat-GH
        if abs(y - b) >= abs(x - a):  # Blue 영역이 Green과 Red보다 우선
            total_distance += vertical_distance**2
        elif abs(y - b) < abs(x - a):  # Green 영역
            total_distance += horizontal_distance**2
        else:  # Red 영역
            total_distance += fixed_distance**2
    
    return total_distance  # 총 거리 반환

# 초기 추정값 (a, b, r)
initial_guess = (0, 0, 1)

# 거리의 제곱합을 최소화
result = minimize(calculate_squared_distances, initial_guess, args=(points,), method='L-BFGS-B')

# 최적화된 파라미터 추출
a, b, r = result.x

# 결과 출력
print(f"최적화된 원의 파라미터: a = {a}, b = {b}, r = {r}")

# 결과:
# 최적화된 원의 파라미터: a = 3.7346066656053014, b = 27.435331279846668, r = 9.17575092039576
