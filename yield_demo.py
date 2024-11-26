import time


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


def main(filename):
    start = time.time()

    for count, line in enumerate(read_file(filename)):
        print(f'{count + 1}: {line}')

    end = time.time()
    print(f"\nTotal time taken to read \"{filename}\": {end - start} seconds!")


if __name__ == '__main__':
    main('sample_file.txt')
