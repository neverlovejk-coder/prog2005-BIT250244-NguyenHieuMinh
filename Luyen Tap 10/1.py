import os
def get_full_filename(path):
    return os.path.basename(path)
def get_song_name_only(path):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]
path = "d:\\music\\Hoang mang - Ho Quynh Huong.mp3"
print(f"ten : {get_full_filename(path)}")
print(f"ten bai hat: {get_song_name_only(path)}")