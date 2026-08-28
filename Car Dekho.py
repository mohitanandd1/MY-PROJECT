# ============================================================
# CAR MARKET TRENDS ANALYSIS USING CAR DEKHO DATA
# ============================================================

# -------------------------------
# 1. IMPORT LIBRARIES
# -------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# Seaborn style
sns.set_theme(style="whitegrid")


# ============================================================
# 2. DATA LOADING
# ============================================================

# Excel file name
file_path = "Car Market Trends Analysis with Car Dekho Data.xlsx"

# Read Excel file
file_path = r"C:\Users\mohit\OneDrive\Documents\EXCELPRACTICEDATASET\Car Market Trends Analysis with Car Dekho Data.xlsx"

df = pd.read_excel(file_path)
print("\n================================================")
print("             DATA LOADED SUCCESSFULLY")
print("================================================")

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())


# ============================================================
# 3. BASIC DATA INFORMATION
# ============================================================

print("\n================================================")
print("              DATA INFORMATION")
print("================================================")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

print("\n================================================")
print("              MISSING VALUES")
print("================================================")

missing_values = df.isnull().sum()

print(missing_values)

print("\nMissing value percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)


# ============================================================
# 5. CHECK DUPLICATE VALUES
# ============================================================

print("\n================================================")
print("              DUPLICATE VALUES")
print("================================================")

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)


# ============================================================
# 6. REMOVE DUPLICATE VALUES
# ============================================================

if duplicates > 0:
    df = df.drop_duplicates()
    print("\nDuplicate rows removed.")
else:
    print("\nNo duplicate rows found.")


# ============================================================
# 7. HANDLE MISSING VALUES
# ============================================================

print("\n================================================")
print("            HANDLING MISSING VALUES")
print("================================================")

# Numerical columns
numeric_columns = df.select_dtypes(include=np.number).columns

# Fill numerical missing values with median
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

# Categorical columns
categorical_columns = df.select_dtypes(include="object").columns

# Fill categorical missing values with mode
for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

print("Missing values handled successfully.")

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ============================================================
# 8. STATISTICAL SUMMARY
# ============================================================

print("\n================================================")
print("             STATISTICAL SUMMARY")
print("================================================")

print(df.describe())


# ============================================================
# 9. UNIQUE VALUES OF CATEGORICAL COLUMNS
# ============================================================

print("\n================================================")
print("           UNIQUE CATEGORY VALUES")
print("================================================")

categorical_check = [
    "Fuel_Type",
    "Selling_type",
    "Transmission",
    "Owner"
]

for column in categorical_check:

    if column in df.columns:
        print(f"\n{column}:")
        print(df[column].unique())


# ============================================================
# 10. DATA CLEANING / COLUMN STANDARDIZATION
# ============================================================

print("\n================================================")
print("          CHECKING COLUMN NAMES")
print("================================================")

print(df.columns.tolist())


# ============================================================
# 11. CREATE CAR AGE COLUMN
# ============================================================

# Current year
current_year = 2026

if "Year" in df.columns:

    df["Car_Age"] = current_year - df["Year"]

    print("\nCar age column created successfully.")

    print(df[["Year", "Car_Age"]].head())


# ============================================================
# 12. EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n================================================")
print("           EXPLORATORY DATA ANALYSIS")
print("================================================")

# Selling price statistics

if "Selling_Price" in df.columns:

    print("\nSelling Price Statistics:")

    print("Minimum Selling Price:",
          df["Selling_Price"].min())

    print("Maximum Selling Price:",
          df["Selling_Price"].max())

    print("Average Selling Price:",
          df["Selling_Price"].mean())

    print("Median Selling Price:",
          df["Selling_Price"].median())


# Present price statistics

if "Present_Price" in df.columns:

    print("\nPresent Price Statistics:")

    print("Minimum Present Price:",
          df["Present_Price"].min())

    print("Maximum Present Price:",
          df["Present_Price"].max())

    print("Average Present Price:",
          df["Present_Price"].mean())


# Kilometers driven

if "Kms_Driven" in df.columns:

    print("\nKilometers Driven Statistics:")

    print("Minimum:",
          df["Kms_Driven"].min())

    print("Maximum:",
          df["Kms_Driven"].max())

    print("Average:",
          df["Kms_Driven"].mean())


# ============================================================
# 13. FUEL TYPE ANALYSIS
# ============================================================

if "Fuel_Type" in df.columns:

    print("\n================================================")
    print("              FUEL TYPE ANALYSIS")
    print("================================================")

    fuel_count = df["Fuel_Type"].value_counts()

    print("\nNumber of cars by fuel type:")
    print(fuel_count)

    fuel_price = df.groupby("Fuel_Type")["Selling_Price"].mean()

    print("\nAverage selling price by fuel type:")
    print(fuel_price)


# ============================================================
# 14. SELLER TYPE ANALYSIS
# ============================================================

# The standard Car Dekho dataset uses Selling_type
# Example values: Dealer / Individual

if "Selling_type" in df.columns:

    print("\n================================================")
    print("             SELLER TYPE ANALYSIS")
    print("================================================")

    seller_count = df["Selling_type"].value_counts()

    print("\nCars by seller type:")
    print(seller_count)

    seller_price = df.groupby(
        "Selling_type"
    )["Selling_Price"].mean()

    print("\nAverage selling price by seller type:")
    print(seller_price)


# ============================================================
# 15. TRANSMISSION ANALYSIS
# ============================================================

if "Transmission" in df.columns:

    print("\n================================================")
    print("            TRANSMISSION ANALYSIS")
    print("================================================")

    transmission_count = df["Transmission"].value_counts()

    print("\nCars by transmission type:")
    print(transmission_count)

    transmission_price = df.groupby(
        "Transmission"
    )["Selling_Price"].mean()

    print("\nAverage selling price by transmission:")
    print(transmission_price)


# ============================================================
# 16. OWNER ANALYSIS
# ============================================================

if "Owner" in df.columns:

    print("\n================================================")
    print("               OWNER ANALYSIS")
    print("================================================")

    owner_count = df["Owner"].value_counts().sort_index()

    print("\nNumber of cars according to previous owners:")
    print(owner_count)

    owner_price = df.groupby(
        "Owner"
    )["Selling_Price"].mean()

    print("\nAverage selling price by number of owners:")
    print(owner_price)


# ============================================================
# 17. YEAR-WISE ANALYSIS
# ============================================================

if "Year" in df.columns:

    print("\n================================================")
    print("                YEAR ANALYSIS")
    print("================================================")

    year_price = df.groupby("Year")["Selling_Price"].mean()

    print("\nAverage selling price by manufacturing year:")
    print(year_price)


# ============================================================
# 18. CORRELATION ANALYSIS
# ============================================================

print("\n================================================")
print("             CORRELATION ANALYSIS")
print("================================================")

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)


# Correlation with Selling Price

if "Selling_Price" in correlation.columns:

    selling_price_corr = (
        correlation["Selling_Price"]
        .sort_values(ascending=False)
    )

    print("\nCorrelation with Selling Price:")
    print(selling_price_corr)


# ============================================================
# 19. DATA VISUALIZATION
# ============================================================

print("\n================================================")
print("              DATA VISUALIZATION")
print("================================================")


# ------------------------------------------------------------
# 19.1 DISTRIBUTION OF SELLING PRICE
# ------------------------------------------------------------

if "Selling_Price" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Selling_Price"],
        kde=True
    )

    plt.title("Distribution of Car Selling Prices")
    plt.xlabel("Selling Price")
    plt.ylabel("Number of Cars")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.2 PRESENT PRICE VS SELLING PRICE
# ------------------------------------------------------------

if "Present_Price" in df.columns and "Selling_Price" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Present_Price",
        y="Selling_Price"
    )

    plt.title("Present Price vs Selling Price")
    plt.xlabel("Present Price")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.3 KILOMETERS DRIVEN VS SELLING PRICE
# ------------------------------------------------------------

if "Kms_Driven" in df.columns and "Selling_Price" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Kms_Driven",
        y="Selling_Price"
    )

    plt.title("Kilometers Driven vs Selling Price")
    plt.xlabel("Kilometers Driven")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.4 CAR AGE VS SELLING PRICE
# ------------------------------------------------------------

if "Car_Age" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Car_Age",
        y="Selling_Price"
    )

    plt.title("Car Age vs Selling Price")
    plt.xlabel("Car Age (Years)")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.5 FUEL TYPE DISTRIBUTION
# ------------------------------------------------------------

if "Fuel_Type" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.countplot(
        data=df,
        x="Fuel_Type"
    )

    plt.title("Number of Cars by Fuel Type")
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Cars")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.6 FUEL TYPE VS SELLING PRICE
# ------------------------------------------------------------

if "Fuel_Type" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df,
        x="Fuel_Type",
        y="Selling_Price"
    )

    plt.title("Selling Price by Fuel Type")
    plt.xlabel("Fuel Type")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.7 TRANSMISSION DISTRIBUTION
# ------------------------------------------------------------

if "Transmission" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.countplot(
        data=df,
        x="Transmission"
    )

    plt.title("Number of Cars by Transmission Type")
    plt.xlabel("Transmission")
    plt.ylabel("Number of Cars")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.8 TRANSMISSION VS SELLING PRICE
# ------------------------------------------------------------

if "Transmission" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df,
        x="Transmission",
        y="Selling_Price"
    )

    plt.title("Selling Price by Transmission Type")
    plt.xlabel("Transmission")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.9 SELLER TYPE DISTRIBUTION
# ------------------------------------------------------------

if "Selling_type" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.countplot(
        data=df,
        x="Selling_type"
    )

    plt.title("Number of Cars by Seller Type")
    plt.xlabel("Seller Type")
    plt.ylabel("Number of Cars")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.10 SELLER TYPE VS SELLING PRICE
# ------------------------------------------------------------

if "Selling_type" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df,
        x="Selling_type",
        y="Selling_Price"
    )

    plt.title("Selling Price by Seller Type")
    plt.xlabel("Seller Type")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.11 OWNER VS SELLING PRICE
# ------------------------------------------------------------

if "Owner" in df.columns:

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        data=df,
        x="Owner",
        y="Selling_Price"
    )

    plt.title("Selling Price by Number of Previous Owners")
    plt.xlabel("Previous Owners")
    plt.ylabel("Selling Price")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.12 YEAR VS SELLING PRICE
# ------------------------------------------------------------

if "Year" in df.columns:

    yearly_price = df.groupby(
        "Year"
    )["Selling_Price"].mean().reset_index()

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=yearly_price,
        x="Year",
        y="Selling_Price",
        marker="o"
    )

    plt.title("Average Selling Price by Manufacturing Year")
    plt.xlabel("Manufacturing Year")
    plt.ylabel("Average Selling Price")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19.13 CORRELATION HEATMAP
# ------------------------------------------------------------

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# ============================================================
# 20. TOP EXPENSIVE CARS
# ============================================================

if "Selling_Price" in df.columns:

    print("\n================================================")
    print("             TOP 10 EXPENSIVE CARS")
    print("================================================")

    top_cars = df.sort_values(
        by="Selling_Price",
        ascending=False
    ).head(10)

    print(top_cars)


# ============================================================
# 21. CHEAPEST CARS
# ============================================================

if "Selling_Price" in df.columns:

    print("\n================================================")
    print("              TOP 10 CHEAPEST CARS")
    print("================================================")

    cheapest_cars = df.sort_values(
        by="Selling_Price",
        ascending=True
    ).head(10)

    print(cheapest_cars)


# ============================================================
# 22. HIGH KILOMETER CARS
# ============================================================

if "Kms_Driven" in df.columns:

    print("\n================================================")
    print("           TOP 10 HIGH-MILEAGE CARS")
    print("================================================")

    high_km = df.sort_values(
        by="Kms_Driven",
        ascending=False
    ).head(10)

    print(high_km)


# ============================================================
# 23. FINAL DATASET
# ============================================================

print("\n================================================")
print("              FINAL DATASET")
print("================================================")

print("Final dataset shape:", df.shape)

print("\nFinal dataset:")
print(df.head())

print("\n================================================")
print("        CAR MARKET ANALYSIS COMPLETED")
print("================================================")



