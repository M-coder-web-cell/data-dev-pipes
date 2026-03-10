import pandas as pd


def extract(filepath):
    df = pd.read_csv(filepath)
    return df

def transform(df):

    df = df.dropna(subset=["amount"])
    df = df[df['amount']>0]

    df['date'] = pd.to_datetime(df['date'], format = 'mixed', dayfirst = True)

    df['category'] = df['category'].str.title()
    print("Categories:", df["category"].unique())

    df['revenue_after_tax'] = df['amount'] * 0.9

    return df


if __name__ == "__main__":
    csv_df = extract('data/raw_csv_sales.csv')
    df = transform(csv_df)
    print(df)