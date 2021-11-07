import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# This function copied from https://github.com/wesley-smith/CS7641-assignment-1/blob/master/helpers.py
def scikit_cv_result_to_df(cv_res, drop_splits=True):
    """Convert a GridSearchCV.cv_result_ dictionary to a dataframe indexed by hyperparameter
    :param cv_res: cv_result_ object (attribute of a GridSearchCV/RandomizedSearchCV instance)
    :type cv_res: dict
    :param drop_splits: whether to drop columns with individual cross-validation scores (default: True)
    :type drop_splits: bool
    :return: DataFrame with a MultiIndex corresponding to each parameter
    :rtype: pd.DataFrame
    """
    params = [k for k in cv_res.keys() if k.startswith('param_')]
    params_to_shorthand = { # Mapping type to remove the 'param_' prefix
        p : p[6:] for p in params
    }
    cv_res_df = pd.DataFrame(cv_res, columns=[k for k in cv_res.keys() if k != 'params'])
    cv_res_df = cv_res_df.rename(index=str, columns=params_to_shorthand)
    cv_res_df = cv_res_df.set_index(list(params_to_shorthand.values()))
    if drop_splits:
        cv_res_df = cv_res_df.drop(axis=1, labels=[c for c in cv_res_df.columns if c.startswith('split')])
    return cv_res_df

def get_useful_cv_columns():
    return ['mean_fit_time', 'mean_score_time', 'mean_test_score', 'mean_train_score']

def center(X):
    X = np.array(X)
    mean = X.mean(axis=1, keepdims=True)
    return X - mean

def whiten(X):
    cov = np.cov(X)
    d, E = np.linalg.eigh(cov)
    D = np.diag(d)
    D_inv = np.sqrt(np.linalg.inv(D))
    X_whiten = np.dot(E, np.dot(D_inv, np.dot(E.T, X)))
    return X_whiten

def add_cluster_label(clusterer, dr, X):
    dr_Xt = dr.fit_transform(X)
    clusterer.fit(dr_Xt)
    y_km = clusterer.predict(dr_Xt)
    new_array = np.zeros((dr_Xt.shape[0], dr_Xt.shape[1]+1))
    for i, row in enumerate(dr_Xt):
        new_array[i] = np.append(row, y_km[i])
    return new_array

