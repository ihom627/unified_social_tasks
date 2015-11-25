# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(Y, A, B, W):
    # write your code in Python 2.7

    DEBUG = 0 

    if DEBUG:
        print "year = %d, month1 = %s, month2 = %s, week = %s" % (Y, A, B, W)
    
    leap_year = Y % 4
    if DEBUG:
        print "leap_year %d" % (leap_year)
    
    #list_days
    list_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if DEBUG:
        print "list_days %s " % list_days

    #calendar_days
    calendar_days = list_days * 53
    if DEBUG:
        print "calendar_days %s " % calendar_days
    
    #list_months
    list_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if DEBUG:
        print "list_months %s " %  list_months    

    #list_days_in_month_non_leap_year
    list_days_in_month_non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if DEBUG:
        print "list_days_in_month_non_leap_year %s " % list_days_in_month_non_leap_year
    
    #list_days_in_month_leap_year
    list_days_in_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if DEBUG:
        print "list_days_in_month_leap_year %s "  % list_days_in_month_leap_year


    #STEP1, calc the total day count index into the first day of the beginning month

    #get number of the day for the first week given month
    first_day_of_year_index = list_days.index(W)
    if DEBUG:
        print "this is the first day of the year index %d " % (first_day_of_year_index)

    for day_index in range(first_day_of_year_index, len(calendar_days)):
        if DEBUG:
            print "this is first day of the year %s " % calendar_days[day_index]

        monday_count = 0
        first_month_total_day_count = 0
        total_day_count = 1;
        total_day_week = "" 
        if leap_year != 0:
            for index in range(0, len(list_days_in_month_non_leap_year)):
                if DEBUG:
                    print "month %s has days %d" % (list_months[index], list_days_in_month_non_leap_year[index])
                for count in range(1, list_days_in_month_non_leap_year[index] + 1):
                    day_of_year = total_day_count
                    total_day_week = calendar_days[first_day_of_year_index + total_day_count - 1]
                    if DEBUG:
                        print "number of day of month is %d, total_day_count %d, total_day_week %s " % (count, total_day_count, calendar_days[first_day_of_year_index + total_day_count - 1])
                    
                    if A == list_months[index] and 1 <= count and 7 >= count and total_day_week == "Monday" :
                        if DEBUG:
                            print "A: This is beginning day count %d" % (total_day_count)
                        first_month_total_day_count = total_day_count

                    total_day_count += 1

        if leap_year == 0:
            for index in range(0, len(list_days_in_month_leap_year)):
                if DEBUG:
                    print "month %s has days %d" % (list_months[index], list_days_in_month_leap_year[index])
                for count in range(1, list_days_in_month_leap_year[index] + 1):
                    day_of_year = total_day_count
                    total_day_week = calendar_days[first_day_of_year_index + total_day_count - 1]
                    if DEBUG:
                        print "number of day of month is %d, total_day_count %d, total_day_week %s " % (count, total_day_count,
 calendar_days[first_day_of_year_index + total_day_count - 1])

                    if A == list_months[index] and 1 <= count and 7 >= count and total_day_week == "Monday" :
                        if DEBUG:
                            print "A: This is beginning day count %d" % (total_day_count)
                        first_month_total_day_count = total_day_count
                        monday_count += 1

                    total_day_count += 1


    #STEP2, calc the total day count index into the last day of the end month

    #get number of the day for the first week given month
    first_day_of_year_index = list_days.index(W)
    if DEBUG:
        print "this is the first day of the year index %d " % (first_day_of_year_index)

    for day_index in range(first_day_of_year_index, len(calendar_days)):
        if DEBUG: 
            print "this is first day of the year %s " % calendar_days[day_index]

        second_month_total_day_count = 0
        total_day_count = 1;

        if leap_year != 0:
            for index in range(0, len(list_days_in_month_non_leap_year)):
                if DEBUG:
                    print "month %s has days %d" % (list_months[index], list_days_in_month_non_leap_year[index])
                for count in range(1, list_days_in_month_non_leap_year[index] + 1):
                    day_of_year = total_day_count
                    total_day_week = calendar_days[first_day_of_year_index + total_day_count - 1]
                    if DEBUG:
                        print "number of day of month is %d, total_day_count %d, total_day_week %s " % (count, total_day_count,
 calendar_days[first_day_of_year_index + total_day_count - 1])

                    if B == list_months[index] and (list_days_in_month_non_leap_year[index] - 7)  <= count and list_days_in_month_non_leap_year[index] >= count and total_day_week == "Sunday" :
                        if DEBUG:
                            print "B: This is beginning day count %d" % (total_day_count)
                        second_month_total_day_count = total_day_count

                    total_day_count += 1

        if leap_year == 0:
            for index in range(0, len(list_days_in_month_leap_year)):
                if DEBUG:
                    print "month %s has days %d" % (list_months[index], list_days_in_month_leap_year[index])
                for count in range(1, list_days_in_month_leap_year[index] + 1):
                    day_of_year = total_day_count
                    total_day_week = calendar_days[first_day_of_year_index + total_day_count - 1]
                    if DEBUG:
                        print "number of day of month is %d, total_day_count %d, total_day_week %s " % (count, total_day_count, calendar_days[first_day_of_year_index + total_day_count - 1])

                    if B == list_months[index] and (list_days_in_month_leap_year[index] - 7)  <= count and list_days_in_month_leap_year[index] >= count and total_day_week == "Sunday" :
                        if DEBUG:
                            print "B: This is beginning day count %d" % (total_day_count)
                        second_month_total_day_count = total_day_count

                    total_day_count += 1


    #STEP3: calc difference between start and end
    number_mondays = 0
    for index_calendar_days in range(first_month_total_day_count, second_month_total_day_count):
        if calendar_days[index_calendar_days] == "Monday":
            number_mondays += 1
         
    if DEBUG:
        print "FINAL: number_mondays = %d " % (number_mondays) 
    return(number_mondays)






result = solution(2014, "April", "May", "Wednesday")
print result
#result = solution(2014, "January", "February", "Monday")



