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

text = b'gAAAAABjDY49F4NG5PBig81pzZrqIAQ_JCscTDhfRPNtOC6kjDIZzcK5Gl-kprLvPp47zIKM3oWLa0PkGUJUJ-RL3fqhIHAtEHBOmO5zXD_3WB6HzzKIm7E='



decMessage = fernet.decrypt(text).decode()
 
print("decrypted string: ", decMessage)