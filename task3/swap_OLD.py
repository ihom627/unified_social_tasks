# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7


    print "this is initial A %s " % A

    dict_index_value = {}

    #STEP1, put list into a hash 
    index_count = 0
    for iter in A:
        #index_count = A.index(iter)
        #print "this is array index %d" % (index)
        dict_index_value[index_count] = iter
        index_count += 1
        
    keylist = dict_index_value.keys()
    keylist.sort()
    for key in keylist:
        print "%s: %s" % (key, dict_index_value[key])

    #STEP2, find smallest value
    current_smallest_value = 1000000000
    current_smallest_index = 0 

    keylist = dict_index_value.keys()
    keylist.sort()
    for key in keylist:
        #print "%s: %s" % (key, dict_index_value[key])
        if dict_index_value[key] < current_smallest_value:
            current_smallest_value = dict_index_value[key]
            current_smallest_index = key

    print "this is the current_smallest_value %d at index %d" % (current_smallest_value, current_smallest_index)


    #STEP3, find second smallest value
    current_second_smallest_value = 1000000000
    current_second_smallest_index = 0

    keylist = dict_index_value.keys()
    keylist.sort()
    for key in keylist:
        #print "%s: %s" % (key, dict_index_value[key])
        if dict_index_value[key] < current_second_smallest_value and dict_index_value[key] > current_smallest_value:
            current_second_smallest_value = dict_index_value[key]
            current_second_smallest_index = key

    print "this is the current_second_smallest_value %d at index %d" % (current_second_smallest_value, current_second_smallest_index)






    #STEP3, do a swap of the smallest and largest values, and see if ascending values
#    temp_value = A[current_smallest_index]
#    A[current_smallest_index] = A[current_largest_index]
#    A[current_largest_index] = temp_value
#
#    print "this is swapped A %s " % A



solution([1, 5, 3, 3, 7])


