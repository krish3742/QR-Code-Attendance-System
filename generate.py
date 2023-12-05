import csv
from MyQR import myqr 
import os 

# Sample data to be written to the CSV file
data = [
    {"Name": "Anirudh Kumar", "ID": "20SCSE1010801"},
    {"Name": "Aman Rathor", "ID": "20SCSE1010865"},
    {"Name": "Sakshi Pandey", "ID": "20SCSE1010812"},
    {"Name": "Saket Lal", "ID": "20SCSE1010833"},
    # Add more data entries as needed
]

# Define the filename for the CSV file
csv_filename = 'students.csv'

# Writing data to the CSV file
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "ID"])

    # Write header
    writer.writeheader()

    # Write data rows
    for student in data:
        writer.writerow(student)

print(f"CSV file '{csv_filename}' created successfully.")

# Read data from CSV file
save_dir = os.path.join(os.getcwd(), 'QR_codes')

# Create the folder if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Read data from the CSV file and generate QR codes
with open(csv_filename, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Skip empty rows
        if not row['ID'].strip():
            continue

        qr_data = f"{row['Name']} {row['ID']}"
        version, level, qr_name = myqr.run(
            qr_data,
            level='H',
            version=1,
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name = f"{row['Name']}_{row['ID']}.bmp" ,
            save_dir=save_dir
        )