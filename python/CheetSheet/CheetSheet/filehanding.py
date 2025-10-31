# ================= Superheat File Handling Cheatsheet =================

import os

# ---------------- 1️⃣ Create / Overwrite File ----------------
# 'w' mode creates the file if not exists, overwrites if exists
with open("example.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("Python File Handling Cheatsheet\n")
# File is automatically closed when using 'with'

# ---------------- 2️⃣ Append Data ----------------
# 'a' mode adds data at the end
with open("example.txt", "a") as f:
    f.write("Appending new line 1\n")
    f.write("Appending new line 2\n")

# ---------------- 3️⃣ Read Entire File ----------------
with open("example.txt", "r") as f:
    content = f.read()  # Reads entire file as a single string
print("\n--- Entire File ---")
print(content)

# ---------------- 4️⃣ Read Line by Line ----------------
with open("example.txt", "r") as f:
    print("\n--- Line by Line ---")
    for line in f:
        print(line.strip())  # .strip() removes newline

# ---------------- 5️⃣ Read Specific Number of Characters ----------------
with open("example.txt", "r") as f:
    print("\n--- Read 5 Characters ---")
    print(f.read(5))  # reads first 5 characters
    print(f.read(5))  # next 5 characters

# ---------------- 6️⃣ File Pointer & Seek ----------------
with open("example.txt", "r") as f:
    print("\n--- File Pointer Example ---")
    print(f.read(5))  # Hello
    print("Pointer now at:", f.tell())
    f.seek(0)         # Move pointer to start
    print(f.read())   # Read full file again

# ---------------- 7️⃣ Read into List ----------------
with open("example.txt", "r") as f:
    lines = f.readlines()  # returns a list of lines
print("\n--- Lines List ---")
print(lines)

# ---------------- 8️⃣ Working with Binary Files ----------------
# Example: reading an image (binary)
# with open("image.png", "rb") as f:
#     data = f.read()
#     print(type(data))  # <class 'bytes'>

# ---------------- 9️⃣ Delete File ----------------
# os.remove("example.txt")  # Uncomment to delete file

# ---------------- 🔟 Rename File ----------------
# os.rename("example.txt", "example_renamed.txt")  # Uncomment to rename

# ---------------- 1️⃣1️⃣ Handle Exceptions ----------------
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nFile does not exist!")

# ---------------- 1️⃣2️⃣ Interactive Phonebook Example ----------------
# One file, everything in one, like a real cheat sheet

filename = "phonebook.txt"

# Create / overwrite
with open(filename, "w") as f:
    f.write("ID,First Name,Last Name,Phone\n")

# Add sample records (like insert)
records = [
    "1,Parth,Shringarpure,1234567890\n",
    "2,Alice,Smith,9876543210\n",
    "3,Bob,Johnson,5555555555\n"
]
with open(filename, "a") as f:
    f.writelines(records)

# View all records
with open(filename, "r") as f:
    print("\n--- Phonebook ---")
    for line in f:
        print(line.strip())

# Search by last name
search = "Smith"
print(f"\n--- Search Results for Last Name: {search} ---")
with open(filename, "r") as f:
    for line in f:
        if search.lower() in line.lower().split(",")[2]:
            print(line.strip())

# Delete a record by ID
del_id = "2"
with open(filename, "r") as f:
    lines = f.readlines()
with open(filename, "w") as f:
    for line in lines:
        if line.split(",")[0] != del_id:
            f.write(line)
print(f"\nRecord with ID {del_id} deleted.")

# View updated phonebook
with open(filename, "r") as f:
    print("\n--- Updated Phonebook ---")
    for line in f:
        print(line.strip())

# ---------------- 1️⃣3️⃣ Notes / Cheat Concepts ----------------
"""
File Modes: r, w, a, x, b, + 
with open(file, mode) as f → auto-close
f.read() → full file
f.readline() → one line
f.readlines() → list of lines
f.write(data) → write/append
f.tell() → pointer position
f.seek(pos) → move pointer
os.remove(file) → delete
os.rename(old, new) → rename
Try/Except → handle file errors
"""

# ===================== END OF FILE HANDLING CHEATSHEET =====================
