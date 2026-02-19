import os
import shutil


def copy_directory(source, destination):

    if os.path.exists(destination):
        print(f"Deleting: {destination}")
        shutil.rmtree(destination)

    print(f"Creating {destination}")
    os.makedirs(destination)

    items = os.listdir(source)

    for item in items:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            print(f"Copying {source_path} to {destination_path}")
            shutil.copy2(source_path, destination_path)

        elif os.path.isdir(source_path):
            print(f"Copying directory {source_path} to {destination_path}")
            copy_directory(source_path, destination_path)