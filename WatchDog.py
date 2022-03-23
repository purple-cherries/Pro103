import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/vkaun/Downloads"
destination = "C:/Users/vkaun/Downloads/images"
tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], 
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in tree.items():
            time.sleep(1)
            if extension in value:
                fileName = os.path.basename(event.src_path)
                print('Downloaded ' + fileName)
                path1 = source + '/' + fileName
                path2 = destination + "/" + key
                path3 = destination + '/' + key + '/' + fileName
                if os.path.exists(path2):
                    print('Moving ' + fileName)
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    print('Moving ' + fileName)
                    shutil.move(path1, path3)
                    time.sleep(1)
                    
eventHandler = FileMovementHandler()
observer = Observer()
observer.schedule(eventHandler,source, recursive = True)
observer.start()

try: 
    while True : 
        time.sleep(2)
        print('Running...')
except KeyboardInterrupt:
    print('Stopped')
    observer.stop()

