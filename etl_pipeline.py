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

#lets get some summary
def load(df, output_path):
    #it gives the revenue of a region per category
    summary = (
        df.groupby(['category', 'region'])['revenue_after_tax']
            .sum()
            .sort_values(ascending=False)
            .reset_index()
    )
    summary.to_csv(output_path, index = False)
    return summary


if __name__ == "__main__":
    csv_df = extract('data/raw_csv_sales.csv')
    df = transform(csv_df)
    load(df, 'data/sales_summary.csv')
    print(df)