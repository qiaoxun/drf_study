from django.test import TestCase

# Create your tests here.


log_file_path = {}
upgrade_log_file_path = '/upgrade_main_log.txt'
start_log_file_path = '/bin/start_log.txt'
log_file_path['upgrade_log_file_path'] = upgrade_log_file_path
log_file_path['start_log_file_path'] = start_log_file_path

for path in log_file_path:
    print(path)
    print(log_file_path[path])

print(type(log_file_path))
print(type(start_log_file_path))