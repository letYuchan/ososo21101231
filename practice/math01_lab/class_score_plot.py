import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('/Users/master/dev/letYuchan.github.io/24Second-2_workspace/2학년_2학기/ososo21101231/practice/math01_lab/data/class_score_kr.csv')
    class_en = read_data('/Users/master/dev/letYuchan.github.io/24Second-2_workspace/2학년_2학기/ososo21101231/practice/math01_lab/data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en= zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]
    

    # TODO) Plot midterm/final scores as points
    plt.figure(figsize=(10, 5))
    plt.scatter(midterm_kr, final_kr, color='red', label='Korean')
    plt.scatter(midterm_en, final_en, color='blue', marker='+', label='English')
    plt.title('Midterm and Final Scores')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.grid(True)
    plt.legend()
    plt.savefig('/Users/master/dev/letYuchan.github.io/24Second-2_workspace/2학년_2학기/ososo21101231/exercise/class_score_scatter.png')
    plt.show()

    # TODO) Plot total scores as a histogram
    plt.figure(figsize=(10, 5))
    plt.hist(total_kr, bins=range(0, 101, 5), alpha=0.5, color='red', label='Korean', edgecolor='black')
    plt.hist(total_en, bins=range(0, 101, 5), alpha=0.5, color='blue', label='English', edgecolor='black')
    plt.xlim(0, 100)
    plt.title('Total Scores Histogram')
    plt.xlabel('Total Score')
    plt.ylabel('The number of students')
    plt.legend(loc='upper left')
    plt.savefig('/Users/master/dev/letYuchan.github.io/24Second-2_workspace/2학년_2학기/ososo21101231/exercise/class_score_hist.png')
    plt.show()
