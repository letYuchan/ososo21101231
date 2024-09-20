# 각 지역별 인구에 따른 확진자수를 백만명당 발생한 신규환자수로 변환하여 리스트를 만드는 함수
def normalize_data(n_cases, n_people, scale):
        # TODO) Calculate the number of cases per its population
    norm_cases = [] # 지역별 확진자 수 리스트(작성한 코드로 아이템을 추가해줄 빈 리스트)
    for idx, n in enumerate(n_cases):
        normalizedData = (n/n_people[idx]) * scale # 확진자수를 지역인구수로 나누고 스케일만큼 곱한다
        norm_cases.append(normalizedData)
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227,  13530519, 3359527,     3322373,   2938429,     2630254, 2393626,    2118183,   1838353,   1792476,    1597179,   1536270,   1454679,   1441970, 1124459, 675883,   365309] # 2021-08
n_covid  = [    644,       529,      38,          29,       148,          28,      41,         62,        23,        27,         27,        33,        16,        40,      20,      5,        4] # 2021-09-21

sum_people = sum(n_people) # TODO) The total number of people
sum_covid  = sum(n_covid) # TODO) The total number of new cases
norm_covid = normalize_data(n_covid, n_people, 1000000) # The new cases per 1 million people

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print() # Print an empty line
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = (pop / sum_people)*100 #총 인구수대비 지역별 인구수 비율 # TODO) The ratio of new cases to the total
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))
print()

# TODO) Print COVID-19 new cases by region
print('### Korean COVID-19 New Cases by Region')
print('* Total new case:', sum_covid)
print()
print('| Region | New Cases | Ratio (%) | New Cases / 1M |')
print('| ------ | --------- | --------- | -------------- |')
for idx, new_cases in enumerate(n_covid):
    covid_ratio = (new_cases /sum_covid) * 100 #지역별 인구당 신규확진자수 비율 계산
    print('| %s | %d | %.1f | %.1f' % (regions[idx], new_cases, covid_ratio, norm_covid[idx])) # 순서대로 지역, 신규확진자 수, 인구수대비 신규확진자 수 비율, 백만명당 신규확진수
print()

# %: 포맷팅 연산자로, 포맷문자열 뒤에 오는 값들을 연결해주는 역할을 함.