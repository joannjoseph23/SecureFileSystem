import os

ENCRYPTED_FOLDER = "encrypted"

# Check if the folder exists, if not, create it
if not os.path.exists(ENCRYPTED_FOLDER):
    os.makedirs(ENCRYPTED_FOLDER)

# Print the absolute path to the folder
print(f"The absolute path to the 'ENCRYPTED_FOLDER' is: {os.path.abspath(ENCRYPTED_FOLDER)}")
