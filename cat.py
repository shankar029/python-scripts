import argparse
import sys
from pathlib import Path
import os


def write_contents(file_list, fout):
    while len(file_list) > 0:
        file_name = file_list.pop()
        file_path = Path(file_name)
        if not file_path.exists():
            file_path = Path(os.getcwd(), file_name)
        with open(file_path, 'r') as f:
            fout.writelines(f.readlines())


parser = argparse.ArgumentParser('cat')
parser.add_argument('files', nargs='+', help="List of file paths to be concatenated")
parser.add_argument('-o', '--output', help="Output file path")

args = parser.parse_args()
files = list(args.files)

if not args.output:
    write_contents(files, sys.stdout)
else:
    with open(args.output, 'w') as out:
        write_contents(files, out)
