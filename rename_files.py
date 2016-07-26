import sys
import getopt
import os 

def rename_files():
    save_path = os.getcwd()
    filelist = os.listdir(r"/Users/hidoos/repository/LearnInUdacity/full-stack-web-develper/project-movie/requirements/python/rename_files/images")
    os.chdir("/Users/hidoos/repository/LearnInUdacity/full-stack-web-develper/project-movie/requirements/python/rename_files/images")
    for filename in filelist:
        os.rename(filename, filename.translate(None, '0123456789'))
    os.chdir(save_path)

def main():
    rename_files()

if __name__ == "__main__":
    main()