from sklearn import tree

# training features: [height, weight, shoe size]
X = [
    [177,90,44],
    [154,85,42],
    [163,79,39],
    [155,88,41],
    [178,87,44],
    [182,93,38],
    [186,99,40],
    [179,75,43],
    [147,90,38],
    [151,69,44],
]

# Target prediction
y = ['male','female','female','male','male', 
'female','male','female','male','male']

classifier = tree.DecisionTreeClassifier()

# Capture patterns in the training data (X, y)
classifier = classifier.fit(X, y)

# Data to predict its gender
newData = [181,90,41]

prediction = classifier.predict([newData])

print(prediction)
