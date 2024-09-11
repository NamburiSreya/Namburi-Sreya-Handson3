def nested_loop_with_extra_op(size):
    """
    Perform nested loops with an additional operation.
    The extra operation doesn't affect the return value.
    """
    accumulator = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            accumulator += 1
            unused_sum = outer + inner  # This operation doesn't affect the result
    return accumulator

def simple_nested_loop(size):
    """
    Perform nested loops with a single increment operation.
    """
    counter = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            counter += 1
    return counter

# Test both functions with an input of 3
output_with_extra_op = nested_loop_with_extra_op(3)
output_simple = simple_nested_loop(3)

# Display the results
print("Result of nested loop with extra operation:", output_with_extra_op)
print("Result of simple nested loop:", output_simple)

"""Output:
Result of nested loop with extra operation: 10
Result of simple nested loop: 10"""
