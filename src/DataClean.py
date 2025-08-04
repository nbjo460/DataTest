import string

import pandas as pd
from pandas import DataFrame


class DataClean:

    def __init__(self, df : DataFrame):
        self.table = df

    def clean(self):
        for col in self.table:
            self.remove_punctuation(col)
            self.lower(col)
        self.delete_na_biased()
        return self.table


    def remove_punctuation(self, column_name : str):
        punc = r'[{}]'.format(string.punctuation)
        table = self.table
        for char in punc:
            try:
                table[column_name] = table[column_name].astype(str).str.replace(char, '')  # remove numbers
            except:
                print(column_name)

    def lower(self, column_name : str):
        table = self.table
        try:
            table[column_name] = table[column_name].astype(str).str.lower()  # remove numbers
        except:
            pass

    def delete_na_biased(self):
        self.table = self.table[~self.table["Biased"].isna()]