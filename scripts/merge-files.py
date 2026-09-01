# Created by Christian Frisson
# License: "CC BY-NC-SA"

import os
from pathlib import Path
import shutil
import re
from tempfile import mkstemp

# https://stackoverflow.com/questions/12714415/python-equivalent-to-sed
def sed(pattern, replace, source):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    Args:
        pattern (str): pattern to match (can be re.pattern)
        replace (str): replacement str
        source  (str): input filename
    """

    fin = open(source, 'r')

    fd, name = mkstemp()

    fout = open(name, 'w')

    for line in fin:
        out = re.sub(pattern, replace, line)
        fout.write(out)

    fin.close()
    fout.close()

    shutil.move(name, source) 

# Check if Quarto successfully populated the directory paths
project_dir = os.environ.get("QUARTO_PROJECT_DIR")
output_dir = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR")
output_files = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES").splitlines()

main_files_created = False
slide_files = "slide_files"
for output_file in output_files:
    stem = Path(output_file).stem
    if not main_files_created:
        if os.path.exists(slide_files):
            shutil.rmtree(slide_files)
        if os.path.exists(f"{stem}_files"):
            print(f"- Moving {stem}_files to {slide_files}")
            shutil.move(f"{stem}_files",slide_files)
            main_files_created = True
    else:
        shutil.rmtree(f"{stem}_files")
    if os.path.exists(output_file):
        print(f"- Updating file {output_file}")
        sed(f"{stem}_files", slide_files, output_file)
    