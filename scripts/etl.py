import pandas as pd

df = pd.read_csv(
    "data/DataCoSupplyChainDataset.csv",
    encoding="latin1"
)

print("Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())


print("\nData Types:")
print(df.dtypes)


df.drop(
    columns=[
        "Product Description",
        "Order Zipcode"
    ],
    inplace=True
)

df["Customer Fname"] = df["Customer Fname"].fillna(" Unknown")

df["Customer Zipcode"] = df["Customer Zipcode"].fillna(df["Customer Zipcode"].mode()[0])
print(df.isnull().sum())

df.duplicated().sum()
df.drop_duplicates(inplace=True)
 
df.info()

print(df["Category Name"].value_counts().head(10))
print(df["Delivery Status"].value_counts())
print(df["Customer Country"].value_counts().head(10))
print(df["Market"].value_counts())



df.columns= df.columns.str.lower().str.replace(" ", "_")
print(df.columns)
for col in df.columns:
    if "date" in col:
        print(col)

df["order_date_(dateorders)"] = pd.to_datetime(
    df["order_date_(dateorders)"]
)

df["shipping_date_(dateorders)"] = pd.to_datetime(
    df["shipping_date_(dateorders)"]
)



df["order_year"] = df["order_date_(dateorders)"].dt.year

df["order_month"] = df["order_date_(dateorders)"].dt.month_name()



df["delivery_delay"] = (
    df["days_for_shipping_(real)"]
    - df["days_for_shipment_(scheduled)"]
)

df["profit_margin"] = (
    df["benefit_per_order"] / df["sales"]
) * 100

print(df["late_delivery_risk"].unique())

keep_cols = [
    "order_date_(dateorders)",
    "sales",
    "benefit_per_order",
    "order_item_quantity",
    "product_name",
    "category_name",
    "department_name",
    "customer_state",
    "market",
    "delivery_status",
    "late_delivery_risk",
    "customer_id",
    "order_year",
    "order_month",
    "profit_margin"

]

df= df[keep_cols]

df.info()

df.to_csv(
    "data/cleaned_supply_chain.csv",
    index=False
)
