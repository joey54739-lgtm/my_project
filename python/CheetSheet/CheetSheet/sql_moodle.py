import sqlite3

# Connect to database
conn = sqlite3.connect('Phonebook1.db')
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "First Name" TEXT NOT NULL,
    "Last Name" TEXT NOT NULL,
    Phone_number INTEGER
)
""")
conn.commit()

# Function to view entire phonebook
def view_phonebook():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    if rows:
        print("\n--- Phonebook ---")
        for row in rows:
            print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Phone: {row[3]}")
    else:
        print("Phonebook is empty.")

# Function to add a new person
def add_person():
    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    phone = input("Enter Phone Number: ")
    cur.execute("INSERT INTO students('First Name', 'Last Name', Phone_number) VALUES(?, ?, ?)", (first, last, phone))
    conn.commit()
    print("Person added successfully!")

# Function to search by surname
def search_surname():
    surname = input("Enter Last Name to search: ")
    cur.execute("SELECT * FROM students WHERE 'Last Name' = ?", (surname,))
    rows = cur.fetchall()
    if rows:
        print("\n--- Search Results ---")
        for row in rows:
            print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Phone: {row[3]}")
    else:
        print("No record found with that surname.")

# Function to delete person by ID
def delete_person():
    try:
        id_to_delete = int(input("Enter ID of the person to delete: "))
        cur.execute("DELETE FROM students WHERE id = ?", (id_to_delete,))
        conn.commit()
        if cur.rowcount > 0:
            print("Person deleted successfully!")
        else:
            print("No record found with that ID.")
    except ValueError:
        print("Invalid ID! Please enter a number.")

# Main loop
while True:
    print("\n--- Main Menu ---")
    print("1. View phone book")
    print("2. Add to phone book")
    print("3. Search for surname")
    print("4. Delete person from phone book")
    print("5. Quit")
    
    choice = input("Enter your selection: ")
    
    if choice == "1":
        view_phonebook()
    elif choice == "2":
        add_person()
    elif choice == "3":
        search_surname()
    elif choice == "4":
        delete_person()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid selection! Please enter a number from 1 to 5.")

# Close connection
conn.close()
