import csv
def read_data(filename):
    # TODO) Read `filename` as a list of integer numbers
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].startswith('#'):  # 주석(헤더)인 줄은 건너뜀
                continue
            # 각 값을 정수로 변환하여 리스트에 추가
            data.append([int(value) for value in row])
    return data

def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`
    # 각 학생의 기말고사와 중간고사 점수를 각각의 weight와 곱하고 이를 더한다 -> 이 과정에서 data를 2차원으로 봐야함(weight의 첫번째요소와 row의 첫번째요소 이런식으로 매치시켜야하기 때문)
    average = []
    for row in data_2d:
        midterm_score = row[0]
        final_score = row[1]
        weighted_avg = (midterm_score*weight[0]) + (final_score*weight[1])
        average.append(weighted_avg)
    return average

def analyze_data(data_1d):
    # TODO) Derive summary of the given `data_1d`
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    # mean: 데이터의 총합을 항목수로 나눈 값, variance(분산): 데이터가 평균에서 얼마나 떨어져있는가, median: 정렬된 데이터에서의 중간값
    mean = sum(data_1d) / len(data_1d)
    var = sum((x - mean) ** 2 for x in data_1d) / len(data_1d)
    sorted_data = sorted(data_1d)
    n = len(sorted_data)
    if n % 2 == 0:  
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2 # //: 정수나눗셈
    else: 
        median = sorted_data[n // 2]
    return mean, var, median, min(data_1d), max(data_1d)

if __name__ == '__main__':
    
    data = read_data('/Users/master/dev/ososo21101231/practice/python02_lab/data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])

        # Write the analysis report as a markdown file
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Average |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column) # 각각의 column은 중간고사점수리스트, 기말고사점수리스트, 평균점수리스트 
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')