## **FEATURES:**
## LoginPage: 
A login dialog that authenticates users. There are two roles: admin and user, with different privileges.
## FileSharingServer: 
A class that handles file operations like:
Encrypting and decrypting files with cryptography.fernet.Fernet.
Uploading and downloading files with compression options.
Logging actions to a file (actions.txt).
Listing uploaded and encrypted files.
## MainWindow: 
The main window of the application, where users can upload, download, list files, and view previous actions. It also provides admin functionality to view encrypted files.

**Compression & Decompression:**
Before uploading, files are compressed if they exceed a certain size. When downloading, files can be decompressed.
File Content Extraction: 
The application can read various file types (PDF, Word, PowerPoint, images) and extract text from them.

## **Improvements/Considerations:**
Error Handling: There's error handling for cases like invalid file paths, decompression issues, and login failures, which is good for ensuring the stability of the application.

Security: File encryption is done using cryptography.fernet.Fernet which is a solid choice for symmetric encryption.

File Formats: The app supports multiple file formats such as .pdf, .docx, .pptx, .jpg, .jpeg, .png, and plain text files.

Admin Role: Admin users have additional privileges, including the ability to view encrypted files.

## **Next Steps:**
File Validation: You may want to add checks to validate the integrity of files before uploading or downloading.

Enhanced UI: You could further enhance the UI by adding file previews before uploads, progress updates for downloads, and better feedback to users during long processes.

Expand Functionality: Consider adding file versioning or automatic backup features for better management of files.


## Disclaimer

This project is a prototype model and does not implement actual client-server socket programming for distributed file sharing. Further enhancements would be required to enable file transfer between different computers over a network.


