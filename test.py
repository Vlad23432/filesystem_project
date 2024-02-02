from path_root import MyPath
from datetime import datetime

file = "data\\alice.txt"
directory = "data"

file_path = MyPath(file)
directory_path = MyPath(directory)
# directory_path.rename('new_data')
print(file_path.get_size())
d = (file_path.get_mtime())
print(d)
print(datetime.fromtimestamp(d))