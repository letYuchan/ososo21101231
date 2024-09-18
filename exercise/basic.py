# 파이썬은 {}로 구분하지 않음, :으로 구분함 그리고 각 코드의 스코프는 
# 들여쓰기 정도로 구분되어지므로 주의하자
# hello wolrd
print("hello world!")
print(3.29)
# int
a = 329

# float
a = 3. # == 3.0
b = 3.29

# bool
c = False
if(c == 0):
    print("같습니다")
else:
    print("다릅니다")

#string
name = "cho"
multiLineStr = "Yuchan\nCho"
multiLineSTrDifferentVer = """Yuchan
cho"""
print(multiLineSTrDifferentVer)

#compound data
# tuple, list, set, dictionary
prof_tuple = ("Cho", 30, False)
print(prof_tuple)
prof_list = ["Cho", 30, False]
print(prof_list)
prof_set = {"Cho", 30, False}
print(prof_set)
prof_dict = {"name" : "Cho", "age" : 30, "isStudent" : False}
print(prof_dict)

#indexing
print(prof_dict["name"])
print(prof_list[-1])

#slicing
prof_str = "Choi"
print(prof_str[1:3])
print(prof_str[1:])
print(prof_str[1::2])

# add, concat, remove etc..
prof_set = prof_set.union({327, 'mirae hall', 'seoulTech'}) # 새집합을 반환, 기존집합 변경x
print(prof_set)
prof_list.append("mirae hall")
print(prof_list)
prof_set.add('ky')
print(prof_set)
prof_dict["building"] = "mirae hall"
print(prof_dict)

# type check
print(type(prof_str)==str)
print(len(prof_str)==4)
print(int(3.29) == 3)
print(str(3)=='3')

# operator: notable
result = 7/3
print(result) #return float type
result = 7//3
print(result) #return int type

print((not 3.29 > 3) and (10.18 <10 or 5.12 >5))

x = 3
is_odd = True if x % 2 == 1 else False # ternary op like is_odd = (x%2) == 1 ? 1: 0; 

# flow control
# for 변수 in 시퀀스: 실행코드
n = 7
for x in range(2, n): #여기서 x는 2부터 7까지 x++을 하면서 값 증가, range(start, stop, step)
    if(n%x == 0):
        print(n, 'equals', x, "*", n//x)
        break
    else:
        print(n, "is a prime number")
        
year_list = [1982,1984,2014,2016]
for idx in range(len(year_list)): # 숫자 시퀀스에 주로 활용
    print(idx) # print index
for item in year_list: 
    print(item) # print item
for idx, item in enumerate(year_list): # 각 요소와 해당하는 인덱스 같이 반환
    print(idx, item) # print index & item
        
# function definition
def factorial_for(n):
    f = 1
    for m in range(1, n+1):
        f *= m
    return f
    
def factorial_rec(n=1):
    if n<=0:
        return 1
    else:
        return n*factorial_rec(n-1)
print(factorial_for(10))
print(factorial_rec(10))

# multiple return values: 다중값 리턴시 파이썬에선 튜플로 반환
def mean_var(data):
    n = len(data)
    if n > 0: # data가 하나 이상이라면
        mean = sum(data) / n # 평균을 구하고
        sum2 = 0
        for datum in data:
            sum2 += datum**2 
        var = sum2 / n - mean**2 # 분산을 구한 후
        return mean, var # multiple return
    return None, None 
    
data = [3,2,9,1,0,8,7,5]
pair = mean_var(data) # (4.375, 9.984)
print(pair)
mean, var = mean_var(data)
mean, _ = mean_var(data) # get only the first one
mean = mean_var(data)[0] # samething

# OOP: class and obj
# dice and coin
from random import randint # == #include

class Dice: 
    def __init__(self, boundary=(1,6)): # 생성자 함수로 __init__이란 이름은 꼭 써줘야함
        # self는 this와 동일한 의미이며, 인스턴스 자신을 참조한다. self는 클래스 내 모든 메서드의 첫번째 인자로 반드시 포함되어야 한다
        self.start = min(boundary) 
        self.end = max(boundary)
        
    def throw(self):
         return randint(self.start, self.end)
     
dice = Dice()
print(dice.throw()) # dice의 범위는 1~6

coin = Dice((0,1))
print(coin.throw()) # coin은 앞(0) 혹은 뒤(1) 이므로 dice의 범위를 축소시키면 됨
        