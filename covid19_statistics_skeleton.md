# 마크다운 파일 쓰기
with open("covid19_statistics.md", "w") as f:

    # 인구 데이터 출력
    f.write('### Korean Population by Region\n')
    f.write('* Total population: %d\n' % sum_people)
    f.write('\n')  # 빈 줄 추가
    f.write('| Region | Population | Ratio (%) |\n')
    f.write('| ------ | ---------- | --------- |\n')
    for idx, pop in enumerate(n_people):
        ratio = (pop / sum_people)*100
        f.write('| %s | %d | %.1f |\n' % (regions[idx], pop, ratio))
    f.write('\n')  # 빈 줄 추가

    # COVID-19 신규 확진자 데이터 출력
    f.write('### Korean COVID-19 New Cases by Region\n')
    f.write('* Total new case: %d\n' % sum_covid)
    f.write('\n')
    f.write('| Region | New Cases | Ratio (%) | New Cases / 1M |\n')
    f.write('| ------ | --------- | --------- | -------------- |\n')
    for idx, new_cases in enumerate(n_covid):
        covid_ratio = (new_cases / sum_covid) * 100
        f.write('| %s | %d | %.1f | %.1f |\n' % (regions[idx], new_cases, covid_ratio, norm_covid[idx]))
    f.write('\n')
