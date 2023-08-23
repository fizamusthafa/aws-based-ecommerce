import csv
import time
import sys

sourceData = "OnlineRetail.csv"
placeholder = "LastLine.txt"

def get_line_count(file_path):
    with open(file_path, encoding='latin-1') as f:
        return sum(1 for _ in f)

def make_log(start_line, num_lines, source_file, dest_file):
    with open(source_file, 'r') as csvfile, open(dest_file, 'w') as dstfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(dstfile)
        next(reader)  # skip header
        lines_written = 0
        for _ in range(start_line):
            next(reader)  # Skip lines until start_line
        for _ in range(num_lines):
            try:
                row = next(reader)
                writer.writerow(row)
                lines_written += 1
            except StopIteration:
                break
        return lines_written

num_lines = 100
start_line = 0

if len(sys.argv) > 1:
    num_lines = int(sys.argv[1])

try:
    with open(placeholder, 'r') as f:
        start_line = int(f.readline())
except IOError:
    start_line = 0

print(f"Writing {num_lines} lines starting at line {start_line}\n")

total_lines_written = 0
lines_in_file = get_line_count(sourceData)

while total_lines_written < num_lines:
    lines_written = make_log(start_line, num_lines - total_lines_written, sourceData, time.strftime("/var/log/cadabra/%Y%m%d-%H%M%S.log"))
    total_lines_written += lines_written
    start_line += lines_written
    if start_line >= lines_in_file:
        start_line = 0

print(f"Wrote {total_lines_written} lines.\n")

with open(placeholder, 'w') as f:
    f.write(str(start_line))
