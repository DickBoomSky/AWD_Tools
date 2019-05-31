from watchdog.observers import Observer
from watchdog.events import *
import threading
import MyConfig
import MyLogger


class MyFileHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.log = MyLogger.MyLogger(filename=MyConfig.monitorlog, level='info')

    def on_created(self, event):
        if event.is_directory:
            self.log.logger.info('DireCreate %s', event.src_path)
        else:
            self.log.logger.info('FileCreate %s', event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            self.log.logger.info('DireModify %s', event.src_path)
        else:
            self.log.logger.info('FileModify %s', event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            self.log.logger.info('DireDelete %s', event.src_path)
        else:
            self.log.logger.info('FileDelete %s', event.src_path)

    def on_moved(self, event):
        if event.is_directory:
            self.log.logger.info('DireMoved %s', event.src_path)
        else:
            self.log.logger.info('FileMoved %s', event.src_path)


class MyFileMonitor(threading.Thread):

    def __init__(self, folder):
        threading.Thread.__init__(self)
        self.observer = Observer()
        self.eventHandler = MyFileHandler()
        self.observer.schedule(self.eventHandler, folder, True)
        self.__stop = False

    def run(self):
        print('Start Monitoring')
        self.observer.start()
        while True:
            if self.__stop:
                self.observer.stop()
                print('Stop Monitoring')
                break

    def stop(self):
        self.__stop = True


if __name__ == '__main__':
    monitor = MyFileMonitor('./test/')
    monitor.start()
    import time

    time.sleep(50)
    monitor.stop()
