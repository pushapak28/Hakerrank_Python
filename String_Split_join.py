def split_and_join(line):
    # write your code here
    a = "-".join(line.split(" "))
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
