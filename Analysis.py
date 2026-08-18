import pandas as pd
df=pd.read_csv(r"C:\Users\hp\Desktop\Mohit Sahdev - Data Scientist\bank-marketing-analysis\Data\bank-direct-marketing-campaigns.csv")

# ============================================================
# BASIC UNDERSTANDING
# ============================================================
#print(df.head()) #data header
#print(df.shape) #how many rows and columns
#print(df.columns) #name of columns
#print(df.info) #data type and missing values
#print(df.describe) #numberical data in statistics
#print(df.tail())
#print(df.sample(5))


# ============================================================
# DATA QUALITY
# ============================================================
#print(df.isnull().sum()) #check missing values
#print(df.dtypes) #check datatypes
#print(df.duplicated().sum()) # check duplicate row
# print(df.nunique()) #check unique values - gives number(numberic)
#print(df["job"].unique()) #gives actual values in it


# ============================================================
# UNIQUE VALUES & VALUE COUNTS
# ============================================================

# print(df["job"].unique())
# print(df["job"].value_counts())

# print(df["age"].unique())
# print(df["age"].value_counts())

# print(df["marital"].unique())
# print(df["marital"].value_counts())

# print(df["education"].unique())
# print(df["education"].value_counts())

# print(df["default"].unique())
# print(df["default"].value_counts())

# print(df["housing"].unique())
# print(df["housing"].value_counts())

# print(df["loan"].unique())
# print(df["loan"].value_counts())

# print(df["contact"].unique())
# print(df["contact"].value_counts())

# print(df["month"].unique())
# print(df["month"].value_counts())

# print(df["poutcome"].unique())
# print(df["poutcome"].value_counts())

# print(df["y"].unique())
# print(df["y"].value_counts())

#======FOR PERCENTAGE======
# df["y"].value_counts(normalize=True) * 100

# ============================================================
# NUMERICAL RANGE CHECK
# ============================================================

# print(df["age"].min())
# print(df["age"].max())


# ============================================================
# COMPARE COLUMNS
# ============================================================

print(pd.crosstab(df["job"], df["y"]))

#print(
    pd.crosstab(
        df["job"],
        df["y"],
        normalize="index"
    ) * 100
)


# ============================================================
# CHECK ALL COLUMNS
# ============================================================

#for col in df.columns:
    print("\nCOLUMN:", col)
    print(df[col].unique())

#=============================================================
#Deep Dive
#=============================================================
# Basic
print(df["age"].describe())

# Range
print(df["age"].min())
print(df["age"].max())

# Different ages
print(df["age"].nunique())

# Most common ages
print(df["age"].value_counts().head(10))

# Average age
print(df["age"].mean())

# Median age
print(df["age"].median())

# Age vs target
print(df.groupby("y")["age"].mean())

# Age range by target
print(df.groupby("y")["age"].agg(["min", "mean", "median", "max"]))

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 20, 30, 40, 50, 60, 100]
)

print(df["age_group"].value_counts().sort_index())

#then
print(
    pd.crosstab(
        df["age_group"],
        df["y"],
        normalize="index"
    ) * 100
)