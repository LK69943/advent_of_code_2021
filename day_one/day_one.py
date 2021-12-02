import os
import pandas as pd


# Day One: Sonar Sweep
# Part One
sonar_depths = pd.read_csv(os.path.join(os.getcwd(), 'sonar_depths.csv'), header=None, names=['sonar_depth'])

sonar_depths['pct_change'] = sonar_depths.pct_change()
direction_cnt = (sonar_depths['pct_change'] > 0).value_counts()

print(f'Answer is {direction_cnt.loc[True]}')  # Answer is 1711


# Part Two
sonar_depths['sliding_window'] = sonar_depths['sonar_depth'].rolling(3).sum()
sonar_depths['sliding_window_pct_change'] = sonar_depths['sliding_window'].pct_change()
sliding_window_direction_cnt = (sonar_depths['sliding_window_pct_change'] > 0).value_counts()

print(f'Answer is {sliding_window_direction_cnt.loc[True]}')  # Answer is 1743
