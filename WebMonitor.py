from watchdog.observers import Observer
from watchdog.events import *
import MyConfig
import MyLogger


class monitor(FileSystemEventHandler):
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


if __name__ == '__main__':
    observer = Observer()
    eventHandler = monitor()
    observer.schedule(eventHandler, './test/', True)
    observer.start()
    print('Start Moniting!')
    observer.join()
