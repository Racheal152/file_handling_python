def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()
        modified_content = content.upper()
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content) 

        print(f"File has been successfully modified and saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_filename = input("Enter the filename to read: ")
output_filename = input("Enter the filename to save the modified content: ")

read_and_write_file(input_filename, output_filename)
