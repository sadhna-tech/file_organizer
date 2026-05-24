import os
import shutil

# Folder path
path = input("Enter folder path: ")

# File type folders
folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Python Files": [".py"]
}

# Create folders if not exist
for folder_name in folders:
    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Check extension
    _, extension = os.path.splitext(file)

    moved = False

    for folder_name, extensions in folders.items():
        if extension.lower() in extensions:
            destination = os.path.join(path, folder_name, file)

            shutil.move(file_path, destination)

            print(f"Moved: {file} → {folder_name}")

            moved = True
            break

    if not moved:
        print(f"Skipped: {file}")

print("\nFiles organized successfully!")