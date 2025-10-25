import os
from fileinput import filename


def readFile(filename):
    try:
        current_path = os.path.join(os.getcwd(), __file__)
        with open(os.path.join(current_path,filename), 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: The file '{0}' was not found.".format(filename))
    except PermissionError:
        print("Error: You do not have permission to read the file '{0}'.".format(filename))
    except ValueError:
        print("Error: Invalid value encountered while reading the file '{0}'.".format(filename))
    except Exception as e:
        print("An unexpected error occurred: ", str(e))



def get_filename_from_user():
    # current file path
    current_path = os.path.join(os.getcwd(), __file__)
    print("Hello you are currently on this path {0}, which file do you want to read?".format(current_path))
    return input("Please enter the file name: ")

if __name__ == "__main__":
    filename = get_filename_from_user()
    readFile(filename)
