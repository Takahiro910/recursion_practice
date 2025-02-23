import os
import sys



def reverse(inputPath, outputPath):
    if not os.path.exists(inputPath):
        raise FileNotFoundError(f'Input file not found: {inputPath}')
    with open(inputPath) as f:
        contents = f.read()
    with open(outputPath, 'w') as f:
        f.write(contents[::-1])

def copy(inputPath, outputPath):
    if not os.path.exists(inputPath):
        raise FileNotFoundError(f'Input file not found: {inputPath}')
    with open(inputPath, 'r') as f:
        contents = f.read()
    with open(outputPath, 'w') as f:
        f.write(contents)

def duplicate_contents(inputPath, n):
    if not os.path.exists(inputPath):
        raise FileNotFoundError(f'Input file not found: {inputPath}')
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    with open(inputPath, 'r') as f:
        contents = f.read()
        dupricated = contents * n
        f.seek(0)
        f.write(dupricated)
        f.truncate()

def replace_string(inputPath, needle, newString):
    if not os.path.exists(inputPath):
        raise FileNotFoundError(f'Input file not found: {inputPath}')
    with open(inputPath, 'r+') as f:
        contents = f.read()
        replaced = contents.replace(needle, newString)
        f.seek(0)
        f.write(replaced)
        f.truncate()

def validate_args(command, args):
    if command == "reverse" or command == "copy":
        if len(args) != 2:
            raise ValueError(f"Usage: {command} inputpath outputpath")
    elif command == "dupricate_contents":
        if len(args) != 2:
            raise ValueError(f"Usage: {command} inputpath n")
        try:
            int(args[1])
        except ValueError:
            raise ValueError(f"n must be an integer")
    elif command == "replace_string":
        if len(args) != 3:
            raise ValueError(f"Usage: {command} inputpath needle newstring")
    else:
        raise ValueError(f"Unknown command: {command}")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_manipulator.py <command> <args>")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    try:
        validate_args(command, args)
        if command == "reverse":
            reverse(args[0], args[1])
        elif command == "copy":
            copy(args[0], args[1])
        elif command == "duplicate-contents":
            duplicate_contents(args[0], int(args[1]))
        elif command == "replace-string":
            replace_string(args[0], args[1], args[2])
        print("Operation successful.")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
        sys.exit(1)