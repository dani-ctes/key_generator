from cryptography.fernet import Fernet
import csv


with open('keys.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        csv_key = row[0]
        print('Key obtenida: ')
        print(Fernet(csv_key))

fernet = Fernet(csv_key)

message = 'some_text_to_encrypt'

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)
 
