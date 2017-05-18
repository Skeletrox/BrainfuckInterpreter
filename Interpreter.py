#usr/bin/python3
import sys
from pathlib import Path
import os.path
memoryCells = []
loopLocations = []
for i in range (0, 256):
    memoryCells.append(0)


def main():
    if len(sys.argv) == 2:
        interpretbrainfuck(sys.argv[1])
    elif len(sys.argv) == 1:
        name = input('Enter filename to read [alternatively you can pass file as a command line argument]: ')
        interpretbrainfuck(name)
    else:
        print ('[-]Usage: Interpreter.py [filename]')

def interpretbrainfuck(fileName):
    if not os.path.isfile(fileName):
        print ('[-]File does not exist!')
        exit(0)
    memoryPointer = 0
    loopLocation = 0
    charsRead = 0
    numberOfLoops = -1
    with open(fileName) as f:
        loopLocation = 0
        while True:
            c = f.read(1)
            charsRead += 1
            if not c:
                break
            if c == '+':
                memoryCells[memoryPointer] += 1
            elif c == '-':
                try:
                    memoryCells[memoryPointer] -= 1
                except:
                    print ('Exception at ' + str(charsRead) + ' trying to reference ' + str(memoryPointer) + ", check your code!")
                    exit(0)
            elif c == '>':
                memoryPointer += 1
            elif c == '<':
                memoryPointer -= 1
            elif c == '.':
                print (chr(memoryCells[memoryPointer]), end='')
            elif c == ',':
                memoryCells[memoryPointer] = ord(input(''))
            elif c == '[':
                loopLocation = charsRead + 1
                loopLocations.append(loopLocation)
                numberOfLoops += 1
            elif c == ']':
                if memoryCells[memoryPointer] != 0:
                    charsRead = loopLocations[numberOfLoops] - 1
                    f.seek(charsRead, 0)
                else:
                    loopLocations.remove(loopLocations[numberOfLoops])
                    numberOfLoops -= 1
    if numberOfLoops > -1:
        print('\nError: Unbalanced brackets, please recheck code!')
'''
    If the number of unfinished loops is a natural number then there is a control fault!
'''

if __name__ == '__main__':
    main()
