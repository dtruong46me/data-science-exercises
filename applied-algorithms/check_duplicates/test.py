from main import main
from generate import generate
from time import time

time_exc = []

def test(test_case_choose):
    test_case = {
        "n": [5, 100, 1000, 5000, 10000, 50000, 100000],
        "initial": [1, 1, 1, 1, 1, 1, 1],
        "final": [10, 100, 1000, 10000, 100000, 10000000, 1000000000]
    }

    # Number of test cases: 7
    # test_case_choose = 

    n = test_case["n"][test_case_choose-1]
    initial = test_case["initial"][test_case_choose-1]
    final = test_case["final"][test_case_choose-1]

    generate(n, initial, final)

    start_time = time()
    main()
    end_time = time()

    print("n       :",n)
    print("initial :",initial)
    print("final   :", final)
    print(f"Execution time: {(end_time - start_time):.5f}")
    time_exc.append(end_time - start_time)

if __name__ == '__main__':
    # for test_case_choose in range(6):
    #     test(test_case_choose)
    
    # for i in range(len(time_exc)):
    #     print(time_exc[i])
    '''
    0.00518
    0.00760
    0.01666
    0.09631
    0.44075
    10.88188

    '''
    test(7)