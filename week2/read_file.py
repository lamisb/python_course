import os
from fileinput import filename

def readFile(filename):
    try:
        with open(os.path.join(os.getcwd(),filename), 'r') as file:
            content = file.read()
            if(content.strip() == ""):
                raise ValueError("The file is empty.")
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: The file '{0}' was not found.".format(filename))
    except PermissionError:
        print("Error: permission denied to read '{0}'.".format(filename))
    except ValueError:
        print("Error: There was an issue processing the file content '{0}'.".format(filename))
    except Exception as e:
        print("An unexpected error occurred: ", str(e))

def get_filename_from_user():
    # current file path
    current_path = os.getcwd()
    print("Hello you are currently on this path {0}, which file do you want to read?".format(current_path))
    return input("Please enter the file name: ")

if __name__ == "__main__":
    filename = get_filename_from_user()
    readFile(filename)
