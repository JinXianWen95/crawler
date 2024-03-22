import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'olevod'
HOMEPAGE = 'https://www.olevod.tv/index.html'
DOMAIN_NAME =  get_domain_name(HOMEPAGE)
QUEUE_FILE = f'{PROJECT_NAME}{os.path.pathsep}queue.txt'
CRAWLED_FILE = f'{PROJECT_NAME}{os.path.pathsep}crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

