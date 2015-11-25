# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7

    DEBUG = 0 

    if DEBUG:
        print S 

    list_calls = S.split("\n") 
    if DEBUG:
        print list_calls

    phone_number_dict = {} 


    #STEP1: Iterate through first time to calculate total seconds for each phone number

    for call_iter in list_calls:

        individual_call_price = 0;
        individual_call_total_seconds = 0

        if DEBUG:
            print "call_iter is %s" % call_iter
        hours, mins, seconds_number = call_iter.split(":")
        if DEBUG:
            print "hours = %d, mins = %d, seconds_number = %s" % (int(hours), int(mins), seconds_number)
        seconds, phone_number = seconds_number.split(",")        
        if DEBUG:
            print "seconds = %d, phone_number = %s" % (int(seconds), phone_number)

        individual_call_total_seconds = 3600 * int(hours) + 60 * int(mins) + int(seconds) 
        if DEBUG:
            print "individual_call_total_seconds = %d" % individual_call_total_seconds

        #if call less than 5 mins
        if 5 > int(mins):
            individual_call_price =  3 * (60 * int(mins) + int(seconds))
        else: #if call atleast 5 mins
            individual_call_price = 150 * int(mins)
            if int(seconds) > 0: #add another 150 for a partial minute
                individual_call_price += 150
        
        if DEBUG: 
            print "individual_call_price = %d" % (individual_call_price)

        #insert into dict if length of call 
        if phone_number in phone_number_dict:
            phone_number_dict[phone_number] += individual_call_total_seconds
        else:
            phone_number_dict[phone_number] = individual_call_total_seconds

        if DEBUG:
            print "\n\n"



    #STEP2, find the phone number with the largest total number of seconds
    #find the largest total number of seconds 
    largest_total_sec = 0
    if DEBUG:
        print "This is phone_number_dict"
    keylist = phone_number_dict.keys()
    for key in keylist:
        if DEBUG:
            print "phone_number_dict %s: %s" % (key, phone_number_dict[key])
        if largest_total_sec < int(phone_number_dict[key]) :
            largest_total_sec = int(phone_number_dict[key])

    if DEBUG:
        print "this is the largest total number of seconds %d" % (largest_total_sec)

    #now check if there are multiple numbers with the larget total number of sec 
    phone_number_with_smallest_total_val = ""
    val1 = 0
    val2 = 0
    val3 = 0
    total_val = 0
    current_smallest_total_val = 100000000000000 

    keylist = phone_number_dict.keys()
    for key in keylist:
        if DEBUG: 
            print "phone_number_dict %s: %s" % (key, phone_number_dict[key])
        if largest_total_sec == int(phone_number_dict[key]) :
            val1, val2, val3 = key.split("-") 
            total_val = int(val1) + int(val2) + int(val3)
            if DEBUG:
                print "this is total_val %d" % (total_val)
            if total_val < current_smallest_total_val:
                 current_smallest_total_val = total_val
                 phone_number_with_smallest_total_val = key

            
    if DEBUG:
        print "this is phone_number with largest total number of secs, but the smallest numerical value in case of tie %s" % phone_number_with_smallest_total_val 



    #STEP3: Iterate through second time and ignore the phone number with the highest number of secs 

    total_call_price = 0
    for call_iter in list_calls:

        individual_call_price = 0;
        individual_call_total_seconds = 0

        if DEBUG:
            print "call_iter is %s" % call_iter
        hours, mins, seconds_number = call_iter.split(":")
        if DEBUG:
            print "hours = %d, mins = %d, seconds_number = %s" % (int(hours), int(mins), seconds_number)
        seconds, phone_number = seconds_number.split(",")        
        if DEBUG:
            print "seconds = %d, phone_number = %s" % (int(seconds), phone_number)

        individual_call_total_seconds = 3600 * int(hours) + 60 * int(mins) + int(seconds) 
        if DEBUG:
            print "individual_call_total_seconds = %d" % individual_call_total_seconds

        #if call less than 5 mins
        if 5 > int(mins):
            individual_call_price =  3 * (60 * int(mins) + int(seconds))
        else: #if call atleast 5 mins
            individual_call_price = 150 * int(mins)
            if int(seconds) > 0: #add another 150 for a partial minute
                individual_call_price += 150
        
        if DEBUG:
            print "individual_call_price = %d" % (individual_call_price)

        #check if should ignore the phone number
        if phone_number != phone_number_with_smallest_total_val: 
            total_call_price += individual_call_price

        if DEBUG:
            print "\n\n"

    if DEBUG:
        print "this is total_call_price %d" % (total_call_price)
    return(total_call_price)



result = solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090")
print result


