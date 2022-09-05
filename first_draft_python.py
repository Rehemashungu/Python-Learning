#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import glob

path = "path\\to current\\ working\ directory"


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

#subsetting the only the columns interested and saving into a new variable called results
results = merged_df[["Rearrangement","ChrA", "PositionA","PositionB", "ChrB", "GeneID","file"]]
print(results)

#subsetting only the t(8;14) interested
print(chr_8_14)
chr_8_14 = results[results["Rearrangement"] == "t(8;14)"]

#setting the file column as our index
final_data = chr_8_14.set_index("file")
final_data.style #viewing

#splitting the dataframe according to the fileindex
output_data= final_data.groupby("file") 
print(output_data)


MN = output_data.get_group("filename1")
MH =  output_data.get_group("filename2")
LA =  output_data.get_group("filename3")

#exporting the individuals files to excel files
MN.to_excel(r'path to output folder\MN.csv')
MH.to_excel(r"path to output folder\MH.csv")
LA.to_excel(r"path to output folder\LA.csv")




