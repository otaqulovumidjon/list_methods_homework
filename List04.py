def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    n = numbers.pop(i)
    return n

print(main([1, 2, 3, 4, 2, 5, 6], 4)) 