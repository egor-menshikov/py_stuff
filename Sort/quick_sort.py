def quick_sort(list_):
    if len(list_) <= 1:
        return list_
    pivot = list_[0]
    left = [item for item in list_[1:] if item < pivot]
    right = [item for item in list_[1:] if item >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
