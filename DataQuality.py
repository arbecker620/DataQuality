import pandas as pd
import dataprofiler as dp
import numpy as np


data = {
    "calories": [420,380, 390,390, 80, 350],
    "duration": [50,45,40,40,np.nan ,50]
}


target_df = pd.DataFrame(data)

profile = dp.Profiler(target_df)


report = profile.report(report_options={"output_format":"pretty"})


data_stats = report["data_stats"]

print(data_stats)

column_list_df = []

ext_data = []

for n in data_stats:
    column_list = list(n.keys())
    for col_name in column_list:
        if col_name not in column_list_df:
            column_list_df.append(col_name)
        else:
            continue
    ext_data.append(list(n.values()))
data = pd.DataFrame(ext_data,columns=column_list_df)
stats_df=pd.DataFrame.from_records(data.statistics.dropna().tolist())


sum_df = pd.concat([data, stats_df], axis=1)





data_stats = report["global_stats"]


print(data_stats)
print(sum_df)

