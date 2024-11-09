# sympy를 활용한 행렬 연산
print("-----sympy를 통한 기본 행렬연산-----")
import sympy as sp
a11, a12, a21, a22 = sp.symbols('a11 a12 a21 a22')
b11, b12, b21, b22 = sp.symbols('b11 b12 b21 b22')
A = sp.Matrix([[a11, a12], [a21, a22]])
B = sp.Matrix([[b11, b12], [b21, b22]])
print(A+B == B+A) # True
print(A*B == B*A) # False
print(A*B - B*A) # Check their difference

print("-----numpy로 행렬 초기화-----")

#numpy : matrix library
# numpy init
import numpy as np
A = np.array([3, 29, 82]) # 1차원
B = np.array(((3.,29, 82), (10,18,24))) # 2차원(2행 3열)
C = np.array([[3, 29, 82], [10, 18, 84]], dtype = float) # 2차원(2행 3열), 요소를 float64로 취급
D = np.array([3, 29, 'Choi']) # 1차원, choi때문에 모든 요소가 문자열취급 -> u21(UTF, 최대문자 21개)
E = np.array([[3], [29], [82]]) # 2차원(3행 1열)

print("-----행렬 정보 출력-----")

print(A.ndim, A.size, A.shape, A.dtype) #ndim -> 몇차원인지 / size -> 요소개수 / shape -> 배열의 모양 (행수, 열수) / dtype -> 요소 데이터타입
print(B.ndim, B.size, B.shape, B.dtype) 
print(C.ndim, C.size, C.shape, C.dtype)
print(D.ndim, D.size, D.shape, D.dtype)
print(E.ndim, E.size, E.shape, E.dtype) # 1차원은 모든 요소를 행취급(shape으로 확인)

print("-----행렬관련 numpy 다양한 함수-----")

# create Fn
F = np.zeros((3, 2)) # 3*2 행렬 생성 후 0으로 채움(default: float64) / (shape, dtype)
G = np.ones((3, 2)) # 3*2, 모든 요소 1로 채움 / (shape, dtype)
H = np.eye(3, dtype=np.float32) # 3*3 단위 행렬(대각선 1, 나머지 0) / (N, dtype) -> N*N
I = np.empty((3, 2)) # 초기화되지 않은 3*2배열 생성 (shpae, dtype)
J = np.empty((0, 9)) # [ ] with size of (0, 9)
K = np.arange(0, 1, 0.2) # Step 0.2: array([0., 0.2, 0.4, 0.6, 0.8]) / (start_num, stop_num, step) -> not including stop_num (<)
L = np.linspace(0, 1, 5) # Number 5: array([0., 0.25, 0.50, 0.75, 1.]) / (start_num, stop_num, num) -> 스타트숫자부터 스탑숫자(포함)까지 동일한 간격으로 num개 만큼 숫자 생성
M = np.random.random((3, 2)) # (shape) -> 0부터 1까지의 난수를 shape에 맞춰 fill

print("-----행렬 인덱싱& 슬라이싱-----")

# indexing and slicing
A = np.array(((3., 29, 82), (10,18,84)))
# 3 29 82
# 10 18 84

A[1][1] # 두번째행 두번째 열 -> 18.0
A[1, 1] # 첫번째와 동일한 접근법 (배열만 가능한 인덱싱 방법)
A[1,1:2] # 두번째(1)열부터 두번째열(<2)까지의 값을 슬라이드 -> array([18.])
A[1,:] # 두번째 행, 모든 열, get a row ->  array([10., 18., 84.])
A[:,2] # 세번째 열, Get a column -> array([82., 84.])
A[0:2,0:2] # Get a submatrix: array([[3., 29.], [10., 18.]])
# 2. Logical indexing
A > 80 # array([[False, False, True], [False, False, True]])
A[A > 80] # array([82., 84.])
A[A > 80] = 80 # 80보다 큰 값에 80 할당
# 3. Fancy indexing
A[(1, 0, 0), (1, 0, 2)] # array([18., 3., 82.])
# Get items at (1, 1), (0, 0), (0, 2) -> 첫번째 튜플은 행을 두번째 튜플은 열을

print("-----행렬 대수 연산-----")

# Arithmetic operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# 같은 위치에 존재하는 요소끼리 연산
print(A+B)
print(A-B)
print(A*B)
print(A/B)

print("-----고급 행렬연산-----")

print(A.T) # A.transpose() -> 전치행렬(행과열을 바꿈)
print(A @ B) # 행렬연산의 곱셈
print(np.linalg.norm(A)) # 5.48 (default: L2-norm) -> 원소들의 제곱값을 모두 더 한 후 루트씌워준 값
print(np.linalg.matrix_rank(A)) # 2, full rank -> rank란 선형 독립적인 행 또는 열을 의미
print(np.linalg.det(A)) # -2, -> 행렬식 구하기(0이 아니면 역행렬 존재)
print(np.linalg.inv(A)) # Matrix inverse -> 역행렬 구하기 A×A^−1=I (여기서 I는 단위 행렬), 역행렬이 존재한다-> 행렬식이 0이 아니다
print(np.linalg.pinv(A)) # Matrix pseudo-inverse -? 의사역행렬 구하기, 역행렬이 존재하지 않을때 근사적으로 역행렬 역할을 함
# 3. Broadcasting: 행렬의 크기가 다르면 몇몇 연산은 진행불가인데, 이를 넘파이에서 자동으로 크기를 맞춰줌
print(A + 1) # [[2, 3], [4, 5]] -> 모든 요소에 1더함
print(A + [0, -1]) # [[1, 1], [3, 3]] -> 크기가 맞지 않아도 첫번째 열에는 0을 더하고 두번째 열에는 -1을 더함
print(A + [[1], [-1]]) # [[2, 3], [2, 3]] -> 첫번째 행에 1을 덛하고 두번째 행에 -1을 더함

print("-----linear타입 모델 시각화-----")

# 이제 시각화를 해볼까요?
import matplotlib.pyplot as plt
true_line = lambda x: -2/3*x + 14/3
data_range = np.array([-4, 12])
data_num = 100
noise_std = 0.5
# Generate the true data
x = np.random.uniform(data_range[0], data_range[1], size=data_num)
y = true_line(x) # y = -2/3*x + 10/3
# Add Gaussian noise
xn = x + np.random.normal(scale=noise_std, size=x.shape)
yn = y + np.random.normal(scale=noise_std, size=y.shape)
# Solve the system of equations
A = np.vstack((xn, np.ones(xn.shape))).T
b = yn
line = np.linalg.pinv(A) @ b
# Plot the data and result
plt.title(f'Line: y={line[0]:.3f}*x + {line[1]:.3f} ')
plt.plot(data_range, true_line(data_range), 'r-', label='The true line')
plt.plot(xn, yn, 'b.', label='Noisy data')
plt.plot(data_range, line[0]*data_range + line[1], 'g-', label='Estimate')
plt.xlim(data_range)
plt.legend()
plt.show()

print("-----곡선그리기 baisc-----")

# 곡선 그리기
true_curve = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 # 3차 다항식 정의
data_range = (-6, 12) # x범위
data_num = 100 # 생성할 데이터 포인트 수
noise_std = 0.5 # 가우시안 노이즈의 표준편차
# Generate the true data
x = np.random.uniform(data_range[0], data_range[1], size=data_num)
y = true_curve(x)
# Add Gaussian noise
xn = x + np.random.normal(scale=noise_std, size=x.shape)
yn = y + np.random.normal(scale=noise_std, size=y.shape)
# 행렬 A b 생성 및 해 구하기
A = np.vstack((xn**3, xn**2, xn, np.ones(xn.shape))).T
b = yn
curve = np.linalg.pinv(A) @ b
# Plot the data and result
plt.title(f'Curve: y={curve[0]:.3f}*$x^3$ + {curve[1]:.3f}*$x^2$ + {curve[2]:.3f}*$x$ + {curve[3]:.3f}')
xc = np.linspace(*data_range, 100)
plt.plot(xc, true_curve(xc), 'r-', label='The true curve')
plt.plot(xn, yn, 'b.', label='Noisy data')
plt.plot(xc, curve[0]*xc**3 + curve[1]*xc**2 + curve[2]*xc + curve[3], 'g-', label='Estimate')
plt.xlim(data_range)
plt.legend()
plt.show()

print("-----buildA 함수를 정의해서 곡선그리기-----")

# model section: build 함수를 통해 위 코드보다 재사용성 및 가독성을 높임, 노이즈 표준편차를 높여 데이터가 더 산란함, 계수를 문자열로 출력, 실제 곡선의 계수를 따로 정의
def buildA(order, xs): # 차수에 따라 다항식의 디자인 행렬 생성
    A = np.empty((0, len(xs)))
    for i in range(order + 1):
        A = np.vstack((xs**i, A))
    return A.T
true_coeff = [0.1, -0.8, -1.5, 5.4] # 실제 다항식 계수 정의
poly_order = 3 # 사용할 다항식 차수 설정
data_range = (-6, 12)
data_num = 100
noise_std = 1 # 노이즈 표준편차 1
# Generate the true data
x = np.random.uniform(data_range[0], data_range[1], size=data_num)
y = buildA(len(true_coeff) - 1, x) @ true_coeff
# Add Gaussian noise
xn = x + np.random.normal(scale=noise_std, size=x.shape)
yn = y + np.random.normal(scale=noise_std, size=y.shape)
# Solve the system of equations
A = buildA(poly_order, xn)
b = yn
coeff = np.linalg.pinv(A) @ b
# Plot the data and result
plt.title(f'Order: {poly_order}, Coeff: ' + np.array2string(coeff, precision=2, suppress_small=True))
xc = np.linspace(*data_range, 100)
plt.plot(xc, np.matmul(buildA(len(true_coeff) - 1, xc), true_coeff), 'k-', label='The true curve', alpha=0.2)
plt.plot(xn, yn, 'b.', label='Noisy data')
plt.plot(xc, np.matmul(buildA(poly_order, xc), coeff), 'g-', label='Estimate')  
plt.xlim(data_range)
plt.legend()
plt.show() 
print("-----특이행렬의 역행렬계산: 안됨!-----")

# 특이행렬일때 역행렬 계산
# import numpy as np
# A = np.array([[1., 1.], [1., 1.]]) # 이는 곧 두 방정식이 독립적이지 않다는 뜻 -> 동일한 x값이여도 서로다른 y값이 출력된다. 즉 해를 구할 수 없다
# b = np.array([[4.], [2.]])
# A_inv = np.linalg.inv(A) # Error! (singular matrix, 특이행렬)
# print(A_inv @ b)

# Null Space(영공간) & Rank-Nullity Theorem(순위 영차정리)
# 영공간: A라는 m*n 행렬에 대해 A를 곱했을 때 제로벡터를 만드는 모든 벡터의 집합 N(A)={v∈R^n∣Av=0}
# 순위-영차정리: rank(A)+nullity(A)=n (n은 행렬의 열 수) -> 독립적인 열(rank)의 개수와 영공간을 생성하는 1개의 벡터(nullity)의 합은 총 열의 개수이다. -> 전체정보는 독립적인 정보와 중복되는 정보의 합이다.
# 독립적이 열: 어떤 열 벡터를 다른 열 벡터의 선형결합으로 표현할 수 없음
# 예를들어 [1] 과 [0] 은 서로 독립적인 열임, 왜냐하면 하나의 열로 다른 열을 표현할 수 없음
#        [0]   [1] 

print("-----Null-space와 Rank-Nullity:scipy로 영공간 계산-----")

from scipy import linalg
A = np.array([[1., 4., 1.], [1., 2., 1.]])
x = linalg.null_space(A)
print(x / x[0]) # [[1.], [0.], [-1.]] Note) Line: x – 1 = 0