# 🏦 PDF to Excel Bank Statement Converter

This project is a **Python-based tool** to extract transaction data from PDF bank statements and convert it into a clean, structured **Excel file** for further analysis.

## 📌 Features
- Reads PDF bank statements using **pdfplumber**.
- Extracts transaction tables (date, description, debit, credit, balance).
- Cleans and formats:
  - Date columns into standard `dd-mm-yyyy` format.
  - Numeric columns (Debit, Credit, Balance) by removing unwanted symbols.
- Exports data to Excel using **openpyxl**.
- Works with multi-page PDFs.

---

## 🛠️ Technologies Used
- **Python 3**
- [pdfplumber](https://github.com/jsvine/pdfplumber) – Extracts tables from PDF.
- **pandas** – Data cleaning and formatting.
- **openpyxl** – Saves the data to Excel.

---

## 📂 Project Structure
