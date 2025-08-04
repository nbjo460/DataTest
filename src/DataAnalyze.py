import pandas as pd

class DataAnalyze:
    def __init__(self, df):
        self.table = df
        self.result = {}

    def analyze(self):
        self.create_len_in_table()
        self.result["category"] = self.count_per_category("Biased")
        self.result["average_len"] = self.average_len_per_category("Biased")

        return self.result

    def count_per_category(self, column_name):
        uniques_list = self.table[column_name].unique()
        twits_per_unique = {}
        sum_twits = 0
        for unique in uniques_list:
            sum_unique = self.table[self.table[column_name] == unique].shape[0]
            twits_per_unique[unique] = sum_unique
            sum_twits += sum_unique
        twits_per_unique["sum"] = sum_twits
        return twits_per_unique

    def create_len_in_table(self):
        self.table["length"] = self.table["Text"].str.len()

    def average_len_per_category(self, column_name):
        average = {}
        for k in self.result["category"]:
            if k == "sum":
                average[k] = self.table.length.mean()
                continue
            average[k] = self.table[self.table[column_name] == k].length.mean()
        return average
