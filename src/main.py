import json

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

import DataClean
import DataAnalyze

def clean(df : DataFrame):
     cleaner_class = DataClean.DataClean(df)
     cleaned_table = cleaner_class.clean()
     cleaned_table.to_csv("../results/tweets_dataset_cleaned.csv")

def analyze(df : DataFrame):
    tmp = DataAnalyze.DataAnalyze(df)
    js = tmp.analyze()
    with open("../results/results.json", "w") as file:
        json.dump(js, file, indent=4)

if __name__ == "__main__":
    df = pd.read_csv("../data/tweets_dataset.csv")
    clean(df)
    analyze(df)
