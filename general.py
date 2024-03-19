import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Crating project ' + directory)
        os.makedirs(directory)

