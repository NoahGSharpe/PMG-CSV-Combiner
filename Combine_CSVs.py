import sys


def main():
    needHeader = True
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        with open(filename) as file:
            for j, line in enumerate(file):
                if needHeader:
                    print(line[:-1] + ",\"filename\"\n")
                    needHeader = False
                if j == 0 or line == '\n':
                    continue
                print(line[:-1] + f",\"{filename}\"\n")


if __name__ == '__main__':
    main()
