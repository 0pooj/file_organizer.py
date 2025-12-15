import os
import shutil

# Get the folder path from the user
path = input("Enter the folder path: ")

# Define file types and corresponding folders
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"]
}

# 1. Create the required folders first
print("Creating required folders...")
for folder in file_types:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 2. Iterate through files and move them
print("Sorting and moving files...")
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    # Ensure it is a file, not a folder
    if os.path.isfile(file_path):
        # Extract the file extension (convert to lowercase)
        extension = os.path.splitext(file)[1].lower()

        # Find the matching folder and move the file
        for folder, extensions in file_types.items():
            if extension in extensions:
                try:
                    # Build the destination path and move
                    destination_path = os.path.join(path, folder, file)
                    shutil.move(file_path, destination_path)
                    print(f"Moved: {file} to {folder}/")
                    break # Move to the next file after successful move
                except Exception as e:
                    print(f"Failed to move file {file}: {e}")
