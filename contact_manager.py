import csv
import json
import sqlite3
from openpyxl import Workbook

# Sample data
contacts = [
    {"name": "Alice", "phone": "1234567890", "email": "alice@example.com"},
    {"name": "Bob", "phone": "0987654321", "email": "bob@example.com"},
]

# --- 1. Save to Text File ---
def save_to_txt():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

# --- 2. Save to CSV File ---
def save_to_csv():
    with open("contacts.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(contacts)

# --- 3. Save to JSON File ---
def save_to_json():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# --- 4. Save to Excel File ---
def save_to_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Contacts"
    ws.append(["Name", "Phone", "Email"])
    for contact in contacts:
        ws.append([contact["name"], contact["phone"], contact["email"]])
    wb.save("contacts.xlsx")

# --- 5. Save to SQLite Database ---
def save_to_sqlite():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            email TEXT
        )
    ''')
    for contact in contacts:
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                       (contact["name"], contact["phone"], contact["email"]))
    conn.commit()
    conn.close()

# --- Main Call ---
if __name__ == "__main__":
    save_to_txt()
    save_to_csv()
    save_to_json()
    save_to_excel()
    save_to_sqlite()
    print("Contacts saved to all formats.")
