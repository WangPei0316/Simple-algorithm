def binary_search(list,item):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = int((start+end)/2)
        guess = list[mid]
        if guess < item:
            start = mid+1
        elif guess > item:
            end = mid-1
        else:
            return mid


mylist = [1,3,5,7,9]
print(binary_search(mylist,3))
