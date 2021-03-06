import os
import shutil

## File Organizer
##  def include( )
##  Advanced Concepts in Python
##  June 2020

#dictionary of file categories and file extensions
DIRECTORIES = {
    "Web": [".html5", ".html", ".htm", ".xhtml", ".css", ".webarchive", ".php",
            ".yaml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".jfif"],
    "Photoshop": [".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".csv"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain Text": [".txt", ".in", ".out", ".key", ".md"],
    "PDF": [".pdf"],
    "Code": [".py", ".java", ".RData", ".Rhistory", ".cpp", ".o"],
    "Shortcuts": [".lnk", ".url"],
    "Configuration": [".ini", ".msi", ".apk", ".crdownload"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

#The path of the directory to be sorted
#edit this to where you placed your test-file folder

path = 'C:\\Users\\Alveena Rehman\\github\\File-Organizer\\file-organizer\\file-organizer\\test-file'

#Creates a list with the filenames in the directory
list_ = os.listdir(path)

#goes through every file in the directory
for file_ in list_:


    ##START CODING HERE

    # 1. Create variables name and ext and set them to the file_'s name and extention
    (name, ext) = os.path.splitext(file_)


    #Checks if there is no extension
    #If the extension variable is empty, moves onto the next iteration
    if ext == '':
        continue

    # 2. Loop through DIRECTORIES
    for extCategory in DIRECTORIES:
        # 3. If the extension is in one of the lists
            if ext in DIRECTORIES[extCategory]:
                dirName = extCategory
                origin = path + "\\" + file_
                newPath = path + "\\" + dirName
            # 4. Check if the key is a folder in the current directory already
                if os.path.exists(newPath) == True:

                # 5. If the key is already a folder in the directory,
                # move the file into that directory using shutil.move
                    shutil.move(origin, newPath)

            # 6. If the folder is not in the current directory already,
            # create the folder
                if os.path.exists(newPath) == False:

                # 7. Move the file into that directory using shutil.move
                    os.makedirs(newPath)
                    shutil.move(origin, newPath)
        # 8. Else, continue to the next iteration
