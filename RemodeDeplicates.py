# A simple function to remove duplicates from the list and return only unique values
def remove_duplicates(numbers):
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
