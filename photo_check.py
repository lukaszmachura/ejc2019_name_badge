from glob import glob



def get_file_info(line, files):
    line = line.split(",")
    pattern = line[5].rstrip()
    d = "nophoto.jpg"
    for f in files:
        if pattern in f:
            # d = "".join([line[5].rstrip()] + [line[i][:3] for i in [0, 1, 2]])
            d = f.split("/")[1]
            break
    return d


def get_lista_info(line):
    line = line.split(",")
    d = "-".join([line[5].rstrip()] + [line[i][:3] for i in [0, 1, 2]])
    return d


def compare_file_lista(fd, ld):
    pass


if __name__ == "__main__":
    dir = "foto/"
    files = glob(dir + '*.jpeg')
    files.extend(glob(dir + '*.png'))
    files.extend(glob(dir + '*.jpg'))

    with open('lista.csv') as f:
        for line in f:
            ld = get_lista_info(line)
            fd = get_file_info(line, files)
            print(line.rstrip() + "," + fd)
