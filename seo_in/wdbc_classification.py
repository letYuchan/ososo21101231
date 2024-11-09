import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib.lines import Line2D

# WDBC 데이터셋을 로드하는 함수
def load_wdbc_data(file_path):
    class WDBCData:
        features = []  # 데이터셋의 속성들 (569, 30 형태로 저장될 예정)
        labels = []  # 데이터셋의 타겟 레이블 (569, )
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
    with open(file_path) as file:
        for line in file.readlines():
            items = line.strip().split(',')
            wdbc.labels.append(0 if items[1] == 'M' else 1)  # 악성은 0, 양성은 1
            wdbc.features.append([float(x) for x in items[2:]])

        wdbc.features = np.array(wdbc.features)
        wdbc.labels = np.array(wdbc.labels)
    return wdbc

if __name__ == '__main__':
    # 데이터셋 로드
    wdbc_data = load_wdbc_data('/Users/master/guapa/2학년_2학기/practice/ml01_lab/data/wdbc.data')

    # 모델 훈련 (SVM 대신 RandomForestClassifier를 사용하여 성능 향상)
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(wdbc_data.features, wdbc_data.labels)

    # 모델 예측 및 정확도 측정
    predictions = rf_model.predict(wdbc_data.features)
    balanced_accuracy = metrics.balanced_accuracy_score(wdbc_data.labels, predictions)
    print(f'Balanced Accuracy: {balanced_accuracy:.3f}')

    # 혼동 행렬 시각화
    confusion_mat = confusion_matrix(wdbc_data.labels, predictions, labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=confusion_mat, display_labels=wdbc_data.target_names)
    disp.plot(cmap='Blues')
    plt.title("Confusion Matrix")
    plt.savefig("wdbc_confusion_matrix.png")  # 혼동 행렬 저장
    plt.show()

    # 첫 번째 산점도만 출력
    color_map = np.array([(1, 0, 0), (0, 1, 0)])  # 색상 설정 (빨강: 악성, 초록: 양성)
    legend_labels = [Line2D([0], [0], marker='o', lw=0, label=wdbc_data.target_names[i], color=color_map[i]) for i in range(len(color_map))]
    
    # 첫 번째 속성 쌍 (0, 1)에 대한 산점도 작성
    plt.figure()
    plt.title(f'My Classifier (Accuracy: {balanced_accuracy:.3f})')
    plt.scatter(wdbc_data.features[:, 0], wdbc_data.features[:, 1], c=color_map[wdbc_data.labels], edgecolors=color_map[predictions])
    plt.xlabel(wdbc_data.feature_names[0])
    plt.ylabel(wdbc_data.feature_names[1])
    plt.legend(handles=legend_labels, framealpha=0.5)
    plt.savefig("wdbc_scatter_0_1.png")  # 첫 번째 산점도 저장
    plt.show()
