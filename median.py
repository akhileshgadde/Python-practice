# Find the median from given list of numbers

def median(list):
    list.sort()
    print list
    median = 0
    if len(list) % 2 == 0:
        print list[len(list)/2 -1], list[len(list)/2]
        median = float(list[len(list)/2 - 1] + list[len(list)/2] ) / 2
    else:
        median = list[len(list)/2]
    return median

median([4,5,5,4])
