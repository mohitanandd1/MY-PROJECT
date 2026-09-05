import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_excel('C:\\mohit_anand\\c_learning\\.vscode\\PYTHON\\INTERNSHIP PROJECT.py\\Unicorn_Companies.xlsx')
# df = pd.read_excel('Unicorn_Companies.xlsx')

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns.to_list)
print(df.describe())
print(df.describe(include='all'))

print(df.duplicated().sum())
print(df.isnull().sum())


print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

print(df.info())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe(include="all").T)

print("\nFirst 10 Records:")
print(df.head(10))

print("\nLast 10 Records:")
print(df.tail(10))


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUE ANALYSIS")
print("=" * 70)

missing_values = df.isnull().sum()

print(missing_values)

missing_percentage = (
    df.isnull().sum() / len(df) * 100
).round(2)

missing_table = pd.DataFrame({
    "Missing Values": missing_values,
    "Missing Percentage": missing_percentage
})

print("\nMissing Value Summary:")
print(missing_table)


# ============================================================
# 5. CHECK DUPLICATES
# ============================================================

print("\n" + "=" * 70)
print("DUPLICATE ANALYSIS")
print("=" * 70)

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)


# ============================================================
# 6. CHECK UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("UNIQUE VALUE ANALYSIS")
print("=" * 70)

for column in df.columns:
    print(
        f"{column}: {df[column].nunique()} unique values"
    )


# ============================================================
# 7. DATA CLEANING
# ============================================================

print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)

# Make a copy
clean_df = df.copy()

# Remove duplicate records
clean_df.drop_duplicates(inplace=True)

# Remove leading/trailing spaces from text columns
text_columns = clean_df.select_dtypes(
    include=["object"]
).columns

for column in text_columns:
    clean_df[column] = clean_df[column].astype(str).str.strip()


# ------------------------------------------------------------
# Clean Valuation column
# ------------------------------------------------------------

print("\nOriginal Valuation examples:")
print(clean_df["Valuation"].head())

# Remove $ and B
clean_df["Valuation_Billion"] = (
    clean_df["Valuation"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace("B", "", regex=False)
    .str.strip()
)

clean_df["Valuation_Billion"] = pd.to_numeric(
    clean_df["Valuation_Billion"],
    errors="coerce"
)


# ------------------------------------------------------------
# Clean Funding column
# ------------------------------------------------------------

print("\nOriginal Funding examples:")
print(clean_df["Funding"].head())

clean_df["Funding_Billion"] = (
    clean_df["Funding"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace("B", "", regex=False)
    .str.replace("M", "", regex=False)
    .str.strip()
)

# Function to convert funding values
def convert_funding(value):

    try:

        value = str(value).strip()

        if value.lower() in ["nan", "none", "n/a"]:
            return np.nan

        # Values ending with B are already in billions
        if value.upper().endswith("B"):
            return float(
                value[:-1].replace(",", "")
            )

        # Values ending with M are converted to billions
        elif value.upper().endswith("M"):
            return float(
                value[:-1].replace(",", "")
            ) / 1000

        else:
            return float(
                value.replace(",", "")
            )

    except:
        return np.nan


clean_df["Funding_Billion"] = df["Funding"].apply(
    convert_funding
)


# ============================================================
# 8. HANDLE MISSING VALUES
# ============================================================

print("\nMissing values before treatment:")
print(clean_df.isnull().sum())

# Numeric columns
numeric_columns = [
    "Valuation_Billion",
    "Funding_Billion",
    "Year Founded"
]

for column in numeric_columns:

    if column in clean_df.columns:
        clean_df[column] = clean_df[column].fillna(
            clean_df[column].median()
        )

# Categorical columns
categorical_columns = [
    "Industry",
    "City",
    "Country",
    "Continent"
]

for column in categorical_columns:

    if column in clean_df.columns:

        mode_value = clean_df[column].mode()

        if len(mode_value) > 0:
            clean_df[column] = clean_df[column].fillna(
                mode_value[0]
            )


print("\nMissing values after treatment:")
print(clean_df.isnull().sum())


# ============================================================
# 9. DATE PREPROCESSING
# ============================================================

clean_df["Date Joined"] = pd.to_datetime(
    clean_df["Date Joined"],
    errors="coerce"
)

# Extract year and month
clean_df["Joined Year"] = (
    clean_df["Date Joined"].dt.year
)

clean_df["Joined Month"] = (
    clean_df["Date Joined"].dt.month
)

clean_df["Joined Month Name"] = (
    clean_df["Date Joined"].dt.month_name()
)


# ============================================================
# 10. COMPANY AGE CALCULATION
# ============================================================

clean_df["Company Age"] = (
    clean_df["Joined Year"] -
    clean_df["Year Founded"]
)

print("\nCompany Age Summary:")
print(clean_df["Company Age"].describe())


# ============================================================
# 11. FINAL DATASET INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("CLEANED DATASET INFORMATION")
print("=" * 70)

print("Rows:", clean_df.shape[0])
print("Columns:", clean_df.shape[1])

print("\nData Types:")
print(clean_df.dtypes)

print("\nCleaned Data:")
print(clean_df.head())


# ============================================================
# 12. EDA - TOP INDUSTRIES
# ============================================================

print("\n" + "=" * 70)
print("TOP INDUSTRIES")
print("=" * 70)

industry_count = (
    clean_df["Industry"]
    .value_counts()
)

print(industry_count.head(10))


# ============================================================
# 13. EDA - TOP COUNTRIES
# ============================================================

print("\n" + "=" * 70)
print("TOP COUNTRIES")
print("=" * 70)

country_count = (
    clean_df["Country"]
    .value_counts()
)

print(country_count.head(15))


# ============================================================
# 14. EDA - TOP CITIES
# ============================================================

print("\n" + "=" * 70)
print("TOP CITIES")
print("=" * 70)

city_count = (
    clean_df["City"]
    .value_counts()
)

print(city_count.head(15))


# ============================================================
# 15. EDA - CONTINENT ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("UNICORNS BY CONTINENT")
print("=" * 70)

continent_count = (
    clean_df["Continent"]
    .value_counts()
)

print(continent_count)


# ============================================================
# 16. KPI ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("KEY PERFORMANCE INDICATORS")
print("=" * 70)

total_unicorns = clean_df["Company"].nunique()

total_valuation = clean_df[
    "Valuation_Billion"
].sum()

average_valuation = clean_df[
    "Valuation_Billion"
].mean()

median_valuation = clean_df[
    "Valuation_Billion"
].median()

total_funding = clean_df[
    "Funding_Billion"
].sum()

average_funding = clean_df[
    "Funding_Billion"
].mean()

largest_valuation = clean_df[
    "Valuation_Billion"
].max()

oldest_company_year = clean_df[
    "Year Founded"
].min()

youngest_company_year = clean_df[
    "Year Founded"
].max()


print("Total Unicorn Companies:", total_unicorns)
print("Total Valuation ($B):", round(total_valuation, 2))
print("Average Valuation ($B):", round(average_valuation, 2))
print("Median Valuation ($B):", round(median_valuation, 2))
print("Total Funding ($B):", round(total_funding, 2))
print("Average Funding ($B):", round(average_funding, 2))
print("Highest Valuation ($B):", round(largest_valuation, 2))
print("Oldest Company Founded:", oldest_company_year)
print("Latest Company Founded:", youngest_company_year)


# ============================================================
# 17. TOP 10 MOST VALUABLE COMPANIES
# ============================================================

print("\n" + "=" * 70)
print("TOP 10 MOST VALUABLE COMPANIES")
print("=" * 70)

top_10_valuation = clean_df[
    [
        "Company",
        "Valuation_Billion",
        "Industry",
        "Country"
    ]
].sort_values(
    by="Valuation_Billion",
    ascending=False
).head(10)

print(top_10_valuation.to_string(index=False))


# ============================================================
# 18. TOP 10 INDUSTRIES BY VALUATION
# ============================================================

industry_valuation = (
    clean_df
    .groupby("Industry")["Valuation_Billion"]
    .sum()
    .sort_values(ascending=False)
)

print("\n" + "=" * 70)
print("TOP INDUSTRIES BY TOTAL VALUATION")
print("=" * 70)

print(industry_valuation.head(10))


# ============================================================
# 19. TOP COUNTRIES BY TOTAL VALUATION
# ============================================================

country_valuation = (
    clean_df
    .groupby("Country")["Valuation_Billion"]
    .sum()
    .sort_values(ascending=False)
)

print("\n" + "=" * 70)
print("TOP COUNTRIES BY TOTAL VALUATION")
print("=" * 70)

print(country_valuation.head(10))


# ============================================================
# 20. UNICORNS CREATED BY YEAR
# ============================================================

unicorn_by_year = (
    clean_df["Joined Year"]
    .value_counts()
    .sort_index()
)

print("\n" + "=" * 70)
print("UNICORNS CREATED BY YEAR")
print("=" * 70)

print(unicorn_by_year)


# ============================================================
# 21. YEAR-ON-YEAR ANALYSIS
# ============================================================

year_analysis = (
    clean_df
    .groupby("Joined Year")
    .agg(
        Unicorns=("Company", "nunique"),
        Total_Valuation=("Valuation_Billion", "sum"),
        Average_Valuation=("Valuation_Billion", "mean"),
        Total_Funding=("Funding_Billion", "sum")
    )
    .reset_index()
)

print("\nYear-wise Analysis:")
print(year_analysis.tail(15))


# ============================================================
# 22. VISUALIZATION 1
# TOP 10 INDUSTRIES BY NUMBER OF UNICORNS
# ============================================================

plt.figure(figsize=(12, 6))

top_industries = (
    clean_df["Industry"]
    .value_counts()
    .head(10)
)

sns.barplot(
    x=top_industries.values,
    y=top_industries.index
)

plt.title("Top 10 Industries by Number of Unicorn Companies")
plt.xlabel("Number of Unicorns")
plt.ylabel("Industry")

plt.tight_layout()
plt.show()


# ============================================================
# 23. VISUALIZATION 2
# TOP 10 COUNTRIES
# ============================================================

plt.figure(figsize=(12, 6))

top_countries = (
    clean_df["Country"]
    .value_counts()
    .head(10)
)

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries by Number of Unicorn Companies")
plt.xlabel("Number of Unicorns")
plt.ylabel("Country")

plt.tight_layout()
plt.show()


# ============================================================
# 24. VISUALIZATION 3
# CONTINENT DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 6))

continent_data = (
    clean_df["Continent"]
    .value_counts()
)

plt.pie(
    continent_data.values,
    labels=continent_data.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Unicorn Companies by Continent")

plt.tight_layout()
plt.show()


# ============================================================
# 25. VISUALIZATION 4
# UNICORNS BY YEAR
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    unicorn_by_year.index,
    unicorn_by_year.values,
    marker="o"
)

plt.title("Number of Unicorn Companies by Year")
plt.xlabel("Year")
plt.ylabel("Number of Unicorns")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 26. VISUALIZATION 5
# TOTAL VALUATION BY YEAR
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    year_analysis["Joined Year"],
    year_analysis["Total_Valuation"],
    marker="o"
)

plt.title("Total Unicorn Valuation by Year")
plt.xlabel("Year")
plt.ylabel("Total Valuation ($ Billion)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 27. VISUALIZATION 6
# TOP 10 COMPANIES BY VALUATION
# ============================================================

plt.figure(figsize=(12, 6))

top_companies = (
    clean_df
    .sort_values(
        "Valuation_Billion",
        ascending=False
    )
    .head(10)
)

sns.barplot(
    data=top_companies,
    x="Valuation_Billion",
    y="Company"
)

plt.title("Top 10 Most Valuable Unicorn Companies")
plt.xlabel("Valuation ($ Billion)")
plt.ylabel("Company")

plt.tight_layout()
plt.show()


# ============================================================
# 28. VISUALIZATION 7
# VALUATION DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    clean_df["Valuation_Billion"],
    bins=30,
    kde=True
)

plt.title("Distribution of Unicorn Company Valuations")
plt.xlabel("Valuation ($ Billion)")
plt.ylabel("Number of Companies")

plt.tight_layout()
plt.show()


# ============================================================
# 29. VISUALIZATION 8
# FUNDING DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    clean_df["Funding_Billion"].dropna(),
    bins=30,
    kde=True
)

plt.title("Distribution of Funding")
plt.xlabel("Funding ($ Billion)")
plt.ylabel("Number of Companies")

plt.tight_layout()
plt.show()


# ============================================================
# 30. VISUALIZATION 9
# VALUATION VS FUNDING
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=clean_df,
    x="Funding_Billion",
    y="Valuation_Billion",
    alpha=0.7
)

plt.title("Relationship Between Funding and Valuation")
plt.xlabel("Funding ($ Billion)")
plt.ylabel("Valuation ($ Billion)")

plt.tight_layout()
plt.show()


# ============================================================
# 31. VISUALIZATION 10
# COMPANY AGE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    clean_df["Company Age"],
    bins=25,
    kde=True
)

plt.title("Distribution of Unicorn Company Age")
plt.xlabel("Company Age at Unicorn Status")
plt.ylabel("Number of Companies")

plt.tight_layout()
plt.show()


# ============================================================
# 32. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("CORRELATION ANALYSIS")
print("=" * 70)

correlation_columns = [
    "Valuation_Billion",
    "Funding_Billion",
    "Year Founded",
    "Joined Year",
    "Company Age"
]

correlation_matrix = clean_df[
    correlation_columns
].corr()

print(correlation_matrix)


# ============================================================
# 33. CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# ============================================================
# 34. INDUSTRY SUMMARY
# ============================================================

industry_summary = (
    clean_df
    .groupby("Industry")
    .agg(
        Number_of_Unicorns=("Company", "nunique"),
        Total_Valuation=("Valuation_Billion", "sum"),
        Average_Valuation=("Valuation_Billion", "mean"),
        Total_Funding=("Funding_Billion", "sum")
    )
    .sort_values(
        "Number_of_Unicorns",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("INDUSTRY SUMMARY")
print("=" * 70)

print(industry_summary.head(15))


# ============================================================
# 35. COUNTRY SUMMARY
# ============================================================

country_summary = (
    clean_df
    .groupby("Country")
    .agg(
        Number_of_Unicorns=("Company", "nunique"),
        Total_Valuation=("Valuation_Billion", "sum"),
        Average_Valuation=("Valuation_Billion", "mean"),
        Total_Funding=("Funding_Billion", "sum")
    )
    .sort_values(
        "Number_of_Unicorns",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("COUNTRY SUMMARY")
print("=" * 70)

print(country_summary.head(15))


# ============================================================
# 36. SAVE CLEANED DATASET
# ============================================================

output_file = "Cleaned_Unicorn_Companies.xlsx"

clean_df.to_excel(
    output_file,
    index=False
)

print("\n" + "=" * 70)
print("CLEANED DATASET SAVED")
print("=" * 70)

print("File:", output_file)


# ============================================================
# 37. SAVE SUMMARY REPORT
# ============================================================

summary = {
    "Total Unicorn Companies": total_unicorns,
    "Total Valuation ($B)": round(total_valuation, 2),
    "Average Valuation ($B)": round(average_valuation, 2),
    "Median Valuation ($B)": round(median_valuation, 2),
    "Total Funding ($B)": round(total_funding, 2),
    "Average Funding ($B)": round(average_funding, 2),
    "Highest Valuation ($B)": round(largest_valuation, 2),
    "Oldest Company Founded": oldest_company_year,
    "Latest Company Founded": youngest_company_year
}


summary_df = pd.DataFrame(
    list(summary.items()),
    columns=["KPI", "Value"]
)

summary_df.to_csv(
    "Unicorn_KPI_Summary.csv",
    index=False
)

print("\nKPI summary saved as:")
print("Unicorn_KPI_Summary.csv")


# ============================================================
# 38. END
# ============================================================

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)