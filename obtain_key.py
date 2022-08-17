from cryptography.fernet import Fernet
import csv


with open('keys.csv') as f:
    reader = csv.reader(f)


    for row in reader:
        csv_key = row[0]
        print(Fernet(csv_key))

