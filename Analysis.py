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