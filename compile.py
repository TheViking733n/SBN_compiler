import sys


INPUT = None
OUTPUT = None
VARS = []
INSTRUCTIONS = []


def getInputFile():
    global INPUT
    """Get the file name from the command line or prompt the user for it."""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter input file name (with extension): ")
    try:
        INPUT = open(filename, "r")
    except FileNotFoundError:
        print("File not found.")
        sys.exit()


def getOutputFile():
    global OUTPUT
    """Get the file name from the command line or prompt the user for it."""
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = input("Enter output file name (with extension): ")
    try:
        OUTPUT = open(filename, "w")
    except FileNotFoundError:
        print("File not found.")
        sys.exit()


def preprocess():
    """Preprocess the input file."""
    flag = 1
    for row in INPUT.readlines():
        row = row.split('//')[0].strip(' \t').upper()
        if row.startswith("SBN"):
            INSTRUCTIONS.append(row)
            flag = 0
        elif flag:
            VARS.append(row)
    INPUT.close()





def compile():
    


def main():
    getInputFile()
    getOutputFile()





if __name__ == "__main__":
    main()