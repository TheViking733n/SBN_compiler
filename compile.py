import sys


def getFile():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "test.txt"
    return input("Enter SBN file name: ")


def main():
    file = getFile()
    print("Compiling...", file)