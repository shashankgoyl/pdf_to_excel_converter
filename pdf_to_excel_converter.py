import pdfplumber
import pandas as pd
import re

# File paths
pdf_path = r"sample_bank_statement.pdf"
output_excel = r"BankStatementAnalysis.xlsx"

# Initialize list for transactions
transactions = []

# Extract tables from PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            # Skip header rows if detected
            for row in table[1:]:  # Assuming first row is header
                if len(row) >= 7:  # Expect 7 columns
                    # Handle potential merged cells or missing values
                    row = [str(cell) if cell is not None else "" for cell in row]
                    transactions.append(row[:7])  # Txn Date, Value Date, Description, Ref No., Debit, Credit, Balance

# Create DataFrame
headers = ["Txn Date", "Value Date", "Description", "Ref No./Cheque No.", "Debit", "Credit", "Balance"]
df = pd.DataFrame(transactions, columns=headers)

# Clean numeric columns
for col in ["Debit", "Credit", "Balance"]:
    df[col] = df[col].astype(str).str.replace("[^0-9.]", "", regex=True)
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# Clean date columns
df["Txn Date"] = pd.to_datetime(df["Txn Date"], errors="coerce", dayfirst=True)
df["Value Date"] = pd.to_datetime(df["Value Date"], errors="coerce", dayfirst=True)

# Save to Excel
df.to_excel(output_excel, index=False, engine="openpyxl")
print(f"Excel file saved as: {output_excel}")