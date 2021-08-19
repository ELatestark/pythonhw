# !/usr/bin/env python3
# count different shells and show groups
 
# /etc/passwd
# /etc/group
from typing import TextIO
 
 
def get_shell_counts() -> dict:
    passwd_file = open('/etc/passwd', 'r')
    passwd_lines = passwd_file.readlines()
 
    shell_counts = dict()
 
    for passwd_line in passwd_lines:
        shell = passwd_line.split(':')[-1].rstrip('\n')
        if shell not in shell_counts:
            shell_counts[shell] = 1
        else:
            shell_counts[shell] = shell_counts[shell] + 1
 
    return shell_counts
 
 
def write_shell_counts(shell_counts: dict, out_file: TextIO) -> None:
    strs_to_write = list()
 
    for shell in shell_counts:
        count = shell_counts[shell]
 
        str_to_write = shell + " - " + str(count)
        strs_to_write.append(str_to_write)
 
    str_to_write_total = " ; ".join(strs_to_write)
    out_file.write(str_to_write_total + "\n")
 
 
def get_groups() -> dict:
    passwd_file = open('/etc/passwd', 'r')
    passwd_lines = passwd_file.readlines()
 
    uid_by_login = dict()
    for passwd_line in passwd_lines:
        passwd_line_data = passwd_line.split(':')
        login = passwd_line_data[0]
        uid = passwd_line_data[2]
        uid_by_login[login] = uid
 
    group_uids = dict()
 
    group_file = open('/etc/group', 'r')
    group_lines = group_file.readlines()
 
    for group_line in group_lines:
        group_name = group_line.split(':')[0]
        logins = group_line.split(':')[3].rstrip('\n')
 
        if logins == "":
            continue
 
        user_ids = list()
        for login in logins.split(','):
            user_ids.append(uid_by_login[login])
 
        group_uids[group_name] = user_ids
 
    return group_uids
 
 
def write_groups(group_uids: dict, out_file: TextIO) -> None:
    for group in group_uids:
        uids = group_uids[group]
 
        str_to_write = group + ": " + ", ".join(uids)
        out_file.write(str_to_write + "\n")
 
 
out_file = open('outfile.txt', 'w')
 
shell_counts = get_shell_counts()
write_shell_counts(shell_counts, out_file)
 
groups = get_groups()
write_groups(groups, out_file)
 
out_file = open('outfile.txt', 'r')
 
file_contents = out_file.readlines()
print(file_contents)