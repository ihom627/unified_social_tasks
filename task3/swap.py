# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    DEBUG = 0 

    if DEBUG:
        print "this is initial A %s " % A

    #find index before first deceasing value
    prev_iter = -10000000 
    prev_iter_index = 0
    cur_iter_index = 0

    swap1_value = 0
    swap1_index = 0
    for cur_iter in A:
        if prev_iter < cur_iter:
            prev_iter = cur_iter
        else:
            if DEBUG:
                print "Found prev_iter %d > cur_iter %d" % (prev_iter, cur_iter)
            swap1_value = prev_iter 
            swap1_index = A.index(prev_iter)
       
    if DEBUG:
        print "this is first element to swap %d at index %d" % (swap1_value, swap1_index)

    #check if no need to swap
    if swap1_index == 0:
        if DEBUG:
            print "there is no need to swap, the list is already in ascending order"
        return(bool(1))


    #find location to swap it into
    index_count = 0
    for cur_iter in A:
        if cur_iter <= swap1_value:
            prev_iter = cur_iter
        else:
            if DEBUG:
                print "Found value at %d at index %d to put in swap1 %d" % (prev_iter, index_count -1, swap1_value)
            break

        index_count += 1


    #STEP3, do a swap and see if ascending values
    temp_value = A[swap1_index]
    A[swap1_index] = A[index_count -1]
    A[index_count -1 ] = temp_value
    if DEBUG:
        print "this is swapped A %s " % A

    #check for ascending
    return_flag = 1 
    prev_iter = -10000000
    for cur_iter in A:
        if prev_iter <= cur_iter:
            prev_iter = cur_iter
            return_flag = 1 
        else:
            return_flag = 0 
            break

    if DEBUG:
        print "this is return_flag %s" % bool(return_flag)
    return(bool(return_flag))



#result = solution([1, 5, 3, 3, 7])
#result = solution([1, 5, 3, 1, 3, 7])
result = solution([1, 3, 5])
print result


