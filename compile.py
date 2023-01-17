import sys




def getInputFile():
    """Get the file name from the command line or prompt the user for it."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "test.txt"
    return input("Enter SBN file name (with extension): ")

def getOutputFile():
    """Get the file name from the command line or prompt the user for it."""
    if len(sys.argv) > 2:
        return sys.argv[2]
    return "output.txt"
    return input("Enter output file name (with extension): ")


def main():
    inp = getInputFile()
    out = getOutputFile()

    print("Compiling...", inp)




if __name__ == "__main__":
    main()