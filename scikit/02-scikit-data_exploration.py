from sklearn import datasets
diabetes = datasets.load_diabetes()
print(diabetes.data.shape, diabetes.target.shape)

print(diabetes.target[:10])
print(diabetes.target[:10])