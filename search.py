#!/usr/bin/python3 

import os
import time 

root_path = '/home/edgar757'
LOG_FILE = 'log_db'

def logSearch():
    matches = []
    log_file = open(LOG_FILE, 'r')
    # To remove duplicate search queries from log DB
    # Cause sets cant have duplicates
    pathsQuery = list(set(log_file.read().splitlines()))
    t0 = time.time()
    for path in pathsQuery:
        for file in os.listdir(path):
            if file == search_target:
                matches.append(file + ' ' + path)
    t1 = time.time()
    print('Found {} match in {} --> from DB'.format(len(matches), t1 - t0))
    return matches

def search():
    matches = []
    t0 = time.time()
    log_file = open(LOG_FILE, 'a')
    for dirpath, dirnames, filename in os.walk(root_path):
        for files in filename:
            if files == search_target:
                matches.append(files + ' ' + dirpath)
                log_file.write(dirpath + '\n')
    t1 = time.time()
    print('Found {} matches in {} --> from Normal Search'.format(len(matches), t1 - t0))
    log_file.close()
    return matches

def clearlogDB():
    log_file = open(LOG_FILE, 'w')
    log_file.write('')
                

search_target = input('Enter search item: ')
# logSearch_result = logSearch()

if not logSearch():
    print(search())
