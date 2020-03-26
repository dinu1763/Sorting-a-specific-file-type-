import glob, os, shutil


source_dir = os.path.dirname(os.path.realpath(__file__))
dest_dir = path to destination directory

for root, dirs, files in os.walk(".", topdown=False):
    for name1 in dirs:
        name_ = os.path.join(root, name1)

        files = glob.iglob(os.path.join(name_, "*.<file-type-extension>"))
        for file in files:
            if os.path.isfile(file):
                if file in dest_dir:
                    continue
                try:
                    shutil.copy2(file, dest_dir)
                except shutil.SameFileError:
                    pass

