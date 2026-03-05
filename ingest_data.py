import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'

def run():
    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    pg_user = 'root'
    pg_password = 'root'
    pg_host = 'localhost'
    pg_db = 'ny_taxi'
    pg_port = 5433
    chunksize = 100000

    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

    #we create an iterator to iterate through the batches of data and ingest the data into postgresql db 
    df_iter = pd.read_csv(
        url,
        dtype = dtype,
        parse_dates = parse_dates,
        iterator = True,
        chunksize = chunksize
    )

    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(
                name = 'yellow_taxi_data',
                con = engine, 
                if_exists = 'replace'
            )
            first = False
        df_chunk.to_sql(
            name = 'yellow_taxi_data', 
            con = engine, 
            if_exists = 'append'
        )

if __name__ == '__main__':
    run()