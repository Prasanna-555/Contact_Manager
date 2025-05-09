📇 Contact Manager (Python)

A mini contact manager project in Python that demonstrates saving and loading contact data in multiple formats: **Text, CSV, JSON, Excel, and SQLlite.

📁 Project Structure
contact_manager/

*contact_manager.py     # Main script
*contacts.txt           # Text file storage
*contacts.csv           # CSV file storage
* contacts.json          # JSON file storage * contacts.xlsx          # Excel file storage
*contacts.db            # SQLite database
 💡 Features
- Save contacts to:
  - 📄 `.txt` – Plain text file (comma-separated)
  - 📋 `.csv` – Standard CSV format
  - 🧾 `.json` – Structured JSON
  - 📊 `.xlsx` – Excel file using `openpyxl`
  - 🗃️ `.db` – SQLite database

- Sample contact data is hard-coded for demonstration.
 🛠️ Technologies Used

- Python 3.7.0
- Built-in modules: `csv`, `json`, `sqlite3`
- External module: `openpyxl` *(for Excel support)*
 🚀 How to Run

1. Make sure Python is installed.
2. Install required library:
   ```bash
   pip install openpyxl

