from Crypto.Cipher import AES
from Crypto.Hash import SHA256  # Fixed incorrect import (SHA265 → SHA256)
import os
from random import randint

def decrypt_file(key, 'EMW'):
    chunksize = 65536
    outputfile, ext = os.path.splitext('EMW'[:-11])  # Restore original filename

    with open('EMW', 'rb') as infile:
        ext = infile.read(16).decode().strip()  # Read and clean file extension
        filesize = int(infile.read(16).decode().strip())  # Read original file size
        IV = infile.read(16)  # Read the Initialization Vector
        
        decryptor = AES.new(key, AES.MODE_CBC, IV)  # Fixed incorrect mode (CNC → CBC)

        with open(outputfile + ext, 'wb') as outfile:  # Append original extension
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)  # Restore original file size

    os.unlink('EMW')  # Remove encrypted file
