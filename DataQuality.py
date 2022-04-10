import pandas as pd


path = r'tablelocation'

target_df = pd.read_csv(path)


class DataQuality(pd.DataFrame):

    def __init__(self, df_Dataquality):
        self.target_df = df_Dataquality


    def perform_DQ_Chk(self):
        target_df = self.target_df
        for column in target_df:
            columnSeriesObj = target_df[column]
            print('Column Name : ', column)
            print('Column Unique Contents : ', target_df[column].unique())
            print('Column Unique Contents Value : ', target_df[column].value_counts())


DataQuality(target_df).perform_DQ_Chk
