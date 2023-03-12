def binarySearch_recursive(arr, x, low, high):
    """Binary search algorithm which returns number x location index in sorted array"""
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
           return mid

        elif arr[mid] > x:
            # mid = (low + mid) // 2 
            return binarySearch_recursive(arr, x, low, mid-1)
        
        elif arr[mid] < x:
            # mid = (mid + high) // 2
            return binarySearch_recursive(arr, x, mid+1, high)
    else:
        return -1 


def binarySearch_bottom_up(arr, x, low, high):
    while low <= high:
        # The sum overflows to a negative value and the value stays negative when divided by 2. 
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

arr = []
x = 0
low = 0
high = len(arr)-1
result = binarySearch_recursive(arr, x, low, high)
if result != -1:
    print(result, arr[result])
else:
    print("Not in array")