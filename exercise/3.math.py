import matplotlib.pyplot as plt
import tkinter as tk
import turtle, math

# matplotlib.pyplot으로 함수 plot(drawing)해보기
scale = 10
xs = [x/scale for x in range(-4*scale, 10*scale)]
ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]
plt.title('$y= 0.1x^3 - 0.8x^2 - 1.5x +5.4$')
plt.plot(xs, ys, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axis('equal')
plt.show() 


# 도함수구하기
scale = 10  # 그래프의 x 축을 더 세밀하게 조정하기 위해 scale을 10으로 설정

# xs는 -4에서 9.9까지의 값을 10등분하여 리스트로 저장 (더 부드러운 그래프를 위해 값을 더 많이 샘플링)
xs = [x/scale for x in range(-4*scale, 10*scale)]  # [-4.0, -3.9, -3.8, ..., 9.9]

# ys는 주어진 방정식 y = 0.1*x^3 - 0.8*x^2 - 1.5*x + 5.4에 대해 각 xs 값에 대응하는 y 값을 계산
ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]

# yt는 기울기 -3.5와 절편 7인 접선 방정식 y = -3.5*x + 7에 대해 각 xs 값에 대응하는 y 값을 계산
yt = [-3.5*x + 7 for x in xs]

# 빨간 실선('r-')으로 방정식 y를 그래프로 그림
plt.plot(xs, ys, 'r-', label='y')  # 라벨 'y'는 범례에 표시됨

# 파란 점선('b--')으로 x = 2에서의 접선 그래프를 그림
plt.plot(xs, yt, 'b--', label='tangent line at x=2')  # 라벨 'tangent line at x=2'는 범례에 표시됨

# x축 라벨을 'x'로 설정
plt.xlabel('x')

# y축 라벨을 'y'로 설정
plt.ylabel('y')

# 그래프에 그리드(격자)를 표시
plt.grid()

# 범례(legend)를 추가하여 그래프에서 각각의 선이 무엇을 나타내는지 보여줌
plt.legend()

# 설정된 그래프를 화면에 출력
plt.show()


# 터틀로 그래프 그리기
# y = 0.1*x**3 − 0.8*x**2 − 1.5*x + 5.4 방정식의 그래프를 그리기 위한 x, y, 기울기 값 생성
scale = 10  # x 값들을 더 세밀하게 나누기 위한 스케일 조정

# x 값들을 -4에서 9.9까지 10등분하여 리스트로 저장 (더 부드러운 곡선을 그리기 위해 x를 0.1 단위로 나눔)
xs = [x/scale for x in range(-4*scale, 10*scale)]

# 각 x에 대응하는 y 값을 방정식 y = 0.1*x^3 - 0.8*x^2 - 1.5*x + 5.4로 계산
ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]

# 각 x에서의 기울기 값을 미분 방정식 y' = 0.3*x**2 - 1.6*x - 1.5로 계산
yd = [0.3*x**2 - 1.6*x - 1.5 for x in xs]

# GUI 창 준비
root = tk.Tk()  # Tkinter로 새로운 창(root)을 생성
canvas = tk.Canvas(root, width=500, height=500)  # 500x500 크기의 캔버스 생성 (그래프를 그릴 화면)
canvas.pack()  # 캔버스를 창에 표시

# TurtleScreen과 RawTurtle 설정
screen = turtle.TurtleScreen(canvas)  # 캔버스를 터틀 스크린으로 사용 (Turtle 그래픽을 캔버스에서 구동)
actor = turtle.RawTurtle(screen, 'turtle')  # 터틀 'actor' 객체 생성
actor.radians()  # 각도 단위를 라디안으로 설정 (기본적으로 터틀은 각도를 도(degree)로 처리함)

# 그래프를 그리기 위한 설정
zoom = 20  # 그래프를 더 크게 보이도록 확대 (x와 y 좌표 값에 곱하여 적용)

# 터틀을 초기 시작 위치로 이동 (펜을 들고 이동, 첫 번째 x, y 값에서 시작)
actor.penup()
actor.setpos(zoom*xs[0], zoom*ys[0])  # 첫 번째 좌표 (x=xs[0], y=ys[0])로 이동
actor.pendown()  # 펜을 내려 그리기 시작

# x, y, 기울기(slope) 값을 하나씩 반복하면서 그래프를 그리기
for (x, y, slope) in zip(xs, ys, yd):
    actor.setpos(zoom*x, zoom*y)  # 확대된 좌표로 터틀을 이동
    actor.setheading(math.atan2(slope, 1))  # 기울기를 기준으로 터틀의 회전 각도를 설정 (atan2 함수는 기울기를 각도로 변환)

# 메인 루프 실행: 창을 유지하면서 터틀 그래픽을 지속해서 표시
screen.mainloop()  # Tkinter의 이벤트 루프를 실행하여 창이 닫힐 때까지 프로그램 유지


# sympy 사용
import sympy as sp

x,y = sp.symbols('x y') # 변수나 식을 수학적으로 조작 가능 -> 미분, 적분, 방정식 등 가능, 즉 우리가 흔히 아는 수학적기호로서 인식(미지수)
y = 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4
yd = sp.diff(y, x) # 미분
print(yd) # 도함수 출력
print(float(yd.subs({x: 2}))) # x = 2 일때 도함수 값

roots = sp.solveset(y, x) # y = 0일때 근 찾기
print(roots)

sp.pprint(sp.factor(y)) # factor(exp): 다항식을 인수분해
# pprint() 인수분해 식을 좀 더 보기좋게 출력

