import sys
import os
import pathlib
import shutil

downloads_directory = '/home/diegof/Downloads/'

downloads_files = os.listdir(downloads_directory)

print(downloads_directory, "donwloads")

images_types = ['jpg', 'png', 'jpeg']
video_types = ['mp4', 'mbw', 'avi', '3gp', 'ogg']
program_types = ['deb', 'AppImage', 'bz2']


def getFileType(file_name):
    file_type = file_name.split('.')
    return file_type[-1]


def move_file_to(file, location):
    shutil.move(downloads_directory + file,
                downloads_directory + location)


for file in downloads_files:
    print("-----------------")
    print(file, "File")
    file_type = getFileType(file)

    if(file_type in program_types):
        move_file_to(file, 'programs')

    if(file_type in video_types):
        move_file_to(file, 'videos')

    if(file_type in images_types):
        move_file_to(file, 'images')

    if(file_type == 'zip'):
        move_file_to(file, 'zip')
