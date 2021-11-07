import pandas as pd

def load_adult_data():
    data = pd.read_csv(
        'data/adult.data',
        names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital status",
        "occupation", "relationship", "race", "sex", "capital gain", "capital loss",
        "hours per week", "country", "target"]
    )
    test = pd.read_csv(
        "data/adult.test", 
        names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital status",
        "occupation", "relationship", "race", "sex", "capital gain", "capital loss",
        "hours per week", "country", "target"]
    )
    data = data.dropna()
    data = pd.get_dummies(data)
    data['target'] = data['target_ >50K']
    del data["target_ <=50K"]
    del data["target_ >50K"]
    return data

def load_wine_data():
    columns = ["Class", "alcohol", "malic acid", "ash", "alcalinity of ash", "magnesium", "total phenols", "flavanoids", "nonflavanoid phenols", "proanthocyanins", "color intensity", "hue", "OD280/OD315 of diluted wines", "proline"]
    data = pd.read_csv("data/wine.data", names=columns)
    data.columns = columns
    return data

def load_cancer_data():
    columns = ["id", "diagnosis", "radius mean", "texture mean", "perimeter mean", "area mean", "smoothness mean", "compactness mean", "concavity mean", "concave points mean", "symmetry mean", "fractal dimension mean", "radius se", "texture se", "perimeter se", "area se", "smoothness se", "compactness se", "concavity se", "concave points se", "symmetry se", "fractal dimension se", "radius worst", "texture worst", "perimeter worst", "area worst", "smoothness worst", "compactness worst", "concavity worst", "concave points worst", "symmetry worst", "fractal dimension worst"]
    data = pd.read_csv("data/wdbc.data", names=columns)
    data.columns = columns
    data = pd.get_dummies(data)
    data['target'] = data['diagnosis_M']
    del data['id']
    del data['diagnosis_M']
    del data['diagnosis_B']
    return data