import json
import logging

def parse_log_file(project):
    log_files = {
        'sample': 'storage/sample.log',
    }

    log_file = open(log_files[project], 'r')
    for line in log_file.readlines():
        print("LINE:", line)
