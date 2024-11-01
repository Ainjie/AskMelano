import os

# Specify the directory where your photos are located
directory = directory = r"C:\Users\ainji\OneDrive\Desktop\AskMelano\train\benign"

for filename in os.listdir(directory):
    if filename.startswith("melanoma"):
        new_name = filename.replace("melanoma", "benign", 1)
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")

print("All files renamed successfully!")
