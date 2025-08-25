
# File Read & Write Challenge 🖋️ + Error Handling Lab 🧪

This project demonstrates how to work with files in Python:
- Reading and writing files
- Modifying file content
- Creating new files with updated content
- Handling errors when working with files

---

## 🚀 Features
1. **File Read & Write Challenge**
   - Reads content from an existing file (`file-test.txt`)
   - Appends a string to the content
   - Saves the modified content into a new file (`file-test-modified.txt`)
   - Prints the modified content to the terminal

2. **Error Handling Lab**
   - Prompts the user to enter a filename
   - Attempts to open and read the file
   - Handles possible errors gracefully:
     - `FileNotFoundError` → File does not exist
     - `PermissionError` → File exists but user does not have permission
     - Any other unexpected errors

---

## 📂 File Structure
```

python-week4/
│── file-read-and-write.py   # Main Python script
│── file-test.txt            # Sample input file
│── file-test-modified.txt   # Output file with modified content
│── README.md                # Documentation

````

---

## 💻 Usage

### 1. Run the Script
```bash
python file-read-and-write.py
````

### 2. Example Workflow

* The script reads from `file-test.txt`
* Creates a new file `file-test-modified.txt` with extra text appended
* Then it asks you to enter any filename:

  * If the file exists → its content is displayed
  * If not → you get a helpful error message

---

## 📝 Example

**file-test.txt**

```
Hello World
This is the original file.
```

After running the script:

**file-test-modified.txt**

```
Hello World
This is the original file.
This is appended to the file
```

---

## ⚠️ Error Handling Examples

* If you enter a file that doesn’t exist:

```
Please Enter the file name: missing.txt
File not found. Please check the filename.
```

* If you try to open a file without permissions:

```
Please Enter the file name: restricted.txt
You don’t have permission to read this file.
```

---

## 🛠️ Requirements

* Python 3.x

No external dependencies are required.

---

## 📜 License

This project is for learning purposes and has no specific license.
