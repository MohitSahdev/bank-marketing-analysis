import pandas as pd
df=pd.read_csv(r"C:\Users\hp\Desktop\Mohit Sahdev - Data Scientist\bank-marketing-analysis\Data\bank-direct-marketing-campaigns.csv")
#basic understanding
#print(df.head()) #data header
#print(df.shape) #how many rows and columns
#print(df.columns) #name of columns
#print(df.info) #data type and missing values
#print(df.describe) #numberical data in statistics

#data quality
#print(df.isnull().sum()) #check missing values
#print(df.duplicated().sum()) # check duplicate row
#print(df.nunique()) #check unique values
#checking value count of individually columns
print(df["job"].value_counts())
print(df["age"].value_counts())
print(df["marital"].value_counts())
print(df["education"].value_counts())
print(df["default"].value_counts())
print(df["housing"].value_counts())
print(df["loan"].value_counts())
print(df["contact"].value_counts())
print(df["month"].value_counts())
print(df["poutcome"].value_counts())
print(df["y"].value_counts())