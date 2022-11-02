import random
import time

def get_random_array(size):
    arr = []
    for i in range(size):
        number = random.randint(-30, 30)
        arr.append(number)

    return arr

def sort_by_function(arr):
    return sorted(arr)


def sort_array(arr):
    s = 0
    while s < len(arr)-1:
        n1 = arr.pop(0)
        s = 0
        for i in range(len(arr)):
            if n1 < arr[i]:
                s += 1
                tmp = n1
                n1 = arr.pop(i)
                arr.insert(i, tmp)
            elif n1 == arr[i]:
                s += 1
            else:
                s = 0

        arr.append(n1)

    return arr

def main():

    input_array = [5, 9, 6, 1]
    arr = get_random_array(20)
    print("Generated array: ", arr)
    print("Yours array: ", input_array)
    tic = time.perf_counter()
    arr.extend(input_array)
    print(sort_array(arr))
    toc = time.perf_counter()

    print(f"Finished in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
