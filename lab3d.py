#!/usr/bin/env python3
# Author ID: ssharma608

import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, 
            stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output = p.communicate()
# The above stdout is stored in bytes
# Convert stdout to a string and strip off the newline characters
    return output[0].decode('utf-8').strip()
if __name__ == '__main__':
    print(free_space())


