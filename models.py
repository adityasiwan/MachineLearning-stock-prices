from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

class PriceModel(object):
    """Linear Regression Model used to predict future prices"""
    def __init__(self, algorithm='gnb'):
        self.algorithm = algorithm

        if algorithm == 'svm':
            self.clf = SVC(kernel='rbf')
        elif algorithm == 'rf':
            self.clf = RandomForestClassifier(n_estimators=10,
                                                max_depth=None,
                                                min_samples_split=1,
                                                random_state=0)
        elif algorithm == 'lr':
            self.clf = LogisticRegression()
        elif algorithm == 'knn':
            self.clf = KNeighborsClassifier(n_neighbors=3)
        else:
            # Naive Bayes
            self.clf = GaussianNB()

    def train(self, X_train, y_train):
        self.clf.fit(X_train, y_train)

    def predict(self, x):
        return self.clf.predict(x)

    def score(self, X_test, y_test):
        return self.clf.score(X_test, y_test)
