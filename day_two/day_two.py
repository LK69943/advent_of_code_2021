import os
import pandas as pd


# Day Two: Dive!
# Part One
position_data = pd.read_csv(os.path.join(os.getcwd(), 'position_data.csv'), header=None, names=['position'])
position_data['direction'] = position_data.apply(lambda x: x.position.split()[0], axis=1)
position_data['units'] = pd.to_numeric(position_data.apply(lambda x: x.position.split()[1], axis=1))

course_data = position_data[['direction', 'units']].groupby(['direction']).sum()

final_depth = course_data.loc['down', 'units'] - course_data.loc['up', 'units']
final_horizontal = course_data.loc['forward', 'units']

print(f'Answer is {final_depth * final_horizontal}')  # Answer is 1427868


# Part Two
aim = 0
horizontal_position = 0
depth = 0

for row in range(position_data.shape[0]):
    if position_data.loc[row, 'direction'] == 'forward':
        horizontal_position += position_data.loc[row, 'units']
        depth += (aim * position_data.loc[row, 'units'])
    elif position_data.loc[row, 'direction'] == 'down':
        aim += position_data.loc[row, 'units']
    elif position_data.loc[row, 'direction'] == 'up':
        aim -= position_data.loc[row, 'units']
    else:
        raise ValueError('Invalid direction.')

print(f'Answer is {depth * horizontal_position}')  # Answer is 1568138742
