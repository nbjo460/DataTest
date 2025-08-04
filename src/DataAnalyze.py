import pandas as pd

class DataAnalyze:
    def __init__(self, df):
        self.table = df

    def analyze(self):
        self.count_per_category()
        return self.table

    def count_per_category(self):
        pass