#-----------------------LIBRARIES----------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid")

#--------------------------DATA LOADING--------------------
df=pd.read_excel('INTERNSHIP PROJECT.py\\seasonal_agriculture_performance_dataset .csv.xlsx')

#--------------------------DATA DESCRIPTION----------------
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

# ----------------DATA CLEANING-------------------------------
# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")

missing = df.isnull().sum()

print(missing)

print("\nMissing percentage:")

missing_percentage = (
    df.isnull().sum() / len(df) * 100
).round(2)

print(missing_percentage)


# ============================================================
# 5. CHECK DUPLICATES
# ============================================================

print("\n========== DUPLICATE CHECK ==========")

print("Duplicate rows:", df.duplicated().sum())


# ============================================================
# 6. DATA CLEANING
# ============================================================

print("\n========== DATA CLEANING ==========")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from text columns
text_columns = df.select_dtypes(
    include="object"
).columns

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# Handle missing numerical values
numeric_columns = df.select_dtypes(
    include=np.number
).columns

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )

# Handle missing categorical values
categorical_columns = df.select_dtypes(
    include="object"
).columns

for column in categorical_columns:

    if df[column].isnull().sum() > 0:

        df[column] = df[column].fillna(
            df[column].mode()[0]
        )


print("Cleaning completed.")

print("\nMissing values after cleaning:")
print(df.isnull().sum().sum())

print("Duplicate rows after cleaning:")
print(df.duplicated().sum())


# ============================================================
# 7. CHECK UNIQUE VALUES
# ============================================================

print("\n========== UNIQUE VALUES ==========")

print("Number of States:",
      df["State"].nunique())

print("Number of Districts:",
      df["District"].nunique())

print("Number of Crops:",
      df["Crop"].nunique())

print("Number of Seasons:",
      df["Season"].nunique())

print("Number of Irrigation Methods:",
      df["Irrigation_Method"].nunique())

#----------------------ANALYSIS-------------------------------
# ============================================================
# SEASONAL AGRICULTURE PERFORMANCE ANALYSIS
# ============================================================

print("\n" + "=" * 80)
print("SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print("=" * 80)


# ------------------------------------------------------------
# 1. NUMBER OF RECORDS IN EACH SEASON
# ------------------------------------------------------------

print("\n1. NUMBER OF FARMS IN EACH SEASON")
print("-" * 60)

season_count = df["Season"].value_counts()

print(season_count)


# ------------------------------------------------------------
# 2. AGRICULTURAL PERFORMANCE ACROSS SEASONS
# ------------------------------------------------------------

print("\n2. AGRICULTURAL PERFORMANCE ACROSS SEASONS")
print("-" * 60)

season_performance = df.groupby("Season").agg(
    Farms=("Farm_ID", "count"),
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Total_Production=("Production_Tonnes", "sum"),
    Average_Production=("Production_Tonnes", "mean"),
    Total_Revenue=("Revenue_INR", "sum"),
    Total_Cost=("Total_Cost_INR", "sum"),
    Total_Profit=("Profit_INR", "sum"),
    Average_Profit=("Profit_INR", "mean")
).round(2)

print(season_performance)


# ------------------------------------------------------------
# 3. MAJOR SEASONAL PATTERNS
# ------------------------------------------------------------

print("\n3. MAJOR SEASONAL PATTERNS")
print("-" * 60)

print("\nAverage Yield by Season:")
print(
    df.groupby("Season")["Yield_Tonnes_Ha"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nTotal Production by Season:")
print(
    df.groupby("Season")["Production_Tonnes"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)

print("\nTotal Profit by Season:")
print(
    df.groupby("Season")["Profit_INR"]
    .sum()
    .sort_values(ascending=False)
    .round(2)
)


# ------------------------------------------------------------
# 4. CHARACTERISTICS CHANGING BETWEEN SEASONS
# ------------------------------------------------------------

print("\n4. CHARACTERISTICS CHANGING BETWEEN SEASONS")
print("-" * 60)

season_characteristics = df.groupby("Season").agg(
    Average_Farm_Area=("Farm_Area_Hectares", "mean"),
    Average_Rainfall=("Rainfall_mm", "mean"),
    Average_Temperature=("Avg_Temperature_C", "mean"),
    Average_Humidity=("Humidity_pct", "mean"),
    Average_Soil_Moisture=("Soil_Moisture_pct", "mean"),
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Water_Usage=("Water_Used_m3", "mean"),
    Average_Water_Efficiency=(
        "Water_Efficiency_t_per_1000m3", "mean"
    ),
    Average_Disease_Pest_Risk=(
        "Disease_Pest_Risk_pct", "mean"
    )
).round(2)

print(season_characteristics)


# ------------------------------------------------------------
# 5. AGRICULTURAL ACTIVITIES IN DIFFERENT SEASONS
# ------------------------------------------------------------

print("\n5. AGRICULTURAL ACTIVITIES ACROSS SEASONS")
print("-" * 60)

print("\nCrop distribution by Season:")

crop_season = pd.crosstab(
    df["Season"],
    df["Crop"]
)

print(crop_season)


print("\nIrrigation Method by Season:")

irrigation_season = pd.crosstab(
    df["Season"],
    df["Irrigation_Method"]
)

print(irrigation_season)


# ------------------------------------------------------------
# 6. RESOURCE USAGE ACROSS SEASONS
# ------------------------------------------------------------

print("\n6. RESOURCE USAGE VARIATION ACROSS SEASONS")
print("-" * 60)

resource_usage = df.groupby("Season").agg(
    Average_Farm_Area=("Farm_Area_Hectares", "mean"),
    Average_Rainfall=("Rainfall_mm", "mean"),
    Average_Water_Used=("Water_Used_m3", "mean"),
    Average_Water_Efficiency=(
        "Water_Efficiency_t_per_1000m3", "mean"
    ),
    Average_Fertilizer=(
        "Fertilizer_kg_ha", "mean"
    ),
    Average_Pesticide=(
        "Pesticide_Litre_ha", "mean"
    )
).round(2)

print(resource_usage)


# ------------------------------------------------------------
# 7. ENVIRONMENTAL CONDITIONS VS AGRICULTURAL PERFORMANCE
# ------------------------------------------------------------

print("\n7. ENVIRONMENTAL CONDITIONS VS AGRICULTURAL PERFORMANCE")
print("-" * 60)

environment_performance = df.groupby("Season").agg(
    Rainfall=("Rainfall_mm", "mean"),
    Temperature=("Avg_Temperature_C", "mean"),
    Humidity=("Humidity_pct", "mean"),
    Soil_Moisture=("Soil_Moisture_pct", "mean"),
    Yield=("Yield_Tonnes_Ha", "mean"),
    Production=("Production_Tonnes", "mean"),
    Water_Efficiency=(
        "Water_Efficiency_t_per_1000m3", "mean"
    )
).round(2)

print(environment_performance)


print("\nCorrelation Between Rainfall and Yield:")

rainfall_yield_corr = df[
    ["Rainfall_mm", "Yield_Tonnes_Ha"]
].corr()

print(rainfall_yield_corr.round(3))


# ------------------------------------------------------------
# 8. ECONOMIC OUTCOMES ACROSS SEASONS
# ------------------------------------------------------------

print("\n8. ECONOMIC OUTCOMES ACROSS SEASONS")
print("-" * 60)

# Calculate profit margin
df["Profit_Margin_pct"] = np.where(
    df["Revenue_INR"] != 0,
    (df["Profit_INR"] / df["Revenue_INR"]) * 100,
    np.nan
)

economic_analysis = df.groupby("Season").agg(
    Total_Revenue=("Revenue_INR", "sum"),
    Total_Cost=("Total_Cost_INR", "sum"),
    Total_Profit=("Profit_INR", "sum"),
    Average_Revenue=("Revenue_INR", "mean"),
    Average_Cost=("Total_Cost_INR", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Profit_Margin=("Profit_Margin_pct", "mean")
).round(2)

print(economic_analysis)


# ------------------------------------------------------------
# 9. SEASONAL PATTERNS ACROSS DIFFERENT STATES
# ------------------------------------------------------------

print("\n9. SEASONAL PATTERNS ACROSS REGIONS")
print("-" * 60)

state_season_profit = pd.pivot_table(
    df,
    values="Profit_INR",
    index="State",
    columns="Season",
    aggfunc="mean"
).round(2)

print("\nAverage Profit by State and Season:")
print(state_season_profit)


print("\nAverage Yield by State and Season:")

state_season_yield = pd.pivot_table(
    df,
    values="Yield_Tonnes_Ha",
    index="State",
    columns="Season",
    aggfunc="mean"
).round(2)

print(state_season_yield)


# ------------------------------------------------------------
# 10. UNUSUAL / UNEXPECTED SEASONAL PATTERNS
# ------------------------------------------------------------

print("\n10. UNUSUAL OR UNEXPECTED SEASONAL PATTERNS")
print("-" * 60)

season_summary = df.groupby("Season").agg(
    Average_Yield=("Yield_Tonnes_Ha", "mean"),
    Average_Profit=("Profit_INR", "mean"),
    Average_Rainfall=("Rainfall_mm", "mean"),
    Average_Water_Usage=("Water_Used_m3", "mean"),
    Average_Risk=("Disease_Pest_Risk_pct", "mean")
).round(2)


highest_yield_season = (
    season_summary["Average_Yield"].idxmax()
)

lowest_yield_season = (
    season_summary["Average_Yield"].idxmin()
)

highest_profit_season = (
    season_summary["Average_Profit"].idxmax()
)

lowest_profit_season = (
    season_summary["Average_Profit"].idxmin()
)

highest_rainfall_season = (
    season_summary["Average_Rainfall"].idxmax()
)

lowest_rainfall_season = (
    season_summary["Average_Rainfall"].idxmin()
)

highest_risk_season = (
    season_summary["Average_Risk"].idxmax()
)

lowest_risk_season = (
    season_summary["Average_Risk"].idxmin()
)


print("Highest Yield Season:", highest_yield_season)
print("Lowest Yield Season:", lowest_yield_season)

print("Highest Profit Season:", highest_profit_season)
print("Lowest Profit Season:", lowest_profit_season)

print("Highest Rainfall Season:", highest_rainfall_season)
print("Lowest Rainfall Season:", lowest_rainfall_season)

print("Highest Disease/Pest Risk Season:",
      highest_risk_season)

print("Lowest Disease/Pest Risk Season:",
      lowest_risk_season)


# ------------------------------------------------------------
# 11. BEST AND WORST PERFORMING SEASON
# ------------------------------------------------------------

print("\n11. BEST AND WORST PERFORMING SEASONS")
print("-" * 60)

best_season = season_summary["Average_Profit"].idxmax()
worst_season = season_summary["Average_Profit"].idxmin()

print("Best Performing Season:", best_season)
print("Worst Performing Season:", worst_season)


# ------------------------------------------------------------
# 12. BEST CROP IN EACH SEASON
# ------------------------------------------------------------

print("\n12. BEST PERFORMING CROP IN EACH SEASON")
print("-" * 60)

crop_season_profit = (
    df.groupby(["Season", "Crop"])["Profit_INR"]
    .mean()
    .reset_index()
)

best_crop_each_season = (
    crop_season_profit
    .sort_values("Profit_INR", ascending=False)
    .groupby("Season")
    .head(1)
)

print(best_crop_each_season)


# ------------------------------------------------------------
# 13. BEST IRRIGATION METHOD IN EACH SEASON
# ------------------------------------------------------------

print("\n13. BEST IRRIGATION METHOD BY SEASON")
print("-" * 60)

irrigation_season_yield = (
    df.groupby(
        ["Season", "Irrigation_Method"]
    )["Yield_Tonnes_Ha"]
    .mean()
    .reset_index()
)

best_irrigation_each_season = (
    irrigation_season_yield
    .sort_values(
        "Yield_Tonnes_Ha",
        ascending=False
    )
    .groupby("Season")
    .head(1)
)

print(best_irrigation_each_season)


# ============================================================
# 14. CROP ANALYSIS
# ============================================================

print("\n========== CROP ANALYSIS ==========")

crop_count = df["Crop"].value_counts()

print(crop_count)


# ============================================================
# 15. SEASON ANALYSIS
# ============================================================

print("\n========== SEASON ANALYSIS ==========")

season_count = df["Season"].value_counts()

print(season_count)


# ============================================================
# 16. IRRIGATION METHOD ANALYSIS
# ============================================================

print("\n========== IRRIGATION METHOD ==========")

irrigation_count = (
    df["Irrigation_Method"]
    .value_counts()
)

print(irrigation_count)


# ============================================================
# 17. KPI / BUSINESS ANALYSIS
# ============================================================

print("\n========== KEY PERFORMANCE INDICATORS ==========")

total_farms = df["Farm_ID"].nunique()

total_production = df["Production_Tonnes"].sum()

average_yield = df["Yield_Tonnes_Ha"].mean()

total_revenue = df["Revenue_INR"].sum()

total_cost = df["Total_Cost_INR"].sum()

total_profit = df["Profit_INR"].sum()

average_profit = df["Profit_INR"].mean()

average_water_efficiency = (
    df["Water_Efficiency_t_per_1000m3"].mean()
)

average_disease_risk = (
    df["Disease_Pest_Risk_pct"].mean()
)


print("Total Farms:", total_farms)

print(
    "Total Production:",
    round(total_production, 2),
    "Tonnes"
)

print(
    "Average Yield:",
    round(average_yield, 2),
    "Tonnes/Ha"
)

print(
    "Total Revenue: ₹",
    round(total_revenue, 2)
)

print(
    "Total Cost: ₹",
    round(total_cost, 2)
)

print(
    "Total Profit: ₹",
    round(total_profit, 2)
)

print(
    "Average Profit: ₹",
    round(average_profit, 2)
)

print(
    "Average Water Efficiency:",
    round(average_water_efficiency, 2)
)

print(
    "Average Disease/Pest Risk:",
    round(average_disease_risk, 2),
    "%"
)


# ============================================================
# 16. PROFIT MARGIN
# ============================================================

df["Profit_Margin_pct"] = (
    df["Profit_INR"] /
    df["Revenue_INR"]
) * 100

print("\n========== PROFIT MARGIN ==========")

print(
    "Average Profit Margin:",
    round(
        df["Profit_Margin_pct"].mean(),
        2
    ),
    "%"
)


# ============================================================
# 17. CROP-WISE ANALYSIS
# ============================================================

crop_analysis = (
    df.groupby("Crop")
    .agg(
        Farms=("Farm_ID", "count"),
        Average_Yield=("Yield_Tonnes_Ha", "mean"),
        Total_Production=("Production_Tonnes", "sum"),
        Total_Revenue=("Revenue_INR", "sum"),
        Total_Profit=("Profit_INR", "sum")
    )
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n========== CROP-WISE ANALYSIS ==========")

print(crop_analysis)


# ============================================================
# 18. SEASON-WISE ANALYSIS
# ============================================================

season_analysis = (
    df.groupby("Season")
    .agg(
        Farms=("Farm_ID", "count"),
        Average_Yield=("Yield_Tonnes_Ha", "mean"),
        Total_Production=("Production_Tonnes", "sum"),
        Total_Revenue=("Revenue_INR", "sum"),
        Total_Profit=("Profit_INR", "sum")
    )
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n========== SEASON-WISE ANALYSIS ==========")

print(season_analysis)


# ============================================================
# 19. IRRIGATION-WISE ANALYSIS
# ============================================================

irrigation_analysis = (
    df.groupby("Irrigation_Method")
    .agg(
        Farms=("Farm_ID", "count"),
        Average_Yield=("Yield_Tonnes_Ha", "mean"),
        Total_Profit=("Profit_INR", "sum"),
        Average_Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        )
    )
    .sort_values(
        "Average_Yield",
        ascending=False
    )
)

print("\n========== IRRIGATION ANALYSIS ==========")

print(irrigation_analysis)


# ============================================================
# 20. STATE-WISE ANALYSIS
# ============================================================

state_analysis = (
    df.groupby("State")
    .agg(
        Farms=("Farm_ID", "count"),
        Average_Yield=("Yield_Tonnes_Ha", "mean"),
        Total_Production=("Production_Tonnes", "sum"),
        Total_Revenue=("Revenue_INR", "sum"),
        Total_Profit=("Profit_INR", "sum")
    )
    .sort_values(
        "Total_Profit",
        ascending=False
    )
)

print("\n========== TOP STATES BY PROFIT ==========")

print(state_analysis.head(10))


# ============================================================
# 21. TOP 10 MOST PROFITABLE FARMS
# ============================================================

top_farms = (
    df[
        [
            "Farm_ID",
            "State",
            "Crop",
            "Season",
            "Yield_Tonnes_Ha",
            "Revenue_INR",
            "Profit_INR"
        ]
    ]
    .sort_values(
        "Profit_INR",
        ascending=False
    )
    .head(10)
)

print("\n========== TOP 10 PROFITABLE FARMS ==========")

print(top_farms.to_string(index=False))

#---------------VISUALIZATION-------------------------------
# ============================================================
# 1. VISUALIZATION 1
# NUMBER OF FARMS BY CROP
# ============================================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    y="Crop",
    order=df["Crop"].value_counts().index
)

plt.title("Number of Farms by Crop")
plt.xlabel("Number of Farms")
plt.ylabel("Crop")

plt.tight_layout()
plt.show()


# ============================================================
# 2. VISUALIZATION 2
# AVERAGE YIELD BY CROP
# ============================================================

plt.figure(figsize=(10, 6))

yield_crop = (
    df.groupby("Crop")["Yield_Tonnes_Ha"]
    .mean()
    .sort_values(ascending=False)
)

sns.barplot(
    x=yield_crop.values,
    y=yield_crop.index
)

plt.title("Average Yield by Crop")
plt.xlabel("Average Yield (Tonnes/Ha)")
plt.ylabel("Crop")

plt.tight_layout()
plt.show()


# ============================================================
# 3. VISUALIZATION 3
# TOTAL PROFIT BY CROP
# ============================================================

plt.figure(figsize=(10, 6))

profit_crop = (
    df.groupby("Crop")["Profit_INR"]
    .sum()
    .sort_values(ascending=False)
)

sns.barplot(
    x=profit_crop.values,
    y=profit_crop.index
)

plt.title("Total Profit by Crop")
plt.xlabel("Total Profit (₹)")
plt.ylabel("Crop")

plt.tight_layout()
plt.show()


# ============================================================
# 4. VISUALIZATION 4
# PROFIT BY SEASON
# ============================================================

plt.figure(figsize=(8, 6))

profit_season = (
    df.groupby("Season")["Profit_INR"]
    .sum()
    .sort_values(ascending=False)
)

sns.barplot(
    x=profit_season.index,
    y=profit_season.values
)

plt.title("Total Profit by Season")
plt.xlabel("Season")
plt.ylabel("Total Profit (₹)")

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()


# ============================================================
# 5. VISUALIZATION 5
# IRRIGATION METHOD VS YIELD
# ============================================================

plt.figure(figsize=(9, 6))

sns.boxplot(
    data=df,
    x="Irrigation_Method",
    y="Yield_Tonnes_Ha"
)

plt.title("Yield Distribution by Irrigation Method")
plt.xlabel("Irrigation Method")
plt.ylabel("Yield (Tonnes/Ha)")

plt.xticks(rotation=20)

plt.tight_layout()
plt.show()


# ============================================================
# 6. VISUALIZATION 6
# RAINFALL VS YIELD
# ============================================================

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Rainfall_mm",
    y="Yield_Tonnes_Ha",
    alpha=0.6
)

plt.title("Rainfall vs Crop Yield")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Yield (Tonnes/Ha)")

plt.tight_layout()
plt.show()


# ============================================================
# 7. VISUALIZATION 7
# FUNDING / COST VS PROFIT
# ============================================================

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Total_Cost_INR",
    y="Profit_INR",
    alpha=0.6
)

plt.title("Total Cost vs Profit")
plt.xlabel("Total Cost (₹)")
plt.ylabel("Profit (₹)")

plt.tight_layout()
plt.show()


# ============================================================
# 8. VISUALIZATION 8
# PROFIT DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Profit_INR"],
    bins=30,
    kde=True
)

plt.title("Distribution of Farm Profit")
plt.xlabel("Profit (₹)")
plt.ylabel("Number of Farms")

plt.tight_layout()
plt.show()


# ============================================================
# 9. VISUALIZATION 9
# DISEASE / PEST RISK BY CROP
# ============================================================

plt.figure(figsize=(10, 6))

risk_crop = (
    df.groupby("Crop")["Disease_Pest_Risk_pct"]
    .mean()
    .sort_values(ascending=False)
)

sns.barplot(
    x=risk_crop.values,
    y=risk_crop.index
)

plt.title("Average Disease/Pest Risk by Crop")
plt.xlabel("Disease/Pest Risk (%)")
plt.ylabel("Crop")

plt.tight_layout()
plt.show()


# ============================================================
# 10. VISUALIZATION 10
# CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(14, 10))

numeric_df = df.select_dtypes(
    include=np.number
)

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    cmap="coolwarm",
    annot=False
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# ============================================================
# 11. SAVE CLEANED DATA
# ============================================================

df.to_excel(
    "Cleaned_Agriculture_Performance.xlsx",
    index=False
)

print("\n========== FILE SAVED ==========")

print(
    "Cleaned dataset saved as:",
    "Cleaned_Agriculture_Performance.xlsx"
)


# ============================================================
# 12. FINAL SUMMARY
# ============================================================

print("\n========== FINAL SUMMARY ==========")

print("Total Farms:", total_farms)

print(
    "Average Yield:",
    round(average_yield, 2),
    "Tonnes/Ha"
)

print(
    "Total Production:",
    round(total_production, 2),
    "Tonnes"
)

print(
    "Total Revenue: ₹",
    round(total_revenue, 2)
)

print(
    "Total Profit: ₹",
    round(total_profit, 2)
)

print(
    "Average Disease/Pest Risk:",
    round(average_disease_risk, 2),
    "%"
)

print("\n========== ANALYSIS COMPLETED ==========")

