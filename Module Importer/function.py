
def display_file_content(filename):
    try:
        with open(data, 'r') as file:
            content = file.read()
            print(f"File content of {data}:")
            print(content)
    except FileNotFoundError:
        print(f"File '{data}' not found.")
    except IOError:
        print(f"Error reading file '{data}'.")
display_file_content('data.txt')

display_file_content('data.txt')
