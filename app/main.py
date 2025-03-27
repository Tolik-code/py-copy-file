import shutil


def copy_file(command: str) -> None:
    try:
        source_file_name, target_file_name = command[3:].split(" ")

        try:
            if source_file_name != target_file_name:
                shutil.copyfile(source_file_name, target_file_name)
        except FileNotFoundError:
            print(f"Not found file with name: {source_file_name}")

    except ValueError:
        print(f"Cannot parse file names from command: {command}")
