import os

def file_reader():
    with open("MSS_TestProblems.txt", 'r') as f:
        temp_data = f.readlines()
    f.close()
    test_data = []
    for line in temp_data:
        line = line.strip().strip(']').strip('[')
        test_data.append([int(x.strip()) for x in line.split(',')])
    
    return test_data
    
def enumerate_case(array):
    max_sum = 0

    for x in range(0, len(array)):
        total = 0
        
        for i in range(x, len(array)):
            
            total += array[i]
            if total > max_sum:
                max_sum = total
                sum_arr = [j for j in array[x:i+1]]
            

    return max_sum, sum_arr
    
def d_and_c(arr, max_sum):
    
    if len(arr) == 1:
        return max_sum
    else:
        mid = int(len(arr)/2)
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        sum3 = sum(arr1) + sum(arr2)
        
        max_sum = max(max_sum, sum1, sum2, sum3)
            
        return max(d_and_c(arr[:mid], max_sum), d_and_c(arr[mid:], max_sum))
        
        
    
def enumerate_test(test_packet):
    max_vals = []
    max_arrs = []
    
    for line in test_packet:
        mx_val, mx_arr = enumerate_case(line)
        max_vals.append(mx_val)
        max_arrs.append(mx_arr)
        
    return max_vals, max_arrs
        
test_data = file_reader()
    
val = d_and_c(test_data[0], 0)

max_vals, max_arrs = enumerate_test(test_data)