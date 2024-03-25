try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("Line 2: 42 is the answer.\n")
        file.write("Line 3: Python is awesome!\n")
    print("File 'my_file.txt' created and initial content written successfully.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("\nContent of 'my_file.txt':")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1: Appended content.\n")
        file.write("Additional line 2: Hello, world!\n")
        file.write("Additional line 3: Python file handling is cool!\n")
    print("\nAdditional content appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to open the file.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
finally:
    print("Script execution complete.")