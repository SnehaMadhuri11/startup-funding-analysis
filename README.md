# Startup Funding Analysis - Exploratory Data Analysis (EDA)

## Overview
This project performs **Exploratory Data Analysis (EDA)** on Indian startup funding data. The goal is to clean the data, analyze funding trends, and visualize insights like:

- Top funded startups  
- Cities attracting the most funding  
- Industries receiving the most investment  
- Top investors  
- Funding trends over time  

The dataset used is `startup_funding.csv`.

---

## Dataset Description

The dataset contains **3044 funding records** with **10 columns**:

| Column | Description |
|--------|-------------|
| `Sr No` | Serial number of the record |
| `Date dd/mm/yyyy` | Date of the funding round (dd/mm/yyyy format) |
| `Startup Name` | Name of the startup |
| `Industry Vertical` | Industry category (e.g., E-commerce, Fintech, Healthcare) |
| `SubVertical` | More specific category (e.g., Online Education under EdTech) |
| `City  Location` | City where the startup is located |
| `Investors Name` | Name of investor or investment firm |
| `InvestmentnType` | Type of investment (Seed, Venture Capital, etc.) |
| `Amount in USD` | Funding amount in USD (some values may be undisclosed) |
| `Remarks` | Additional notes/comments |

**Key Observations:**

- Most funding is concentrated among a few startups.  
- Bangalore, Mumbai, and Delhi are the top cities.  
- Industries like E-commerce, Fintech, and Healthcare dominate funding.  
- Top investors include Sequoia Capital, Accel, and Tiger Global.  

---

## Features / Functionality

1. **Data Loading & Inspection**
   - Reads the CSV file into a Pandas DataFrame.  
   - Displays data shape, column names, data types, and missing values.  

2. **Data Cleaning**
   - Converts `Amount in USD` to numeric, replacing non-numeric values with NaN.  
   - Fills missing `Remarks` with `"No Remarks"`.  
   - Handles missing cities and industries.  
   - Converts date column to proper datetime format.  

3. **Exploratory Data Analysis (EDA)**
   - Top 10 funded startups.  
   - Top 10 cities by total funding.  
   - Top 10 industries by funding.  
   - Top 10 investors by funding.  
   - Funding trends over time (daily).  

4. **Data Visualization**
   - Bar charts for startups, cities, industries, and investors.  
   - Line chart for funding over time.  

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/Snehamadhuri11/startup-funding-analysis.git

