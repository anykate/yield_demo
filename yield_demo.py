def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


def main():
    for count, line in enumerate(read_file('sample_file.txt')):
        print(f'{count + 1}: {line}')


if __name__ == '__main__':
    main()
