from watchdog.events import FileSystemEvent
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import shutil
from os import listdir
from os.path import join, isfile
import time

download_folder_path = "E:\Downloads"

def check_in_use(path):
    try:
        os.rename(path, path)
        return False
    except:
        return True

class Organizer(FileSystemEventHandler):
    types_map = {
        '.pdf' : f'{download_folder_path}\PDFs',
        '.txt' : f'{download_folder_path}\Text Files',
        '.xlsx' : f'{download_folder_path}\Excel Files',
        '.xls' : f'{download_folder_path}\Excel Files',
        '.docx' : f'{download_folder_path}\Word Files',
        '.doc' : f'{download_folder_path}\Word Files',
        '.jpg' : f'{download_folder_path}\Images',
        '.png' : f'{download_folder_path}\Images',
        '.zip' : f'{download_folder_path}\RAR and ZIP files',
        '.rar' : f'{download_folder_path}\RAR and ZIP files',
        '.mp3' : f'{download_folder_path}\Audios',
        '.mp4' : f'{download_folder_path}\Videos',
        '.pptx' : f'{download_folder_path}\PowerPoint Files',
        '.ppt' : f'{download_folder_path}\PowerPoint Files',
        '.csv' : f'{download_folder_path}\CSV Files',
        '.psd' : f'{download_folder_path}\PDFs'
    }

    misc_folder = f'{download_folder_path}\Misc'

    def on_modified(self, event):
        if event.event_type == 'modified':
            for item in listdir(download_folder_path):
                file_path = join(download_folder_path, item)
                print(file_path)
                if isfile(file_path):
                    print("It is a file")
                    if check_in_use(file_path) == False:
                        print("File not in use")
                        file_extension = os.path.splitext(file_path)[1]
                        if file_extension == '.tmp' or file_extension == '.crdownload':
                            print("Its a temp.")
                            continue
                        if file_extension in self.types_map:
                            dest = os.path.join(self.types_map[file_extension], os.path.basename(file_path))
                            num = 0
                            while os.path.exists(dest):
                                num += 1
                                file_name_split = os.path.basename(file_path).split('.')
                                base_name = file_name_split[0] + ' (' + str(num) + ')' + '.' + file_name_split[1]
                                dest = os.path.join(self.types_map[file_extension], base_name)
                            
                            shutil.move(file_path, dest)
                        else:
                            dest = os.path.join(self.misc_folder, os.path.basename(file_path))
                            num = 0
                            while os.path.exists(dest):
                                num += 1
                                file_name_split = os.path.basename(file_path).split('.')
                                base_name = file_name_split[0] + ' (' + str(num) + ')' + '.' + file_name_split[1]
                                dest = os.path.join(self.misc_folder, base_name)
                            shutil.move(file_path, dest)
                    else:
                        print("In use!")
                        continue


        # if event.event_type == 'modified':
        #     for item in listdir(download_folder_path):
        #         file_path = join(download_folder_path, item)
        #         print("Listing: ", file_path)
        #         if isfile(file_path):
        #             print("It is a file!")
        #             file_extension = os.path.splitext(file_path)[1]
        #             if file_extension == '.tmp' or file_extension == 'crdownload':
        #                 print("Its a temp.")
        #                 continue
        #             if file_extension in self.types_map:
        #                 shutil.move(file_path, os.path.join(self.types_map[file_extension], os.path.basename(file_path)))
        #             else:
        #                 shutil.move(file_path, os.path.join(self.misc_folder, os.path.basename(file_path)))
        
        
        
        # if event.event_type == 'created':
        #     file_path = event.src_path
        #     file_extension = os.path.splitext(file_path)[1]
        #     print("Currently reading: ", file_path)
        #     t = time.localtime()
        #     current_time = time.strftime("%H:%M:%S", t)
        #     print(current_time)

        #     if file_extension == '.tmp' or file_extension == 'crdownload':
        #          return
            
        #     time.sleep(1)
        #     t = time.localtime()
        #     current_time = time.strftime("%H:%M:%S", t)
        #     print("After sleep time: ", current_time)

        #     if file_extension in self.types_map:
        #         dest = os.path.join(self.types_map[file_extension], os.path.basename(file_path))
        #         num = 0
        #         while os.path.exists(dest):
        #             num += 1
        #             file_name_split = os.path.basename(file_path).split('.')
        #             base_name = file_name_split[0] + '(' + str(num) + ')' + '.' + file_name_split[1]
        #             dest = os.path.join(self.types_map[file_extension], base_name)
                
        #         shutil.move(file_path, dest)
        #     else:
        #         shutil.move(file_path, os.path.join(self.misc_folder, os.path.basename(file_path)))

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(Organizer(), download_folder_path, recursive=False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()