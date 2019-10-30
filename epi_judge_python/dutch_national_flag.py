import functools
import ipdb

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    mid_index = pivot_index
    cursor = 0
    ipdb.set_trace()
    while cursor < len(A):
        print('Cursor at ', cursor)
        print('Pivot at ', pivot_index)
        print(A)
        if cursor == pivot_index:
            cursor += 1
            print('Cursor at pivot. Increasing the cursor')
            continue
        if A[cursor] > A[pivot_index] and cursor < pivot_index:
            A[cursor], A[pivot_index] = A[pivot_index], A[cursor]
            pivot_index = cursor
            cursor += 1
            print('Greater element in lower range.'
                  ' Swapping and putting pivot back')
            continue
        if A[cursor] < A[pivot_index] and cursor > pivot_index:
            A[cursor], A[pivot_index] = A[pivot_index], A[cursor]
            pivot_index = cursor
            cursor += 1
            print('Smaller element in greater range. Swapping '
                  'and putting pivot to front')
            continue
        if A[cursor] == A[pivot_index] and cursor != mid_index:
            A[cursor], A[mid_index] = A[mid_index], A[cursor]
            cursor += 1
            continue
        cursor += 1
        continue
        # if A[cursor] == A[pivot_index] and cursor == mid_index:
        #     mid_index += 1
    return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main("dutch_national_flag.py",
    #                                    'dutch_national_flag.tsv',
    #                                    dutch_flag_partition_wrapper))
    A = [1, 1, 0, 2]
    dutch_flag_partition(1, A)
    print(A)
