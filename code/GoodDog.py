from watchdog.events import FileSystemEventHandler
from icecream import  ic
from watchdog.observers import Observer
import time


class GoodDog(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_any_event(self, event):
        print(event)

    def on_created(self, event):
        ic("created!!!")
        if event.is_directory:
            print(f"dirctory  created:{event.src_path}")
        else:
            print(f"file created:{event.src_path}")

    def  on_deleted(self,event):
        if event.is_directory:
            print(f"dirctory deleted:{event.src_path}")
        else:
            print(f"file deleted:{event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            print(f"dirctory  modified: {event.src_path}")
        else:
            print(f"file modified: {event.src_path}")

    def on_moved(self,event):
        if event.is_directory:
            print(f"directory moved from {event.src_path}   to   {event.dest_path}")
        else:
            print(f"file moved from {event.src_path}   to   {event.dest_path}")


'''
if __name__=="__main__":
        observer = Observer()
        event_handler = FileEventHandler()
        # observer.schedule(event_handler,r"C:",recursive=True)
        observer.schedule(event_handler,r"D:\\",recursive=True)
        observer.schedule(event_handler,r"E:\\",recursive=True)
        observer.schedule(event_handler,r"F:\\",recursive=True)
        observer.start()
        ic("execute!!!")
        try:
            while True:
                time.sleep(0.2)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
'''