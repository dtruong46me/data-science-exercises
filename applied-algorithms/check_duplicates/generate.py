from random import randint

path = "applied-algorithms/check-duplicates/data.txt"

def generate(n, initial, final):
    with open(path, 'w') as f:
        f.write(str(n) + '\n')
        array = [randint(initial, final) for _ in range(n)]
        # print(array)
        for i in range(n):
            f.write(str(array[i]) + ' ')

# def main():
#     n = 100
#     initial = 1
#     final = 20
    
#     # Starting generate the test case
#     generate(n, initial, final)

# if __name__ == '__main__':
#     main()