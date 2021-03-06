import numpy as np
def extract(lst):
    return list(next(zip(*lst)))
def avg_nested_lists(nested_vals):
    """
    Averages a 2-D array and returns a 1-D array of all of the columns
    averaged together, regardless of their dimensions.
    """
    output = []
    maximum = 0
    for lst in nested_vals:
        if len(lst) > maximum:
            maximum = len(lst)
    for index in range(maximum): # Go through each index of longest list
        temp = []
        for lst in nested_vals: # Go through each list
            if index < len(lst): # If not an index error
                temp.append(lst[index])
        output.append(np.nanmean(temp))
    return output

import pandas as pd

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