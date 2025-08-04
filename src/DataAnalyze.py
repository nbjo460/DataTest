import pandas as pd
from pandas.plotting import table


class DataAnalyze:
    def __init__(self, df):
        self.table = df
        self.result = {}

    def analyze(self):
        self.create_len_in_table()
        longset_series = self.convert_table_to_long_series()
        self.result["category"] = self.count_per_category("Biased")
        self.result["average_len"] = self.average_len_per_category("Biased")
        self.result["longest"] = self.three_longest_twits("Biased")
        self.result["commons"] = self.ten_commons_words(longset_series)

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

    def three_longest_twits(self, column_name):
        longest = {}
        for k in self.result["category"]:
            if k == "sum": continue
            sorted = self.table[self.table[column_name] == k].sort_values(by="length", ascending=False)
            longest[k] = sorted["Text"].head(3).to_list()
        return longest

    def convert_table_to_long_series(self):
        splitted = self.table.Text.str.split(" ", expand=True)
        series = splitted[0]
        series.dropna()
        for i in range(splitted.shape[1]):
            if i == 0: continue
            tmp = splitted[i]
            tmp = tmp.dropna()
            series = series._append(tmp)
        series.reset_index(inplace=True, drop=True)
        return series

    def ten_commons_words(self, _longest_series):
        grouped = _longest_series.value_counts()
        grouped = grouped.sort_values(ascending = False)
        grouped = grouped.head(10).to_dict()
        return grouped
