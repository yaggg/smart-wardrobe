import numpy as np
import pandas as pd

TOPWEARS = ['Shirts', 'Tshirts', 'Sweatshirts', 'Sweaters']
BOTTOMWEARS = ['Jeans', 'Track Pants', 'Shorts']
OUTWEARS = ['Rain Jacket', 'Jackets']
FOOTWEARS = ['Casual Shoes', 'Formal Shoes', 'Sports Shoes', 'Flip Flops', 'Sandals']
ACCESSORIES = ['Sunglasses', 'Scarves', 'Lip Care', 'Gloves', 'Umbrellas']

SEASONS = ['Winter', 'Spring', 'Summer', 'Autumn']
TEMP_RANGES_DICT = {'r1': (-np.inf, -25), 'r2': (-25, -20), 'r3': (-20, -10), 'r4': (-10, -5), 'r5': (-5, 0),
                    'r6': (0, 5),
                    'r7': (5, 10), 'r8': (10, 15), 'r9': (15, 20), 'r10': (20, 25), 'r11': (25, np.inf)}
WEATHER_TYPES = ['sunny', 'cloudy', 'snowy', 'rainy', 'foggy', 'other']

ALL_TYPES = np.array(TOPWEARS + BOTTOMWEARS + OUTWEARS + FOOTWEARS + ACCESSORIES)


ALL_MAPPINGS = np.array([
    [0, 1, 0, 1,    0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,    1, 1, 0, 1, 1, 0],
    [0, 1, 1, 1,    0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,    1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,    0, 1, 1, 1, 1, 0],
    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,    0, 1, 1, 1, 1, 0],

    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,    0, 1, 1, 1, 1, 0],
    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,    0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,    1, 1, 0, 1, 0, 0],

    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,    1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,    1, 1, 1, 0, 1, 0],

    [1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,    1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1,    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,    1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,    1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,    1, 1, 0, 0, 1, 0],

    [0, 1, 1, 1,    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,    1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,    1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0,    1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,    1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1,    1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,    1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,    0, 0, 0, 1, 0, 0]
]).astype(np.float64)

df_values = np.hstack((ALL_TYPES.reshape(19, 1), ALL_MAPPINGS))

COLUMNS = ['ItemType'] + SEASONS + list(TEMP_RANGES_DICT.keys()) + WEATHER_TYPES


def _find_temp_name_for_temp(temp):
    return [temp_name for temp_name, temp_range in TEMP_RANGES_DICT.items() if temp_range[0] <= temp < temp_range[1]][0]


class ClothesMapper:
    def __init__(self):
        self.mapping_df = pd.DataFrame(data=df_values, columns=COLUMNS)

        for column in self.mapping_df.columns[1:]:
            self.mapping_df[column] = pd.to_numeric(self.mapping_df[column])

    def get_item_types_for_weather(self, season, temp, weather_type):
        temp_name = _find_temp_name_for_temp(temp)
        return self.mapping_df[(self.mapping_df[season] == 1.0) & (self.mapping_df[temp_name] == 1.0) &
                               (self.mapping_df[weather_type] == 1.0)]['ItemType']



