def split_and_join(line):
    x=line.split()
    y='-'.join(x)
    return y

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)