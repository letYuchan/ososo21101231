# swap
a = 3
b = 4
temp = a
a = b
b = temp
print(a, b)

(a, b) = (b, a)
print(a, b)

# math
import math
factorial_prod = lambda n: math.prod(range(1, n+1))
print(factorial_prod(10))

print(math.sqrt(16))
print(math.ceil(15.5))
print(math.sin(math.degrees(45)))
print(math.atan(math.radians(45)))
print(math.log2(4))
print(math.isinf(9.999))

# decimal
print(round(3.5)) # 4
print(round(4.5)) # 4

import decimal

print(decimal.Decimal(3.5).quantize(1, decimal.ROUND_HALF_UP)) # 4
print(decimal.Decimal(4.5).quantize(1, decimal.ROUND_HALF_UP)) # 5

# random
import random
print(100*random.random())
print(random.randint(a, b)) # a <= n <= b
print(random.uniform(5.0, 10.5)) # a <= float <= b

# time
import time

print(time.time())
print(time.process_time())
print(time.thread_time())
print(time.gmtime())
print(time.localtime())
print(time.asctime())
print(time.ctime())

# glob
import glob
print(glob.glob("*.py"))

# fnmatch
import fnmatch
profs = ["My name is Choi and my E-mail is sunglok@wseoultech.ac.kr",
         "My name is Kim and my e-mail address is jindae.kim@seoultech.ac.kr"]

print([fnmatch.fnmatch(prof, '*e-mail*') for prof in profs])
print([fnmatch.fnmatchcase(prof, '*e-mail*') for prof in profs])
print([fnmatch.fnmatchcase(prof, '*[Ee]-mail*') for prof in profs])

print(fnmatch.filter(profs, '*e-mail*')) # 대소문자 구분
print(fnmatch.filter(profs, '*Ch?i*'))

# csv
# import csv
# files = glob.glob('file_directory') # 파일 읽기
# all_data = [] 
# for file in files: # 각 파일을 열고
#     with open(file, 'r') as f:
#         csv_reader = csv.reader(f) 
#         data = []
#         for line in csv_reader: # 각 파일의 내용을 한줄 한줄 읽는데
#             if line and not line[0].strip().startswith('#'): # #으로 시작하지 않는, 즉 제목줄이 아닌 데이터부분만 골라서
#                 data.append([int(val) for val in line]) # 데이터를 추출하고
#         all_data = all_data + data # 추출한 데이터를 all_data에 넣는데, 여러파일을 돌아가면서 계속 추출한 data[]를 all_data에 넣는다.

# # pickle
# import pickle
# with open("~", "wb") as f:
#     pickle.dump((files, all_data), f)

# with open("~", "rb") as f2:
#     _, data = pickle.load(f)
#     print(data)

# # tkinter
# import tkinter as tk
# from fnmatch import fnmatch

# # Generate reply to the given message
# def reply_msg(msg):
#     if fnmatch(msg, '*hello*') or fnmatch(msg, '*good morning*'):
#         return 'Hello'
#     elif fnmatch(msg, '*what*you*name*'):
#         return 'My name is OSS Chatbot.'
#     return "I don't understand your words."

# # Handle events from 'button_send'
# def handle_button_send():
#     text_dialog.insert('end', 'You: ' + entry_msg.get() + '\n')
#     text_dialog.insert('end', 'Bot: ' + reply_msg(entry_msg.get()) + '\n')
#     entry_msg.delete(0, tk.END)  # Clear 'entry_msg' after reply

# # Add widgets to GUI
# root = tk.Tk()
# root.title('A Very Simple Chatbot')

# label = tk.Label(root, text='Chat Dialog')
# label.pack()

# text_dialog = tk.Text(root)
# text_dialog.pack()

# label = tk.Label(root, text='Your Message:')
# label.pack()

# entry_msg = tk.Entry(root)
# entry_msg.pack()

# button_send = tk.Button(root, text='Send Your Message', command=handle_button_send)
# button_send.pack()

# root.mainloop()

# turtle
import turtle
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

# tqdm
from tqdm import tqdm
n = 10000
for i in tqdm(range(n)):
    pass
   

