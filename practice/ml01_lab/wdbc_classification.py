import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib.lines import Line2D

# 데이터셋을 로드하는 함수
def load_wdbc_data(filename):
    class WDBCData:
        data = []
        target = []
        target_names = ['malignant', 'benign']
        feature_names = [
            'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
            'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry',
            'mean fractal dimension', 'radius error', 'texture error', 'perimeter error',
            'area error', 'smoothness error', 'compactness error', 'concavity error',
            'concave points error', 'symmetry error', 'fractal dimension error', 'worst radius',
            'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
            'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry',
            'worst fractal dimension'
        ]

    wdbc = WDBCData()
    with open(filename) as f:
        for line in f.readlines():
            items = line.strip().split(',')
            wdbc.target.append(0 if items[1] == 'M' else 1)  # 악성은 0, 양성은 1
            wdbc.data.append([float(x) for x in items[2:]])

        wdbc.data = np.array(wdbc.data)
        wdbc.target = np.array(wdbc.target)
    return wdbc

if __name__ == '__main__':
    # 데이터셋 로드
    wdbc = load_wdbc_data('/Users/master/dev/letYuchan.github.io/24Second-2_workspace/2학년_2학기/ososo21101231/practice/ml01_lab/data/wdbc.data')

    # 모델 훈련 (SVM에서 RandomForestClassifier로 변경하여 성능 향상 기대)
    model = RandomForestClassifier(random_state=42)
    model.fit(wdbc.data, wdbc.target)

    # 모델 예측 및 정확도 측정
    predict = model.predict(wdbc.data)
    accuracy = metrics.balanced_accuracy_score(wdbc.target, predict)
    print(f'Balanced Accuracy: {accuracy:.3f}')

    # 혼동 행렬 시각화
    cm = confusion_matrix(wdbc.target, predict, labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wdbc.target_names)
    disp.plot(cmap='Blues')
    plt.title("Confusion Matrix")
    plt.savefig("wdbc_classification_matrix.png")  # 혼동 행렬 저장
    plt.show()

    # 첫 번째 산점도만 출력
    cmap = np.array([(1, 0, 0), (0, 1, 0)])  # 색상 설정 (빨강: 악성, 초록: 양성)
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    
    # 첫 번째 속성 쌍 (0, 1)에 대한 산점도 작성
    plt.figure()
    plt.title(f'My Classifier (Accuracy: {accuracy:.3f})')
    plt.scatter(wdbc.data[:, 0], wdbc.data[:, 1], c=cmap[wdbc.target], edgecolors=cmap[predict])
    plt.xlabel(wdbc.feature_names[0])
    plt.ylabel(wdbc.feature_names[1])
    plt.legend(handles=clabel, framealpha=0.5)
    plt.savefig("wdbc_classification_scatter_0_1.png")  # 첫 번째 산점도 저장
    plt.show()
