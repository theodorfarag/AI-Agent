from functions.get_files_info import get_files_info



def test_get_files_info(workingDirectory, directory):
    return get_files_info(workingDirectory, directory)

def main():
    print(test_get_files_info("calculator", "."))
    print(test_get_files_info("calculator", "pkg"))
    print(test_get_files_info("calculator", "/bin"))
    print(test_get_files_info("calculator", "../"))


if __name__ == "__main__":
    main()