#!/usr/bin/env python3

# Part 0 Python: split & slice
# Susanne Peer
# 

def main():
    result = None

    name = "4. Nov. 2027 by Susanne Peer, SWD"

# Split the string by comma and get the last part
    parts = name.split(',')
    if len(parts) > 1:
        last_name = parts[0].split()[-1].strip()
        result = last_name.upper()

    return result

# Just for testing. The printed output is NOT relevant for grading.
# Evaluation calls function 'main' and analyses the values returned.
print(main())

