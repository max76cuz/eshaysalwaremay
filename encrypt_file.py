from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from random import randint
import os

def encrypt_file(key, 'EMW'):
    chunksize = 65536
    ext = os.path.splitext('EMW')[1]  # Get the original file extension
    ext += ' ' * (16 - (len(ext) % 16))  # Pad extension to 16 bytes
    outputfile = 'EMW.EMA'  # Fixed output file name
    filesize = str(os.path.getsize('EMW')).zfill(16)
    IV = ''.join(chr(randint(0, 255)) for _ in range(16))

    encryptor = AES.new(key, AES.MODE_CBC, IV)
    
    with open('EMW', 'rb') as infile:
        with open(outputfile, 'wb') as outfile:
            outfile.write(ext.encode())  # Write padded extension
            outfile.write(filesize.encode())  # Write file size
            outfile.write(IV.encode())  # Write IV

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))  # Pad chunk to 16 bytes
                outfile.write(encryptor.encrypt(chunk))
    
    os.unlink('EMW')  # Delete the original file
