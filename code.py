import os
import re
import argparse

def rename_files(directory, pattern, replacement, recursive):
    regex = re.compile(pattern)
    if recursive:
        for root, _, files in os.walk(directory):
            for name in files:
                new_name = regex.sub(replacement, name)
                if new_name != name:
                    old_path = os.path.join(root, name)
                    new_path = os.path.join(root, new_name)
                    os.rename(old_path, new_path)
                    print(f"{old_path} -> {new_path}")
    else:
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                new_name = regex.sub(replacement, name)
                if new_name != name:
                    new_path = os.path.join(directory, new_name)
                    os.rename(path, new_path)
                    print(f"{path} -> {new_path}")

parser = argparse.ArgumentParser()
parser.add_argument("directory")
parser.add_argument("pattern")
parser.add_argument("replacement")
parser.add_argument("-r", "--recursive", action="store_true")

args = parser.parse_args()
rename_files(args.directory, args.pattern, args.replacement, args.recursive)
