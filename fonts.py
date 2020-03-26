import glob, os, shutil


source_dir = os.path.dirname(os.path.realpath(__file__))
dest_dir = r'H:\UberEats App + Backend\adobe\Adobe.Font.Folio.Collection.v11.0.otf_p30download.com\Western Fonts\dir'

for root, dirs, files in os.walk(".", topdown=False):
    for name1 in dirs:
        name_ = os.path.join(root, name1)

        files = glob.iglob(os.path.join(name_, "*.otf"))
        for file in files:
            if os.path.isfile(file):
                if file in dest_dir:
                    continue
                try:
                    shutil.copy2(file, dest_dir)
                except shutil.SameFileError:
                    pass

