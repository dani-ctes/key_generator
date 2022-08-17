from cryptography.fernet import Fernet
import csv


key = Fernet.generate_key()

with open('keys.csv', 'w+') as f:
    headers = ['key']
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerow({'key': key.decode('utf-8')})