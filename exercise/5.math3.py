# 뉴턴 방법으로 함수의 최소값을 찾자
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 # 목적함수
fd = lambda x: 0.3*x**2 - 1.6*x - 1.5 # 1차 도함수
fdd = lambda x: 0.6*x - 1.6 # 2차 도함수

viz_range = np.array([-6, 12]) # 함수 그래프 범위
max_iter = 100 
min_tol = 1e-6 # 종료조건
x_init = 12 # Try -2, 0, and 16/6 (a saddle point)

# 시각화 준비
xs = np.linspace(*viz_range, 100) # viz_range 범위에서 100개의 점 생성
plt.plot(xs, f(xs), 'r-', label='f(x)', linewidth=2)
plt.plot(x_init, f(x_init), 'b.', label='Each step', markersize=12)
plt.axis((*viz_range, *f(viz_range)))
plt.legend()

x = x_init
for i in range(max_iter):
    # 뉴턴 방법 실행
    xp = x
    # 안장점 및 극대값 문제 해결을 위한 처리
    if abs(fdd(x)) < 1e-6:  # fdd가 0에 가까운 경우를 방지
        print("fdd(x) is too small, stopping iteration to avoid division by zero")
        break
    x = x - fd(x) / (fdd(x) + 1e-6)  # 분모에 작은 값을 더하여 0으로 나누는 것을 방지
    
    # 각 반복 단계의 값 출력
    print(f'Iter: {i}, x = {xp:.3f} to {x:.3f}, f(x) = {f(xp):.3f} to {f(x):.3f} (f\'(x) = {fd(xp):.3f}, f\'\'(x) = {fdd(xp):.3f})')

    # 시각적으로 업데이트
    lcolor = np.random.rand(3)
    approx = 0.5*fdd(xp)*(xs-xp)**2 + fd(xp)*(xs-xp) + f(xp)
    plt.plot(xs, approx, '-', linewidth=1, color=lcolor, alpha=0.8)
    plt.plot(x, f(x), '.', color=lcolor, markersize=12)

    # 종료 조건 체크
    if abs(x - xp) < min_tol:
        print(f"Converged at iteration {i}")
        break

# 최종 결과 출력
plt.show()



# Scipy 라이브러리를 활용한 최적화 문제 풀기(극소값 찾기)
# 필요한 라이브러리 임포트
import numpy as np               # 수치 계산을 위한 NumPy 라이브러리
import matplotlib.pyplot as plt   # 그래프 시각화를 위한 Matplotlib 라이브러리
from scipy.optimize import minimize  # 최적화 문제를 해결하기 위한 SciPy의 minimize 함수

# 목적 함수 정의: f(x) = 0.1x^3 - 0.8x^2 - 1.5x + 5.4
f = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 

# 그래프 범위를 설정 (x의 최소값과 최대값)
viz_range = np.array([-6, 12]) 

# 최적화 관련 변수 설정
max_iter = 100            # 최대 반복 횟수
min_tol = 1e-6           # 수렴 조건: 두 값의 차이가 이 값보다 작아지면 종료
x_init = 12               # 초기값 설정 (여기서는 12로 시작)

# SciPy를 이용하여 최소값 찾기
result = minimize(f, x_init, tol=min_tol, options={'maxiter': max_iter, 'return_all': True})

# 최적화 결과 출력
print(result)  # 결과에는 극소값, 반복 횟수, 성공 여부 등이 포함됨

# 그래프를 그리기 위한 x값 생성
xs = np.linspace(*viz_range, 100)  # 지정한 범위에서 100개의 점 생성
plt.plot(xs, f(xs), 'r-', label='f(x)', linewidth=2)  # 함수 f(x)의 그래프를 빨간 선으로 그리기

# 모든 반복 과정에서의 x값을 수직 배열로 변환
xr = np.vstack(result.allvecs)  
plt.plot(xr, f(xr), 'b.', label='Each step', markersize=12)  # 각 단계에서의 f(x) 값을 파란 점으로 표시

# 그래프의 범례와 축 범위 설정
plt.legend()  # 범례 추가
plt.axis((*viz_range, *f(viz_range)))  # x축과 y축의 범위 설정
plt.show()  # 그래프를 화면에 표시

# 선형회귀를 통한 최적화 문제
# 진짜 직선을 정의하는 함수: y = -14/3*x + 14/3
true_line = lambda x: -14/3*x + 14/3

# 데이터의 범위 설정
data_range = np.array([-4, 12])  # x 값의 범위를 -4에서 12까지 설정
data_num = 100                     # 생성할 데이터 포인트의 수
noise_std = 1                      # 가우시안 노이즈의 표준편차

# 진짜 데이터 생성
# data_range 내에서 균등하게 분포된 x 값 100개를 생성
x = np.random.uniform(data_range[0], data_range[1], size=data_num)
# 진짜 y 값 생성
y = true_line(x)

# 가우시안 노이즈 추가
# x 값에 노이즈를 추가하여 xn 생성
xn = x + np.random.normal(scale=noise_std, size=x.shape)
# y 값에도 노이즈를 추가하여 yn 생성
yn = y + np.random.normal(scale=noise_std, size=y.shape)

# 대수적 거리를 최소화하는 직선 찾기
# xn과 1로 이루어진 행렬 A를 수직 스택하여 행렬 A를 생성
A = np.vstack((xn, np.ones(xn.shape))).T
b = yn  # y 값은 b로 설정
# 피팅된 직선의 계수를 계산: A의 무어-펜로즈 유사 역행렬을 사용
l_alg = np.linalg.pinv(A) @ b
# 피팅된 직선의 평균 절대 오차 계산
e_alg = np.mean(np.abs(l_alg[0]*xn - yn + l_alg[1]) / np.sqrt(l_alg[0]**2 + 1))

# 기하학적 거리를 최소화하는 직선 찾기
# 기하학적 거리 함수 정의
geo_dist2 = lambda x: np.sum((x[0]*xn - yn + x[1])**2) / (x[0]**2 + 1)
# 기하학적 거리를 최소화하는 결과를 찾기 위해 minimize 함수 호출
result = minimize(geo_dist2, [-1, 0])  # 초기값 설정: y = -x로 시작
l_geo = result.x  # 최적화 결과에서 직선의 계수 추출
# 기하학적 거리의 평균 절대 오차 계산
e_geo = np.mean(np.abs(l_geo[0]*xn - yn + l_geo[1]) / np.sqrt(l_geo[0]**2 + 1))

# 데이터 및 결과를 시각화
plt.plot(data_range, true_line(data_range), 'r-', label='The true line')  # 진짜 직선
plt.plot(xn, yn, 'b.', label='Noisy data')  # 노이즈가 추가된 데이터 포인트
plt.plot(data_range, l_alg[0]*data_range + l_alg[1], 'g-', label=f'Solve Ax=b (GeoError: {e_alg:.3f})')  # 대수적 거리 피팅 결과
plt.plot(data_range, l_geo[0]*data_range + l_geo[1], 'm-', label=f'Optimization (GeoError: {e_geo:.3f})')  # 기하학적 거리 피팅 결과
plt.legend()  # 범례 추가
plt.xlim(data_range)  # x축의 범위 설정
plt.show()  # 그래프를 화면에 표시


# 이 코드는 노이즈가 포함된 데이터에 대한 선형 회귀를 통해 최적의 직선을 찾는 과정을 나타냅니다. 다음은 이 코드가 목표로 하는 바를 요약한 내용입니다:

# 코드의 목적 및 설명
# 진짜 직선 정의:

# 진짜 데이터는 선형 관계를 갖고 있으며, 이 코드에서는 true_line 함수를 통해 정의된 진짜 직선이 있습니다. 이 직선은 데이터의 실제 관계를 나타냅니다.
# 노이즈가 포함된 데이터 생성:

# 진짜 직선 위의 
# 𝑦
# y 값에 가우시안 노이즈를 추가하여 노이즈가 포함된 데이터 포인트를 생성합니다. 이는 현실 세계에서 수집한 데이터가 항상 완벽하지 않음을 반영합니다.
# 두 가지 피팅 방법:

# 대수적 거리 최소화: 데이터 점들과 직선 사이의 수직 거리의 합을 최소화하는 직선을 찾습니다. 이 방법은 각 데이터 포인트와 피팅된 직선 사이의 수직 거리를 기준으로 최적화합니다.
# 기하학적 거리 최소화: 데이터 점들과 직선 사이의 실제 거리를 최소화하는 직선을 찾습니다. 이 방법은 거리의 제곱을 합산하여 최적의 직선을 도출합니다.
# 결과 시각화:

# 최종적으로, 그래프를 통해 진짜 직선, 노이즈가 포함된 데이터 점들, 그리고 두 가지 방법으로 찾은 최적의 직선을 시각적으로 보여줍니다. 이를 통해 각 방법이 어떻게 데이터에 적합하게 직선을 찾는지 비교할 수 있습니다.
