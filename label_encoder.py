import pandas as pd
from sklearn.preprocessing import LabelEncoder , OneHotEncoder


data = pd.read_csv("Gender_geography.csv")
print(data.head(10))

Le = LabelEncoder()
data["Gender"]  = Le.fit_transform(data["Gender"])
data["Geography"] = Le.fit_transform(data["Geography"])
print(data.head(10))

ohe = OneHotEncoder(categorical_features=[0,1])
data = ohe.fit_transform(data).toarray()
print(data)