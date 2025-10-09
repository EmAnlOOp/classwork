def eda(df, max_uniques:int=10) -> None:
    """
    A function to perform based EDA tasks on a dataframe 
    which prints out information on each column 
    
    Arguments:
        df:pd.DataFrame = A pandas dataframe
        max_uniques:int = the max  of unique values for which 
        we will pprint out those values on categorical columns.
        defaults to 10 
    Returns:
        None 
    """
    import pandas as pd
    print(f"DF shape = {df.shape}")
    num_cols =[]
    cat_cols = []
    for col in df.columns:
        print(f"{'='*4}{col}{'='*4}")
        if pd.api.types.is_numeric_dtype(df[col]):
            num_cols.append(col)
        else:
            cat_cols.append(col)
    print(f"{'='*4}Numeric Columns{'='*4}")
    for col in num_cols:
        print(f"{col}")
        print(f"\t{col} is numeric")
        print(f"\t Mean = {df[col].mean()}")
        print(f"Median = {df[col].median()}")
        print(f"Mode = {df[col].mode()}")
        print(f"\t ST.Dev = {df[col].std():.3f}")
        print(f"\t 33%ile = {df[col].quantile(0.33)}")           
        print(f"\t 66%ile = {df[col].quantile(0.66)}")
        
    print(f"\n{'='*4}Categorical Columns{'='*4}")
    for col in cat_cols: 
     print(f"{col}")
     print(f"\t is categorical")
     print(f"\t # Nullish = {df[col].isna().sum()}")
     print(f"\t # unique value = {df[col].nunique()}")
     if df[col].nunique() < max_uniques:
        print(f"\t\t uniques = {df[col].unique()}")