def your_sort(unsorted):
    """Write this first.  Don't look up sorting algorithms beforehand.  It's
    good to reason through it yourself first.

    Normally, you'd just use the built in sorted function like I have here, but
    since this is an exercise in learning sorting algorithms, don't use it! ;P
    """
    return sorted(unsorted) # Change this. 

def bubble_sort(unsorted):
    return unsorted

def insertion_sort(unsorted):
    return unsorted

def sort(unsorted_list):
    """Sort takes any list and returns a sorted list.

    Uncomment the algorithm you're working on, and comment the rest. Run the
    test suite to check your implemeintation.
    """
    # Make a copy so we don't modify the original list. [:] makes a copy.
    unsorted = unsorted_list[:] # the [:] is syntax for a "slice" operation.
    
    # Sort
    result = your_sort( unsorted )
    # result = bubble_sort(unsorted)
    # result = insertion_sort(unsorted)
    return result 
