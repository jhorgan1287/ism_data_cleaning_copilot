
## 🧹 What the Script Does

The `data_cleaning.py` script performs the following steps:

1. **Loads** the raw sales CSV file  
2. **Standardizes column names** (lowercase, underscores, no extra spaces)  
3. **Strips whitespace** from text fields  
4. **Handles missing values** for price and quantity  
5. **Removes invalid rows** with negative numbers  
6. **Saves the cleaned dataset** to `data/processed/sales_data_clean.csv`

These steps ensure the dataset is consistent, usable, and ready for analysis.

## 🚀 How to Run the Script

From the project’s root folder, run:

```bash
python src/data_cleaning.py
