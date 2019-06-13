
def get_nutrient_data(df, item):
    return df.loc[df['Shrt_Desc'] == item]

#df_broccoli = get_nutrient_data(food_df, "BROCCOLI,RAW")
#df_blueberries = get_nutrient_data(food_df, "BLUEBERRIES,RAW")
#df_walnuts = get_nutrient_data(food_df, "WALNUTS,ENGLISH")
#print(df_broccoli)

def convert_units(given_unit: str) -> int:
    """

    :param given_unit:
    :return: 10^x from base.
    """
    # print(given_unit)
    given_unit = given_unit.replace("μ", "MICRO")
    given_unit = given_unit.replace("µ", "MICRO") #DIFF!
    # assert given_unit[-1] == "g"

    prefix = {"M": 6, "k": 3, "h": 2, "d": -1, "c": -2, "m": -3, "MICRO": -6, "n": -9, "p": -12, "f": -15, "a": -18, "z": -21, "y": -24}
    # print("given unit: {}".format(given_unit))

    if given_unit == "g":
        return 0

    return prefix[given_unit[:-1]]


def get_in_gram(given_unit: str, value: float) -> float:
    return pow(10, convert_units(given_unit)) * value

#print(food_df.columns)
