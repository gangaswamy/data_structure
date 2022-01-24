import math

def binary_search(arr, val):
    start = 0
    end = len(arr)-1
    
    while ( start < end):
        mid = math.ceil((start + end)/2)
        print("start: %d, mid: %d, end: %d" % ( start, mid, end ))
        if( arr[mid] == val):
            print("found in position: ", mid)
            return mid 
        if(  val < arr[mid]):
            end = mid
        else:
            start = mid
    return -1

array = [1, 4, 6, 7, 9, 10, 13, 17]
binary_search(array, 7)