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

    #first iteration
    for x in range(0, len(array)):
        #initialize total
        
        
        #second interator
        for i in range(x, len(array)):
            total = 0
            #sum total
            for y in range(x, i):
                total += array[y]
            
            #if sum is larger than max_sum, set new max_sum
            if total > max_sum:
                max_sum = total
                
                #this line tells you the values in your max array
                sum_arr = [j for j in array[x:i+1]]

    return max_sum, sum_arr

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
    
def d_and_c(arr, max_sum):
    
    if len(arr) == 1:
        return max_sum
    else:
        mid = int(len(arr)/2)
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        
        sum1 = 0
        max_sum1 = 0
        for x in range(len(arr1)-1, -1, -1):
            sum1 += arr1[x]
            max_sum1 = max(max_sum1, sum1)
            
        sum2 = 0
        max_sum2 = 0
        for x in range(0, len(arr2)):
            sum2 += arr2[x]
            max_sum2 = max(max_sum2, sum2)
            
        sum3 = max_sum1 + max_sum2
        
        max_sum = max(max_sum, max_sum1, max_sum2, sum3)
            
        return max(d_and_c(arr[:mid], max_sum), d_and_c(arr[mid:], max_sum))
        
          
def enumerate_test(test_packet):
    max_vals = []
    #max_arrs = []
    
    for line in test_packet:
        #mx_val, mx_arr = enumerate_case(line)
        mx_val = better_enumerate_case(line)
        max_vals.append(mx_val)
        #max_arrs.append(mx_arr)
        
    return max_vals
    
def linear_time(arr):
    
    max_sum = 0
    total = 0
    i = 0
    for j in range(i, len(arr)):
        
        
        
        
test_data = file_reader()
    
val = d_and_c(test_data[0], 0)

max_vals = enumerate_test(test_data)