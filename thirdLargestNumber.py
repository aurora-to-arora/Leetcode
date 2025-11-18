def thirdLargest(arr):
    n = len(arr)
    
    # Sort the array 
    arr.sort()
    arr.reverse()
    uniq=[]
    for x in arr:
      if x not in uniq:
        uniq.append(x)
      if len(uniq)>=3:
        return uniq[2]
    return -1
      
     
if __name__ == "__main__":
    arr = [1, 14, 2, 16, 10, 20]
    print(thirdLargest(arr))
