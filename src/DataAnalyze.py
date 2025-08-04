import pandas as pd

class DataAnalyze:
    def __init__(self, df):
        self.table = df
        self.result = {}

    def analyze(self):
        self.result["category"] = self.count_per_category("Biased")
        return self.result

    def count_per_category(self, column_name):
        uniques_list = self.table[column_name].unique()
        twits_per_unique = {}
        for unique in uniques_list:
            twits_per_unique[unique] = self.table[self.table[column_name] == unique].shape[0]
        return twits_per_unique

