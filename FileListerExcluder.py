import os
files = []
for i in os.listdir():
    if i == "FileListerExcluder.py":
        continue
    files.append(i)
print(files)
