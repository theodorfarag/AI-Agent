import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_path = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(abs_path, file_path))
        valid_path = os.path.commonpath([abs_path, target_file_path]) == abs_path

        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file_path, 'r') as file:
            file_content = file.read(MAX_CHARS)
            if file.read(1):
                file_content += f'[...File "{file_path} truncated at {MAX_CHARS} characters"]'
    except Exception as e:
        return f"Error: {e}"
    return file_content
    
def main():
    print(get_file_content("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()