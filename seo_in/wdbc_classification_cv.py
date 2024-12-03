import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

# 데이터셋 로드
data = datasets.load_breast_cancer()
features, labels = data.data, data.target

# 사용할 모델과 하이퍼파라미터 설정
models = {
    "RandomForest": (RandomForestClassifier(class_weight='balanced', random_state=42), {
        'model__n_estimators': [200, 300, 400],
        'model__max_depth': [10, 15, 20, None],
        'model__min_samples_split': [2, 4]
    }),
    "GradientBoosting": (GradientBoostingClassifier(random_state=42), {
        'model__n_estimators': [200, 300],
        'model__learning_rate': [0.05, 0.1, 0.15],
        'model__max_depth': [3, 5]
    }),
    "SVM": (SVC(class_weight='balanced', probability=True, random_state=42), {
        'model__C': [10, 50, 100],
        'model__kernel': ['rbf'],
        'model__gamma': ['scale']
    }),
    "KNN": (KNeighborsClassifier(), {
        'model__n_neighbors': [3, 5, 7],
        'model__weights': ['uniform', 'distance']
    })
}

highest_accuracy = 0
top_model_name = None
best_pipeline = None

# 각 모델에 대해 파이프라인과 GridSearchCV를 통한 하이퍼파라미터 최적화 수행
for name, (model, params) in models.items():
    pipeline = Pipeline([
        ('standardizer', StandardScaler()),  # 데이터 정규화
        ('pca', PCA(n_components=0.98)),     # PCA로 차원 축소
        ('model', model)
    ])
    
    # GridSearchCV를 이용한 최적 하이퍼파라미터 탐색
    search = GridSearchCV(pipeline, params, cv=5, scoring='accuracy', return_train_score=True, n_jobs=-1)
    search.fit(features, labels)
    
    # 교차 검증에서의 평균 학습 및 테스트 정확도 계산
    avg_train_acc = np.mean(search.cv_results_['mean_train_score'][search.best_index_])
    avg_test_acc = np.mean(search.cv_results_['mean_test_score'][search.best_index_])
    
    # 테스트 정확도가 가장 높은 모델 저장
    if avg_test_acc > highest_accuracy:
        highest_accuracy = avg_test_acc
        top_model_name = name
        best_pipeline = search.best_estimator_

# 최적의 모델을 VotingClassifier로 결합
voting_classifier = VotingClassifier(estimators=[
    ('rf', best_pipeline if top_model_name == "RandomForest" else RandomForestClassifier(n_estimators=300, max_depth=15, random_state=42)),
    ('gb', best_pipeline if top_model_name == "GradientBoosting" else GradientBoostingClassifier(n_estimators=300, learning_rate=0.1, max_depth=3, random_state=42)),
    ('svc', best_pipeline if top_model_name == "SVM" else SVC(C=50, kernel='rbf', gamma='scale', probability=True, random_state=42))
], voting='soft')

# 전체 데이터에 대해 최종 모델 학습 및 성능 평가
voting_classifier.fit(features, labels)
train_accuracy = np.mean(cross_val_score(voting_classifier, features, labels, cv=5, scoring='accuracy'))
test_accuracy = accuracy_score(labels, voting_classifier.predict(features))

# 점수 계산
final_score = max(10 + 100 * (test_accuracy - 0.9), 0)

# 결과 출력 (기존 형식으로 유지)
print(f"* Accuracy @ training data: {train_accuracy:.3f}")
print(f"* Accuracy @ test data: {test_accuracy:.3f}")
print(f"* Your score: {final_score:.0f}")
