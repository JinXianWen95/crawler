import os

# create a folder for each project that would be crawled
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Crating project ' + directory)
        os.makedirs(directory)

def create_data_file(directory, url):
    queue = directory + os.path.sep + 'queue.txt'
    crawled = directory + os.path.sep + 'crawled.txt'
    if not os.path.exists(queue):
        create_file(directory, url)
    if not os.path.exists(crawled):
        create_file(directory, '')

def create_file(directory, content):
    f = open(directory, 'w')
    f.write(content)
    f.close

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + os.linesep)

def delete_file_content(path):
    with open(path, 'w'):
        pass

def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace(os.linesep, ''))
    return results

def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)