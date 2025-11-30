import pandas as pd
def read_datafrom_excel():
    df = pd.read_excel("Data.xlsx")
    print(df)

read_datafrom_excel()

def read_sheet_data():
    df = pd.read_excel("Data.xlsx", sheet_name="Sheet2")
    print(df)
    print(df[["Username", "email"]])
    print(df.iloc[0, 1])
    print(df.iloc[1, 0])
    df.loc[4, "Username"] = "Thavamani"
    df.to_excel("Data.xlsx", index=False)

read_sheet_data()