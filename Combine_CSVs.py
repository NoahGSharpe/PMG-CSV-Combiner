import sys


def main():
    if len(sys.argv) < 2:
        return

    with open(sys.argv[1]) as file:
        print(file.readline()[:-1] + ",\"filename\"\n")

    for i in range(1, len(sys.argv)):
        path = sys.argv[i]
        filename = path[path.rfind('/')+1:]
        with open(path) as file:
            for j, line in enumerate(file):
                if j == 0 or line == '\n':
                    continue
                print(line[:-1] + f",\"{filename}\"\n")


if __name__ == '__main__':
    main()
