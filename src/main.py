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
    df = tmp.analyze()
    df.to_json("../results/results.json")



df = pd.read_csv("../data/tweets_dataset.csv")
clean(df)
analyze(df)
print(df["Biased"].isna().sum())
