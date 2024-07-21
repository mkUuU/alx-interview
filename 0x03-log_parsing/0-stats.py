#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def parse_line(line):
    """ Parse a log line and return the status code and file size, or None if the line is invalid. """
    pattern = r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        return status_code, file_size
    return None

def print_statistics(file_size_total, status_counts):
    """ Print the statistics in the required format. """
    print(f"File size: {file_size_total}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    file_size_total = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                file_size_total += file_size
                status_counts[status_code] += 1
                line_count += 1
            
            if line_count % 10 == 0:
                print_statistics(file_size_total, status_counts)
                
    except KeyboardInterrupt:
        print_statistics(file_size_total, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
