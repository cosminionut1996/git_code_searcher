import fnmatch
import os
import shutil
import subprocess
import sys
import pathlib


def clone_repository(addr, destination):
    cd = os.getcwd()
    os.chdir(destination)
    subprocess.Popen(["git", "clone", addr]).wait()
    os.chdir(cd)

def clear_repository(destination):
    shutil.rmtree(destination)


def get_sequence(i, j, a, b):
    i0 = i
    i += 1
    j += 1
    n, m = len(a), len(b)
    while i < n and j < m and a[i] == b[j]:
        i += 1
        j += 1
    return a[i0: i], i


def find_file_matches(lines1, lines2):
    # Greedily search for matches trying to avoid duplicates

    matching_sections = list()

    i = 0
    while i < len(lines1):
        for j in range(len(lines2)):
            if lines1[i] == lines2[j] and lines1[i] != "\n":
                seq, jump = get_sequence(i, j, lines1, lines2)
                matching_sections.append(seq)
                i = jump - 1
                break

        i += 1
    return matching_sections


def find_dir_content_matches(directory, filepath, glob_pattern):

    matches = dict()
    file_lines = open(filepath).readlines()

    for root, _, files in os.walk(directory):
        for f in fnmatch.filter(files, glob_pattern):
            fpath = os.path.join(root, f)
            try:
                content = open(fpath).readlines()
            except UnicodeDecodeError:
                continue
            found_matches = find_file_matches(file_lines, content)
            if found_matches:
                matches[f] = found_matches

    return matches
