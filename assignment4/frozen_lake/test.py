import pandas as pd

vi_data = pd.read_csv('output/report/VI/frozen_lake_no_reward_0.8.csv')
print(vi_data)
print(vi_data['time'].sum())

pi_data = pd.read_csv('output/report/PI/frozen_lake_no_reward_0.9.csv')
print(pi_data)
print(pi_data['time'].sum())

ql_data = pd.read_csv('output/report/Q/frozen_lake_no_reward_0.5_random_0.3_0.0001_0.95.csv')
print(ql_data)
print(ql_data['time'].sum())



