def file_reader():
    #open file, read in all the lines
    with open("MSS_TestProblems.txt", 'r') as f:
        temp_data = f.readlines()
    f.close()
    #create array for data
    test_data = []
    
    #strip out all the syntax and split strings into lines
    for line in temp_data:
        line = line.strip().strip(']').strip('[')
        test_data.append([int(x.strip()) for x in line.split(',')])
    
    #return test data
    return test_data

def enumerate_case(array):
    
    #initialize max sum
    max_sum = 0
    max_array = []
    #first iteration
    for x in range(0, len(array)):
        #initialize total
        
        
        #second interator
        for i in range(x, len(array)):
            total = 0
            array_test = []
            #sum total
            for y in range(x, i):
                total += array[y]
                array_test.append(array[y])
                
            #if sum is larger than max_sum, set new max_sum
            if total > max_sum:
                max_sum = total
                max_array = array_test

    return max_sum, max_array

#I think this is actually the better enum case?
def better_enumerate_case(array):
    
    #initialize max sum
    max_sum = 0

    #first iteration
    for x in range(0, len(array)):
        #initialize total
        total = 0
        
        #second interator
        for i in range(x, len(array)):
            
            #sum total
            total += array[i]
            
            #if sum is larger than max_sum, set new max_sum
            if total > max_sum:
                max_sum = total
                
                #this line tells you the values in your max array
                sum_arr = [j for j in array[x:i+1]]
                
                
    return max_sum, sum_arr
    
def d_and_c(arr, max_sum, max_arr):
    
    if len(arr) == 1:
        return max_sum, max_arr
        
    else:
        mid = int(len(arr)/2)
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        
        sum1 = 0
        max_sum1 = 0
        val_arr1 = []
        max_arr1 = []
        for x in range(len(arr1)-1, -1, -1):
            sum1 += arr1[x]
            val_arr1.append(arr1[x])
            if max_sum1 < sum1:
                max_sum1 = sum1
                max_arr1 = val_arr1[::-1]
            
        sum2 = 0
        max_sum2 = 0
        val_arr2 = []
        max_arr2 = []
        for x in range(0, len(arr2)):
            sum2 += arr2[x]
            val_arr2.append(arr2[x])
            if max_sum2 < sum2:
                max_sum2 = sum2
                max_arr2 = val_arr2[:]
            
        sum3 = max_sum1 + max_sum2
        max_arr3 = max_arr1 + max_arr2
        
        if max_sum1 > max_sum:
            max_sum = max_sum1
            max_arr = max_arr1
            
        if max_sum2 > max_sum:
            max_sum = max_sum2
            max_arr = max_arr2
            
        if sum3 > max_sum:
            max_sum = sum3
            max_arr = max_arr3
                
        return max(d_and_c(arr[:mid], max_sum, max_arr), d_and_c(arr[mid:], max_sum, max_arr))
        
          
def enumerate_test(test_packet):
    max_vals = []
    max_arrs = []
    
    for line in test_packet:
        mx_val, mx_arr = linear_time(line)
        max_vals.append(mx_val)
        max_arrs.append(mx_arr)
        
    return max_vals, max_arrs
    
def linear_time(arr):
    
    max_sum = 0
    total = 0
    sum_array = []
    start = 0
    stop = 0
    
    for j in range(0, len(arr)):
        total += arr[j]
        if arr[j] > total:
            total = arr[j]
            start = j
            
        if total > max_sum:
            max_sum = total
            stop = j
            
            
    sum_array = [arr[x] for x in range(start, stop+1)]

            
    return max_sum, sum_array
        
        
        
test_data = file_reader()
testar = []
val, val2 = d_and_c(test_data[0], 0, testar)

max_vals, max_arrs = enumerate_test(test_data)
