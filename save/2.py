import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import PhoneNumberFormat

def read_numbers_from_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [line.strip() for line in file if line.strip()]
            return numbers
    except FileNotFoundError:
        print('file was not found.')
        return []

def save_number_to_contacts(phone_number):
    # اینجا می‌توانید کد خود را برای ذخیره شماره در مخاطبین اضافه کنید
    print(f"number {phone_number} Added to contacts.")

def process_phone_numbers(numbers):
    for number in numbers:
        try:
            parsed_number = phonenumbers.parse(number, "IR")  # تحلیل شماره تلفن با پیش‌شماره ایران
            formatted_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)

            # اینجا می‌توانید اطلاعات مربوط به شماره را بررسی و بر اساس نیاز اقدامات خود را انجام دهید
            print(f"number: {formatted_number}")
            print(f"area code: {phonenumbers.national_significant_number(parsed_number)}")
            print(f"Operator: {carrier.name_for_number(parsed_number, 'en')}")
            print(f"Area: {geocoder.description_for_number(parsed_number, 'en')}")
            print(f"Time zone: {timezone.time_zones_for_number(parsed_number)}")

            # ذخیره شماره در مخاطبین
            save_number_to_contacts(formatted_number)

        except phonenumbers.NumberParseException as e:
            print(f"Error in analyzing the number {number}: {e}")

# آدرس فایل متنی شامل شماره‌ها
file_path = 'contacts.txt'

# خواندن شماره‌ها از فایل متنی
numbers = read_numbers_from_txt(file_path)

# پردازش و ذخیره شماره‌ها در مخاطبین
process_phone_numbers(numbers)
