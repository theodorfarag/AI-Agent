import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        res_directory = "current" if directory == "." or directory == "./" else f"'{directory}'"
        res = f"Result for {res_directory} directory:\n"    
        working_dir_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
        if not os.path.exists(target_dir):
            return f'Error: "{directory}" is not a directory\n'

        with os.scandir(target_dir) as entries:
            for entry in entries:
                res += f"- {entry.name}: file_size={os.path.getsize(os.path.normpath(target_dir +"/"+ entry.name))} bytes, is_dir={entry.is_dir()}\n"
        
    except Exception as e:
        return f"Error: {e}\n"



    return res 


def main():
    print(get_files_info("calculator"))

if __name__ == "__main__":
    main()