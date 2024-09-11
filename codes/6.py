def merge_sort(sequence):
    """Implement the merge sort algorithm to sort a sequence."""
    if len(sequence) > 1:
        midpoint = len(sequence) // 2
        left_half = sequence[:midpoint]
        right_half = sequence[midpoint:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index = merged_index = 0

        # Merge the sorted halves
        while True:
            if left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] < right_half[right_index]:
                    sequence[merged_index] = left_half[left_index]
                    left_index += 1
                else:
                    sequence[merged_index] = right_half[right_index]
                    right_index += 1
                merged_index += 1
            else:
                break

        # Handle remaining elements in left half
        while left_index < len(left_half):
            sequence[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1

        # Handle remaining elements in right half
        while right_index < len(right_half):
            sequence[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

# Test the merge sort algorithm
unsorted_data = [5, 2, 4, 7, 1, 3, 2, 6]
print("Unsorted Sequence:", unsorted_data)

merge_sort(unsorted_data)

print("Sorted Sequence:", unsorted_data)

'''Output:
Unsorted Sequence: [5, 2, 4, 7, 1, 3, 2, 6]
Sorted Sequence: [1, 2, 2, 3, 4, 5, 6, 7]
'''