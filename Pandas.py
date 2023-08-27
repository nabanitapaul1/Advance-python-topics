# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 00:15:37 2023

@author: paulna
"""

## Pandas  is used for data analysis, data manipulation, data cleaning.
## Full Form is Pannel Data or Pandas for Data Analysis

## For installing pandas

#pip install pandas

import pandas  as pd
import numpy as np

## Checking version of pandas

print(pd.__version__)

help(pd.Series)
## Data Structrues in pandas
## 1. Series
## 2. Data Frame



## Series
## It like a column from a table. 1-D Array which can hold value of any data types.

## Creating Series

#a) From a list
a_series1 = pd.Series([1,4,6,9,11,23])
print(a_series1)

## Indexing aor Labelling for a particular elements
a_series1[1] # Accesing the 2nd element by index
a_series1[1:5] ## Accessing a range of elements

## Defining custom index

a_series2 = pd.Series([1,4,6,9,11,23],index=["A","B","C","D","E","F"])
print(a_series2)
a_series2["A"]

a_series2["A":"D"]

#b) From a Dictionary 

acal_dict = {"Day1":50,"Day2":100,"Day3":120,"Day4":130,"Day5":180,"Day6":200}
a_series3 = pd.Series(acal_dict)
print(a_series3)

acal_dict1 = {"Day1":50,"Day2":100,"Day3":120,"Day4":130,"Day5":180,"Day6":200}
a_series3 = pd.Series(acal_dict1,index=["Day1","Day3","Day5","Day4"])
print(a_series3)

a_series3["Day1":"Day5"]


## Data Frame  

## Its a table like  2-D strurcture which have rows and columns

## Creating a Data Frame

a_df1 = pd.DataFrame({"Cal":[20,30,40,50],"Duration":[1,2,3,4]})
print(a_df1)
print(a_df1.loc[[1]]) ## return a series

print(a_df1.loc[1:4])
print(a_df1.loc[[1,3]])

type(a_df1.loc[1]) ## return a series
print(a_df1.iloc[1:3])

a_df2 = pd.DataFrame({"Cal":[20,30,40,50],"Duration":[1,2,3,4]},index=["Day1","Day2","Day3","Day4"])
a_df2.loc['Day1']
a_df2.loc[['Day1']]
a_df2.loc[['Day1','Day2']]
a_df2.loc['Day1':'Day4']
a_df2.loc['Day1':'Day4',"Cal"]
a_df2.iloc[0:2,0:2]


## Create a data frame from a random number

dates =pd.date_range("20130101",periods=6)
dates

a_df3 = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
a_df3

a_df4= pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
a_df4

a_df4.info()   ## describe about no. of non-null columns and data types of columns


a_df4.columns ## returns column name
a_df4.index ## returns indices
a_df4.dtypes ## returns data types of columns

a_df4.head(3) ## returns number of 1st top rows
a_df4.tail(2)   ## returns number of last end rows

a_df4.describe() ## 5 number summary


a_df3.to_numpy() ## converting each row to arrays
a_df4.to_numpy()


## Transpose
x =a_df3.T
x
type(x)
x.columns
x.index


## Sort Index
a_df3.sort_index(axis=0, ascending=False)

a_df3.sort_index(axis=1, ascending=False)

## Sort Values

a_df3.sort_values(by='B')


## Selection  



a_df3["A"]
a_df3[0:2]


## Selection by labels or name
## .loc and .at
a_df2.loc[["Day1","Day3"],"Cal"] ## .Loc returns multiple values


a_df2.loc["Day1":"Day3","Cal"] ## .Loc returns multiple values
a_df2.at["Day1","Cal"] ## .at returns single value

## Selection by position or index

## .iloc or .iat

a_df3.iloc[1]
a_df3.iloc[1,2]
a_df3.iloc[[1,2]]
a_df3.iloc[:,1:3]
a_df3.iloc[1,1:3]
a_df3.iloc[[1,3],1:3]
a_df3.iloc[[1,3],[1,3]] ## .iloc  returns multipke values 


a_df3.iat[1,1]  ## .iat returns single value

## Boolean Indexing
a_df3[a_df3["B"]>0]
a_df3[a_df3>0]

a_df3["E"] =["One","Two","One","Three","Four","Two"]
a_df3
a_df3[a_df3["E"].isin(["One","Two"])]


## Missing data

#.dropna()
#.fillna()
#pd.isna()

## Statistical Operations


a_df3.mean() ## Column wise
a_df3.mean(1) ## row wise

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
a_df3.drop(['E'],inplace=True,axis=1)


## Apply is used to apply a user defined function across the data frame either accross columns or rows

a_df3.apply(np.cumsum)
a_df3.apply(np.cumsum,axis=1)
a_df3.apply(np.cumsum,axis=0)
a_df3["E"] =a_df3.apply(lambda x : x.max()-x.min(),axis=1)
a_df3


## Histograming

a_series =pd.Series(np.random.randint(1,6,size=8))
a_series

a_series.value_counts()

# String Methods

a_series2 =pd.Series(["Aman","Rajesh","Kuber","Raynold"])
a_series2
a_series2.str.lower()
a_series2.str.upper()



## Combining data frames


# 1. Concat 
## It can combine two or more dataframes row wise or columns wise.


df1 = pd.DataFrame({"key1" :[1,2,3,4,5,6], 
                    "Feature1": ["A1","B1","C1","D1","E1","F1"], 
                    "Feature2":["X1","X2","X3","X4","X5","X6"]})
df1

df2 = pd.DataFrame({"key1" :[1,2,3,4,5,6,7], 
                    "Feature1": ["A1","B1","C1","D1","E1","F1","G1"], 
                    "Feature2":["X1","X2","X3","X4","X5","X6","X7"]})


df2
df3 = pd.DataFrame({"key3" :[7,8,9,10,11,12], 
                    "Feature1": ["A1","B1","C1","D1","E1","F1"], 
                    "Feature2":["X1","X2","X3","X4","X5","X6"],
                    "Feature3":["Y1","Y2","Y3","Y4","Y5","Y6"]})



pd.concat([df1,df2])
df1.append(df2)

pd.concat([df1,df2,df3])



pd.concat([df1,df2],axis=1)

x=pd.concat([df1,df2,df3],axis=1)



## 2. Merge 

## it can combine dataframes beased on common column --- Inner Join,Outer Join,Left Join, Right Join


pd.merge(df1,df2)

pd.merge(df1,df2,on="key1", how ="inner")

pd.merge(df1,df2,how="inner")



pd.merge(df1,df2,on="key1", how ="left",indicator=True)

pd.merge(df1,df2,how="left")

pd.merge(df1,df2,on="key1", how ="right",indicator=True)

pd.merge(df1,df2,how="right")


pd.merge(df1,df2,on="key1", how ="outer",indicator=True)

pd.merge(df1,df2,how="outer")


## Join 
## join dataframes based on indices

df1.merge(df2,on="key1", how ="inner")
df1.merge(df2,on="key1", how ="left")





pd.merge(df1,df2,how="inner")