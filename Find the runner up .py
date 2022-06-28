if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
print(sorted(list(set(arr)))[::-1][1])
#print(sorted(set(arr)))[-2])
