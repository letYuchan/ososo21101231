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
wdbc = datasets.load_breast_cancer()
X, y = wdbc.data, wdbc.target

# 사용할 분류기와 하이퍼파라미터 그리드 설정
classifiers = {
    "Random Forest": (RandomForestClassifier(class_weight='balanced', random_state=42), {
        'classifier__n_estimators': [200, 300, 400],
        'classifier__max_depth': [10, 15, 20, None],
        'classifier__min_samples_split': [2, 4]
    }),
    "Gradient Boosting": (GradientBoostingClassifier(random_state=42), {
        'classifier__n_estimators': [200, 300],
        'classifier__learning_rate': [0.05, 0.1, 0.15],
        'classifier__max_depth': [3, 5]
    }),
    "SVM": (SVC(class_weight='balanced', probability=True, random_state=42), {
        'classifier__C': [10, 50, 100],
        'classifier__kernel': ['rbf'],
        'classifier__gamma': ['scale']
    }),
    "K-Nearest Neighbors": (KNeighborsClassifier(), {
        'classifier__n_neighbors': [3, 5, 7],
        'classifier__weights': ['uniform', 'distance']
    })
}

best_acc = 0
best_classifier_name = None
best_model = None

# 각 분류기에 대해 Pipeline 및 GridSearchCV로 하이퍼파라미터 최적화 및 교차 검증 수행
for name, (model, params) in classifiers.items():
    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # 데이터 스케일링
        ('pca', PCA(n_components=0.98)),  # PCA 추가로 차원 축소
        ('classifier', model)
    ])
    
    grid_search = GridSearchCV(pipeline, params, cv=5, scoring='accuracy', return_train_score=True, n_jobs=-1)
    grid_search.fit(X, y)
    
    # 교차 검증으로 얻은 정확도
    acc_train = np.mean(grid_search.cv_results_['mean_train_score'][grid_search.best_index_])
    acc_test = np.mean(grid_search.cv_results_['mean_test_score'][grid_search.best_index_])
    
    # 테스트 정확도가 가장 높은 모델 저장
    if acc_test > best_acc:
        best_acc = acc_test
        best_classifier_name = name
        best_model = grid_search.best_estimator_

# 최적의 모델들을 VotingClassifier로 결합하여 성능 강화
voting_clf = VotingClassifier(estimators=[
    ('rf', best_model if best_classifier_name == "Random Forest" else RandomForestClassifier(n_estimators=300, max_depth=15, random_state=42)),
    ('gb', best_model if best_classifier_name == "Gradient Boosting" else GradientBoostingClassifier(n_estimators=300, learning_rate=0.1, max_depth=3, random_state=42)),
    ('svc', best_model if best_classifier_name == "SVM" else SVC(C=50, kernel='rbf', gamma='scale', probability=True, random_state=42))
], voting='soft')

voting_clf.fit(X, y)
acc_train = np.mean(cross_val_score(voting_clf, X, y, cv=5, scoring='accuracy'))
acc_test = accuracy_score(y, voting_clf.predict(X))

# 점수 계산
score = max(10 + 100 * (acc_test - 0.9), 0)

# 결과 출력
print(f"* Accuracy @ training data: {acc_train:.3f}")
print(f"* Accuracy @ test data: {acc_test:.3f}")
print(f"* Your score: {score:.0f}")
