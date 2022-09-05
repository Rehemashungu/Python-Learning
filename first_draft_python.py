#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import glob

path = "C:\\Users\\jhokororo\\Desktop\\Python Script\\ig caller\\"


all_files = glob.glob("*.csv")
print(all_files)

filenames = glob.glob(path + "\*.csv")
print(filenames)


all_df = []
for f in filenames:
    d_f = pd.read_csv(f, sep =",")
    d_f['file'] = f.split('/')[-1]
    all_df.append(d_f)

merged_df = pd.concat(all_df, ignore_index=True, sort=True)
print(merged_df)   

results = merged_df[["Rearrangement","ChrA", "PositionA","PositionB", "ChrB", "GeneID","file"]] #subsetting the only the columns interested and saving into a new variable called results
print(results)

chr_8_14 = results[results["Rearrangement"] == "t(8;14)"] #subsetting only the t(8;14) interested
print(chr_8_14)


final_data = chr_8_14.set_index("file") #setting the file column as our index
final_data.style #viewing

output_data= final_data.groupby("file") #splitting the dataframe according to the file index
print(output_data)


MNH085 = output_data.get_group("C:\\Users\\jhokororo\\Desktop\\Python Script\\ig caller\\MNH085.csv")
MNH081 =  output_data.get_group("C:\\Users\\jhokororo\\Desktop\\Python Script\\ig caller\\MNH081.csv")
LACOR050 =  output_data.get_group("C:\\Users\\jhokororo\\Desktop\\Python Script\\ig caller\\LACOR050.csv")

#exporting the individuals files to excel files
MNH085.to_excel(r'C:\Users\jhokororo\Desktop\Python Script\ig caller\Output\MNH085.xlsx')
MNH081.to_excel(r'C:\Users\jhokororo\Desktop\Python Script\ig caller\Output\MNH081.xlsx')
LACOR050.to_excel(r'C:\Users\jhokororo\Desktop\Python Script\ig caller\Output\LACOR050.xlsx')




