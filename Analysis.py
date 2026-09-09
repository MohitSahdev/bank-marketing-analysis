import pandas as pd
df=pd.read_csv(r"C:\Users\hp\Desktop\Mohit Sahdev - Data Scientist\bank-marketing-analysis\Data\bank-direct-marketing-campaigns.csv")

def dataset_overview(df, target=None):

    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    # 1. Dataset size
    rows, columns = df.shape
    print(f"\nRows       : {rows:,}")
    print(f"Columns    : {columns}")

    # 2. Column names
    print("\nCOLUMN NAMES")
    print("-" * 60)
    print(df.columns.tolist())

    # 3. Data types
    print("\nDATA TYPES")
    print("-" * 60)
    print(df.dtypes)

    # 4. Numerical columns
    numerical_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    print("\nNUMERICAL COLUMNS")
    print("-" * 60)
    print(numerical_cols)

    # 5. Categorical columns
    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    print("\nCATEGORICAL COLUMNS")
    print("-" * 60)
    print(categorical_cols)

    # 6. Missing / non-null overview
    print("\nDATA COMPLETENESS")
    print("-" * 60)
    print(df.info())

    # 7. Unique values
    print("\nUNIQUE VALUES")
    print("-" * 60)
    print(df.nunique().sort_values())

    # 8. Categorical value overview
    print("\nCATEGORICAL VALUE COUNTS")
    print("-" * 60)

    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts())

    # 9. Target overview
    if target:
        print("\nTARGET VARIABLE")
        print("-" * 60)
        print(f"Target: {target}")
        print(df[target].value_counts())
        print("\nTarget percentage:")
        print(
            df[target]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )


dataset_overview(df, target="y")


def data_quality_check(df):

    print("=" * 60)
    print("DATA QUALITY CHECK")
    print("=" * 60)

    # Missing values
    print("\nMISSING VALUES")
    print("-" * 60)
    print(df.isnull().sum())

    # Duplicate rows
    print("\nDUPLICATE ROWS")
    print("-" * 60)
    print(df.duplicated().sum())

    # Unique values
    print("\nUNIQUE VALUES")
    print("-" * 60)
    print(df.nunique())

    # Numerical summary
    print("\nNUMERICAL SUMMARY")
    print("-" * 60)
    print(df.describe().T)

    # Categorical values
    print("\nCATEGORICAL VALUES")
    print("-" * 60)

    categorical_cols = df.select_dtypes(include="object").columns

    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].unique())


data_quality_check(df)


# checking finding from above code - there are pdays showing 999 days that mean previously the bank staff has contected 999 days ago. now we will go deep into it to know

print(df["pdays"].value_counts().sort_index())
pday_percentage=df["pdays"].value_counts(normalize=True).loc[999]*100
print(pday_percentage)

#Finding more details about pday=999
new_customers = df[df["pdays"] == 999]
new_customers.shape
print(new_customers["y"].value_counts(normalize=True)*100)
print(pd.crosstab(df["pdays"] == 999, df["poutcome"]))

#EDA PROCESS
print("=" * 60)
print("NUMERICAL DISTRIBUTIONS")
print("=" * 60)

# Numerical columns that we want to analyse
numerical_cols= ["age" , "campaign" , "pdays", "previous", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
print(numerical_cols)

# Import libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns


# Plot distribution of each numerical column
for col in numerical_cols:
    plt.figure(figsize=(8,4))

    #create histogram
    sns.histplot(data=df, x=col, bins=30)

#add title and labels
plt.title(f"Distribution of {col}")
plt.xlabel(col)
plt.ylabel("Frequency")

#adjust layout
plt.tight_layout()

#display the graph
plt.show()