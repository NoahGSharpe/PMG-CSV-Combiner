import sys


def main():
    # End program if there are not enough arguments
    if len(sys.argv) < 2:
        return

    # Output column headers with appended filename column
    with open(sys.argv[1]) as file:
        print(file.readline()[:-1] + ",\"filename\"\n")

    # Iterate through csv files
    for i in range(1, len(sys.argv)):
        path = sys.argv[i]
        # Find filename (anything after last forward slash)
        filename = path[path.rfind('/')+1:]
        with open(path) as file:
            for j, line in enumerate(file):
                # Skip header lines and blank lines
                if j == 0 or line == '\n':
                    continue
                print(line[:-1] + f",\"{filename}\"\n")


if __name__ == '__main__':
    main()
