
def display_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError:
        print(f"Error reading file '{filename}'.")
display_file_content('filename.txt')

