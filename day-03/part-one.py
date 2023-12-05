import os
import re

def main():

    previous_line = ""
    this_line = ""

    sum = 0

    with open('input.txt') as f:
        for next_line in f:

            if this_line == "":
                this_line = next_line
                continue


            i = 0
            searching = True
            
            for i in range(len(this_line)):
                if this_line[i] in '1234567890':
                    if searching:
                        start = i
                        searching = False
                else:
                    if not searching:
                        end = i
                        searching = True
                        number = check_number(start, end, previous_line, this_line, next_line)
                        if number > 0:
                            print('OK!')
                            sum += number

            previous_line = this_line
            this_line = next_line

    print(sum)

def check_number(start, end, previous_line, this_line, next_line):
    pattern = r'[\*\#\+\$=\-\/%&@]'

    number = int(this_line[start:end])

    print(previous_line[max(0,start-1):min(end+1,len(previous_line))])
    print(    this_line[max(0,start-1):min(end+1,len(this_line))])
    print(    next_line[max(0,start-1):min(end+1,len(next_line))])

    m = re.search(pattern, previous_line[max(0,start-1):min(end+1,len(previous_line))])
    if m:
        return number
    m = re.search(pattern, this_line[max(0,start-1):start])
    if m:
        return number
    m = re.search(pattern, this_line[end:min(end+1,len(this_line))])
    if m:
        return number
    m = re.search(pattern, next_line[max(0,start-1):min(end+1,len(next_line))])
    if m:
        return number
    
    print('no')
    return 0

main()