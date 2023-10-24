from datetime import datetime
import os

desktop_path = os.path.expanduser("~\\Desktop")
file_path = os.path.join(desktop_path, "text.txt")

with open(file_path, 'w') as file:
    file.write(str(datetime.now()))

raise RuntimeError("Oh no")
