import os.path
import re


upload_file_names = []

for (source_dir, dir_list, file_list) in os.walk('../ppp_files/'):
	for file_name in file_list:
		if file_name == '.DS_Store':
			pass
		elif source_dir == '../ppp_files/':
			upload_file_names.append(file_name)
		else:
			target = source_dir + '/' + file_name
			match = re.match("../ppp_files/(.+)", target)
			upload_file_names.append(match.groups()[0])

print upload_file_names