import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv('startup_funding.csv')

# Inspect
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------
# Data Cleaning
# ----------------------------

# Clean Amount in USD: remove commas and convert to float, non-numeric become NaN
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'].astype(str).str.replace(',', ''), errors='coerce')

# Fill missing Remarks
df['Remarks'] = df['Remarks'].fillna("No Remarks")

# Strip extra spaces in column names
df.columns = df.columns.str.strip()

# Fill missing cities and industry verticals if needed
df['City  Location'] = df['City  Location'].fillna("Unknown")
df['Industry Vertical'] = df['Industry Vertical'].fillna("Unknown")

# Convert Date to datetime
df['Date dd/mm/yyyy'] = pd.to_datetime(df['Date dd/mm/yyyy'], dayfirst=True, errors='coerce')

# ----------------------------
# EDA Plots
# ----------------------------

# Top 10 funded startups
top_startups = df.groupby('Startup Name')['Amount in USD'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,5))
top_startups.plot(kind='bar')
plt.title("Top 10 Funded Startups")
plt.ylabel("Funding Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Funding by City
funding_city = df.groupby('City  Location')['Amount in USD'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,5))
funding_city.plot(kind='bar')
plt.title("Top 10 Cities by Funding")
plt.ylabel("Funding Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top Industries by Funding
industry_funding = df.groupby('Industry Vertical')['Amount in USD'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,5))
industry_funding.plot(kind='bar')
plt.title("Top 10 Industries by Funding")
plt.ylabel("Funding Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top Investors by Total Funding
top_investors = df.groupby('Investors Name')['Amount in USD'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,5))
top_investors.plot(kind='bar')
plt.title("Top 10 Investors by Funding")
plt.ylabel("Funding Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Funding Over Time
funding_date = df.groupby('Date dd/mm/yyyy')['Amount in USD'].sum()
plt.figure(figsize=(12,5))
funding_date.plot()
plt.title("Funding Over Time")
plt.ylabel("Funding Amount (USD)")
plt.xlabel("Date")
plt.tight_layout()
plt.show()
