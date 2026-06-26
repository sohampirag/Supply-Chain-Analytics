import pandas as pd
from sqlalchemy import create_engine

# Read cleaned data
df = pd.read_csv("cleaned_supply_chain.csv")

# Connect MySQL
engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/supply_chain"
)

# Load table
df.to_sql(
    "orders",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")
