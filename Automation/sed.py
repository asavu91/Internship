import re

def is_numeric(word):
    return bool(re.match(r'^\d+$', word))

def replace_timestamp(log_line):
    words = log_line.split()
    timestamp = words[1]

    if len(words) >= 3 and (is_numeric(words[-1]) or is_numeric(words[-2])):
        if is_numeric(words[-1]):
            replacement = words[-1]
        else:
            replacement = words[-2]

        return True, log_line.replace(timestamp, replacement)
    else:
        return False, log_line

def process_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        changed, modified_line = replace_timestamp(lines[i])
        if changed:
            print(f"Original: {lines[i].strip()}")
            print(f"Modified: {modified_line.strip()}\n")
            lines[i] = modified_line

    with open(file_path, 'w') as file:
        file.writelines(lines)

log_file_path = "log.txt"
process_log_file(log_file_path)
