import tkinter as tk
from tkinter import filedialog
import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberFormat

def save_contacts(phone_numbers):
    for number in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number, "IR")
            formatted_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)

            # اینجا می‌توانید کد خود را برای ذخیره شماره در مخاطبین اضافه کنید
            print(f"Saving number {formatted_number} to contacts.")
        except phonenumbers.NumberParseException as e:
            print(f"Error in analyzing the number {number}: {e}")

def read_phone_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [line.strip() for line in file if line.strip()]
            return numbers
    except FileNotFoundError:
        print('File not found.')
        return []

def select_file():
    file_path = filedialog.askopenfilename(title="Select TXT file", filetypes=[("Text files", "*.txt")])
    if file_path:
        phone_numbers = read_phone_numbers_from_file(file_path)
        save_contacts(phone_numbers)

# ساخت پنجره اصلی
root = tk.Tk()
root.title("Contact List App")

# اضافه کردن یک دکمه برای انتخاب فایل
select_file_button = tk.Button(root, text="Select TXT File", command=select_file)
select_file_button.pack(pady=20)

# اجرای پنجره
root.mainloop()
