#!/bin/bash
in=$@
folders="images|sounds|videos|web"
echo Adding $folders files from $in to git.
files=$(grep -Eo "($folders)[^\")]*\.[a-z]+" $in _quarto.yml)
for file in $files; do 
    f=${file#*:}
    echo - $f; 
    git add $f; 
done
