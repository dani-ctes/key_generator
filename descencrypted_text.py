from cryptography.fernet import Fernet
import csv


with open('keys.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        csv_key = row[0]
        print('csv_key = ', csv_key)
        
        #print(Fernet(csv_key))

fernet = Fernet(csv_key)
print('Key obtenida: ', fernet)

text = b'gAAAAABi-_RlkSDyFgnUHNOZuZFMFMErcKmIFLWMIGrE1L68FgQIjFHRh-2KI4_12VFv02eog1k06b5k5QYDAL2bPlhjErTdfwC188YzThwmA_b94WJD3KY='



decMessage = fernet.decrypt(text).decode()
 
print("decrypted string: ", decMessage)