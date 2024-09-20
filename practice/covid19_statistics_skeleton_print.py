
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

with open("covid19_statistics.md", "w") as f:

    f.write('### Korean Population by Region\n')
    f.write('* Total population: %d\n' % sum_people)
    f.write('\n')  
    f.write('| Region | Population | Ratio (%) |\n')
    f.write('| ------ | ---------- | --------- |\n')
    for idx, pop in enumerate(n_people):
        ratio = (pop / sum_people)*100
        f.write('| %s | %d | %.1f |\n' % (regions[idx], pop, ratio))
    f.write('\n')  

    f.write('### Korean COVID-19 New Cases by Region\n')
    f.write('* Total new case: %d\n' % sum_covid)
    f.write('\n')
    f.write('| Region | New Cases | Ratio (%) | New Cases / 1M |\n')
    f.write('| ------ | --------- | --------- | -------------- |\n')
    for idx, new_cases in enumerate(n_covid):
        covid_ratio = (new_cases / sum_covid) * 100
        f.write('| %s | %d | %.1f | %.1f |\n' % (regions[idx], new_cases, covid_ratio, norm_covid[idx]))
    f.write('\n')
