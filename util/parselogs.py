from datetostr import datetimestr_to_unix

log_files = {
    'sample': '../storage/sample.log',
}

def parse_log_file(project):
    logs = {}

    log_file = open(log_files[project], 'r')
    for line in log_file.readlines():
        metadata, log_msg = line.split("-->")
        if len(log_msg.strip())==0:
        	continue

        level, _, log_date, log_time = metadata.split()
        log_datetime = log_date + " " + log_time
        timestamp = datetimestr_to_unix(log_datetime)

        logs[timestamp] = {
            'level': level,
            'message': log_msg
        }

    return logs

if __name__=='__main__':
    print	parse_log_file('sample')