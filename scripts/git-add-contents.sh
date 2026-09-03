#!/bin/bash
in=$@
if [[ "$in" != *.qmd ]]; then
    echo "Please specify a qmd file as input."
    exit 1;
fi
folders="images|sounds|videos|web"
echo Adding $folders files from $in to git.
files=$(grep -Eo "($folders)[^\")]*\.[a-z]+" $in _quarto.yml)
for file in $files $in ${in%qmd}html; do 
    f=${file#*:}
    echo - $f; 
    git add $f; 
done
