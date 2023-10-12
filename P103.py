import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

source = "/Users/poornimaponnuswamy/Downloads"
destination = "/Users/poornimaponnuswamy/Desktop"


# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path}has been created!")
    
    def on_deleted(self,event):
        print(f"Oops! Someone deleted{event.src_path}!")

    def on_moved(self,event):
        print(f"Oops! Someone moved{event.src_path}!")
    def on_modified(self,event):
        print(f"Oops! Someone modified{event.src_path}!")

    
               

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except  ZeroDivisionError:
    print("stopped")
    observer.stop()
    