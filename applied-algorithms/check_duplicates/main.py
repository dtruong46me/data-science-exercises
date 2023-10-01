import sys

def main():
    # n = int(sys.stdin.readline())
    # print(type(n))
    # array = [int(x) for x in sys.stdin.readline().split()]

    path = "applied-algorithms/check-duplicates/data.txt"

    with open(path, 'r') as f:
        n = int(f.readline())
        array = [int(x) for x in f.readline().split()]

    check = []
    
    for i in range(n):
        # print(check)
        if array[i] not in check:
            print(0, end=' ')
            check.append(array[i])
        else:
            print(1, end=' ')
    print()
    # print(check)

# if __name__ == '__main__':
#     main()