import os

def file_read_write_challenge():
    """Challenge 1: Read a file and write a modified version to a new file"""
    print("\nFile Read & Write Challenge")
    print("--------------------------")
    
    try:
        # Get input file name from user
        input_file = input("Enter the name of the file to read: ")
        
        # Read the original file
        with open(input_file, 'r') as file:
            content = file.read()
            print(f"\nOriginal content:\n{content}")
        
        # Create output file name
        base_name, ext = os.path.splitext(input_file)
        output_file = f"{base_name}_modified{ext}"
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"\nModified content has been written to: {output_file}")
        print(f"Modified content preview:\n{modified_content[:200]}...")  # Show first 200 chars
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def error_handling_lab():
    """Challenge 2: Ask for filename and handle potential errors"""
    print("\nError Handling Lab")
    print("-----------------")
    
    while True:
        filename = input("\nEnter a filename to check (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            break
        
        try:
            # Check if file exists
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' does not exist.")
            
            # Check if file is readable
            if not os.access(filename, os.R_OK):
                raise PermissionError(f"No read permissions for '{filename}'.")
            
            # Try to open the file
            with open(filename, 'r') as file:
                first_line = file.readline()
                print(f"\nFile exists and is readable!")
                print(f"First line preview: {first_line.strip()}")
                
        except FileNotFoundError as e:
            print(f"Error: {str(e)}")
        except PermissionError as e:
            print(f"Error: {str(e)}")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        else:
            # If no exceptions occurred, offer to read the whole file
            read_full = input("Would you like to see the full content? (y/n): ").lower()
            if read_full == 'y':
                with open(filename, 'r') as file:
                    print("\nFile content:")
                    print(file.read())

def main():
    print("File Handling and Exception Handling Assignment")
    print("==============================================")
    
    while True:
        print("\nMenu:")
        print("1. File Read & Write Challenge")
        print("2. Error Handling Lab")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            file_read_write_challenge()
        elif choice == '2':
            error_handling_lab()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
