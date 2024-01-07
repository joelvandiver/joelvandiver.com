#!/bin/bash

# Read from the file file.txt and output the tenth line to stdout.
# The 'NR' is the line number.  The "NR" stands for "Number of Records".
# "awk" stands for "Aho, Weinberger, and Kernighan", the authors of the language.
awk 'NR == 10' file.txt