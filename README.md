
# Secure File Management System

## Features

### LoginPage:
A login dialog that authenticates users. There are two roles: admin and user, with different privileges.

### FileSharingServer:
Handles file operations like:
- Encrypting and decrypting files using `cryptography.fernet.Fernet`.
- Uploading and downloading files with optional compression.
- Logging actions to `actions.txt`.
- Listing uploaded and encrypted files.

### MainWindow:
Main interface for users to:
- Upload, download, list files, and view previous actions.
- Admins can view encrypted files.

### Compression & Decompression:
Files are compressed if they exceed 1KB before uploading, and decompressed during download if applicable.

### File Content Extraction:
Supports text extraction from:
- PDF
- Word (.docx)
- PowerPoint (.pptx)
- Images (.jpg, .jpeg, .png)
- Plain text files

## Improvements/Considerations
- Error handling for login failures, file issues, etc.
- Encryption with Fernet provides solid security.
- Supports multiple file formats.
- Role-based access: Admins have extra privileges.

## Next Steps
- Add file integrity checks.
- Enhance UI with previews and progress updates.
- Implement file versioning or backup support.

## Disclaimer
This is a prototype and does **not** implement actual client-server socket programming. Network file sharing would need further enhancements.

## Repository
[SecureFileSystem GitHub Repository](https://github.com/joannjoseph23/SecureFileSystem)
