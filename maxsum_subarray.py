def find_max_crossing_subarray(a,low,mid,high):
    left_sum = -99999
    Sum = 0
    for i in range(mid,low-1,-1):
        Sum += a[i]
        if Sum > left_sum:
            left_sum = Sum
            max_left = i 
            
    right_sum = -99999 
    Sum = 0
    for j in range(mid,high+1):
        Sum += a[j]
        if Sum > right_sum:
            right_sum = Sum
            max_right = j
            
    return max_left,max_right,left_sum+right_sum

def maximum_subarray(a,low,high):
    if high==low:
        return low,high,a[low]
    
    else:
        mid = (low+high)/2 
        left_low,left_high,left_sum = maximum_subarray(a,low,mid)
        right_low,right_high,right_sum = maximum_subarray(a,mid+1,high)
        cross_low,cross_high,cross_sum = find_max_crossing_subarray(a,low,mid,high)
        
        if left_sum >= max(right_sum,cross_sum):
            return left_low,left_high,left_sum
        elif right_sum >= max(cross_sum,left_sum):
            return right_low,right_high,right_sum
        else:
            return cross_low,cross_high,cross_sum
        

if __name__ == '__main':
    a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    a,b,c = maximum_subarray(a,0,len(a))
    print(a," ",b," ",c)