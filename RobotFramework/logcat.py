import re
from datetime import datetime

def parse_logcat_file(file_path):
    parsed_data = []
    with open(file_path, 'r') as file:
        current_app = {}
        for line in file:
            if 'ActivityTaskManager: START u0' in line:
                current_app['package'] = extract_package_name(line)
                current_app['start_time'] = extract_timestamp(line)
            elif 'Layer: Destroyed ActivityRecord' in line:
                current_app['end_time'] = extract_timestamp(line)
                current_app['lifespan'] = calculate_lifespan(current_app['start_time'], current_app['end_time'])
                parsed_data.append(current_app)
                current_app = {}
    return parsed_data

def extract_package_name(line):
    match = re.search(r'cmp=(.*?)/', line)
    return match.group(1) if match else None

def extract_timestamp(line):
    match = re.search(r'(\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3})', line)
    if match:
        return datetime.strptime(match.group(1), '%m-%d %H:%M:%S.%f')
    return None

def calculate_lifespan(start_time, end_time):
    return (end_time - start_time).total_seconds()

def output_to_yaml(data, output_file):
    with open(output_file, 'w') as file:
        file.write("applications:\n")
        for idx, app in enumerate(data, start=1):
            file.write(f"  - application_{idx}:\n")
            file.write(f"      app_path: {app['package']}\n")
            file.write(f"      ts_app_started: {app['start_time'].strftime('%m-%d %H:%M:%S.%f')[:-3]}\n")
            file.write(f"      ts_app_closed: {app['end_time'].strftime('%m-%d %H:%M:%S.%f')[:-3]}\n")
            file.write(f"      lifespan: {app['lifespan']:.3f}s\n")

if __name__ == "__main__":
    logcat_file = "logcat.txt"
    output_file = "output.yml"

    parsed_data = parse_logcat_file(logcat_file)
    output_to_yaml(parsed_data, output_file)
    print(f"Output written to {output_file}")
