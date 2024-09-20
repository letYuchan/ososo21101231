# swap func
a = 3
b = 4
(a, b) = (b, a)
print(a, b)

# 진법
a = 329 # decimal
b = 0b1101 # binary
c = 0o511 # octal
d = 0x149 #hexadecimal

#허수
a = 3.29+ 8.2j #j는 허수 단위
print(a.real) # 실수부
print(a.imag) # 허수부
print(a)

#none type: 값이 없음 -> 조건문에서 활용
type(None)
print(None == False) # false 

#서식문자와 포맷함수
# %s - string,  %d - integer, %f - float
print('My name is %s and my room is %d' % ('Choi', 327)) # % - 서식연산자: 직관적으로 서식문자와 그에 해당하는 값들을 연결시켜줌
print('My nmae is {1} and my room is {0}' .format(327, 'choi')) # .format(): %와 역할은 같으나 더 복잡한 포맷팅에 적합하고, 인덱스활용이 가능
                # 327은 0번째 인덱스를 'choi'는 1번째 인덱스를 가짐, {}안에 원하는 인덱스를 써서 작성 순서에 관계없이 인덱스로 삽입 가능

#string 연산
name = 'Cho'
str1 = 'myname is ' + name 
print(str1)

#f-string: 좀 더 편하게 포맷팅하기 위한 함수
# f"{삽입변수}"
age = 23
print(f"이름: {name}, 나이: {age}")

#string-trimming: 불필요한 공백이나 특정문자를 제거하는 함수
text = "    hello world"
clean_text = text.strip() # 디폴트값: 공백지우기
print(clean_text)
text = "\t\nhello world"
clean_text = text.strip('\t\n')
print(clean_text)
#lstrip() : 지정한 문자열이나 서식 중 왼쪽에 있는것만 제거
#rstrip() : 반대

#splitting: 해당 문자열을 기준으로 나눠서 리스트(대체로)로 반환
prof = 'Choi, 327, 1'
split_prof = prof.split(',')
print(split_prof)
split_prof = prof.partition(',') # 첫번째로 나오는 해당문자열을 기준으로 양옆으로 나눔 -> ,가 나올때마다 파티션을 설치하는게 아님을 주의, 튜플로반환
print(split_prof)
profs = """my name is
Cho"""
split_prof = profs.splitlines() # 라인을 기준으로 나눔, 리스트로 반환
print(split_prof)

#matching & searching
profs = [
    'My name is Choi and my E-mail is sunglok@seoultech.ac.kr',
    'My name is Kim and my e-mail address is jindae.kim@seoultech.ac.kr.'
]
for line in profs:
    print('e-mail' == line) # matching -> 완전히 같냐를 물음
    print('e-mail' in line) # searching -> 서브문자열이 포함되어있냐
    print('e-mail' in line.lower()) # line을 모두 소문자로 변경 후 포함여부를 물음
    print(line.find('e-mail')) # 해당 문자열이 처음 나타나는 위치를 반환, 없으면 -1 반환
    print(line.endswith('.')) # 문자열이 특정접미사로 끝나는지 물음
    
# compound data: union -> 집합 합체, update -> 딕셔너리 아이템 추가, append -> 리스트 아이템 추가(맨 뒤에), add -> 집합 원소 추가
prof_tuple = ('Choi', 327, True)
prof_list = ['Choi', 327, True]
prof_set = {'Choi', 327, True}
prof_dict = {'name': 'Choi', 'room_no': 327, 2021: True}

new_prof_set = prof_set.union({'SeoulTech'}) # 새로운 set으로 반환
print(new_prof_set)

prof_dict.update({'room_no' : 109}) # 기존 변수에 업데이트
print(prof_dict)

prof_set.add('Mirae Hall')
print(prof_set)

prof_list.append('hello world')
print(prof_list)
# 뭐가 기존변수를 업데이트하고 뭐가 새로운 객체를 반환하는지는 함수이름 감으로 보면 됨 ex) union 둘을 합친다 -> 새롭게 반환해야겠지?    
# string도 immutable data type임, 즉 다시말해 수정한다면 새 str 객체를 생성하므로 기존 변수에 재할당하거나 다른 변수에 할당해야함

# lambda expression: 익명함수
# lambda argu: expression
data = [3, 2, 9]
data.sort() # 오름차순 정렬
print(data)
data.sort(reverse=True) # 내림차순 정렬
print(data)
data.sort(key=lambda x: abs(x-4)) # key는 각 아이템들을 의미, 각 아이템 값에서 4를 뺀 값을 새롭게 재삽입
print(data)

# .sort() 대신 sorted(list)를 한다면 새로운 객체를 반환
new_data = sorted(data, reverse=True) # 첫번째 인자: 수정할 리스트, 두번째 인자: 수정사항
print(new_data)

# operators
x = 2021
y = 2022
print(x == y)
print(x is y) # 'is' == '==',  둘이 같니?
print(1 in [1,2,3,4,5]) # 안에 포함되었니
print(5 not in range(5)) #range()함수는 숫자 시퀀스를 생성하는 객체, 안들어있지 않아?

#flow control
n = 7
f = 1
if n < 0:
    pass # pass: 아무런 동작을 취하지 않음 -> 아직 세부구현사항이 없을 때, 디버깅할 때
elif n == 0:
    pass
else:
    while n > 0:
        f = f*n
        n = n-1
print(f)

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores): # zip함수: iterable 객체들의 각 요소들을 서로 대응(같은 인덱스끼리 대응)시켜 튜플로 묶어버림
    print(name, score)


#function
# 파이썬에선 오버로딩 지원X₩

# def range(end, start=0, step=1):
#     if start > end:
#         (start, end) = (end, start)
#     return list(range(start, end, step))


# print(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(range(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(range(1, 10, 2)) # [1, 3, 5, 7, 9]
# print(range(10, step=2)) # [0, 2, 4, 6, 8], 인자의 순서와 상관없이 인자이름을 구체적으로 언급해주면 작성순서는 상관없는 듯
#  # print(range(step=2, 10)) # Error! ->  명시적으로 작성한 인자가 하나라도 있으면 나머지의 위치를 정확히 맞춰서 작성하거나, 명시적이지 않은 인자를 딱 하나만 남겨야 함
# print(range(step=2, end=10)) # Check the result
# print(range(10, step=2, start=1)) # [1, 3, 5, 7, 9] 
# print(range(10, 2, start=1)) # Check the result
# arg_tuple = (1, 10, 2)
# print(range(*arg_tuple)) # 위치기반인자 연산자 -> 튜플로 인자값을 넣어주는데 이제 인자의 순서(위치)가 정확히 맞아야함, [1, 3, 5, 7, 9] 
# arg_dict = {'end': 10, 'step': 2, 'start': 1}
# print(range(**arg_dict)) # 키워드기반인자 연산자 -> 튜플로 인자값을 넣어주는데 이제 인자의 키워드를 통해 값을 입력함 [1, 3, 5, 7, 9]

#OOP
from random import randint
class Dice:
    def __init__(self, boundary=(1, 6)): # A constructor
        self.__start = min(boundary) # 단순한 변수명이면 Public, __라는 접두사를 갖으면 private
        self.__end = max(boundary)
    def throw(self):
        return randint(self.start, self.end)
    

dice = Dice()
# print(dice.__start, dice.__end) # Error! -> 외부에서 접근불가능하므로
print(dice._Dice__start, dice._Dice__end) # 1 6

# File management

#file_read
#open(filename, mode-r,w,a,b): 파일을 열고 파일 객체를 반환
#read(읽을 바이트 수, default: 파일전체): 파일 내용 읽어드리기
#readline(읽을 바이트 수): 파일에서 한줄만 읽음
#readlines(읽을 바이트 수): 파일의 모든 줄을 읽고 각 줄을 리스트의 아이템으로 추가하여 리스트로 반환
#close(): 파일을 닫고 객체를 정리
#with expression as variable: 어떤 변수에 표현식을 담는다. 자원 간편 관리 문법 -> 메모리 자동 해제 기능 제공 -> 메모리 릭 문제 방지
f = open('/Users/master/dev/ososo21101231/exercise/0.basic.py', 'r')
lines = f.read()
print(lines)

while True:
    line = f.readline()
    if not line:
        break
    print(line)
    
with open('/Users/master/dev/ososo21101231/exercise/0.basic.py', 'r') as f: # close 없이도 자동으로 닫아줌
    for line in f.readlines():
        print(line.strip())
        
#Exception -> runtime error
try: # 오류가 발생할 수 있는 코드를 감쌈
    result = 10 / 0
except ZeroDivisionError as e: # 예외발생시 처리, ZeroDivisionError는 built-in inner except class임
    print("Cannot divide by zero:", e)

#package Import
# from "module_name" import "specific_function_or_variable_or_class"
# mean_var.py 참조
from mean_var import mean_var
data = [1,5,2,3,10]
processed_data = mean_var(data)
print(processed_data)








