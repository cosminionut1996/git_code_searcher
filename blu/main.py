import json
import sys

from .server_blu import run as server_blu_run
from .utils import find_dir_content_matches


def console():
    matches = find_dir_content_matches(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(matches, indent=2))

def server():
    server_blu_run()
