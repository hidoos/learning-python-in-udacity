#!/usr/bin/env python

import os

save_path = os.getcwd()

def rename_file():
    os.chdir("./rename_files/images/")
    file_name = '2d.png'
    os.rename(file_name, "<hello>world</hello>")
    current_dir = os.getcwd()
    print current_dir

rename_file()
