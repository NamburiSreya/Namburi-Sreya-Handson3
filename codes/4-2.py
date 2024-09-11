import time
import numpy as np
import matplotlib.pyplot as plt

def baseline_nested_loop(limit):
    """Execute a nested loop with a simple counter increment."""
    counter = 1
    for outer in range(1, limit + 1):
        for inner in range(1, limit + 1):
            counter += 1
    return counter

def enhanced_nested_loop(limit):
    """Execute a nested loop with additional operation."""
    primary_counter = 1
    secondary_value = 1
    for outer in range(1, limit + 1):
        for inner in range(1, limit + 1):
            primary_counter += 1
            secondary_value = outer + inner
    return primary_counter

input_range = np.arange(1, 10)
baseline_runtimes = np.zeros_like(input_range, dtype=float)
enhanced_runtimes = np.zeros_like(input_range, dtype=float)

for index, size in enumerate(input_range):
    start = time.time()
    baseline_nested_loop(size)
    baseline_runtimes[index] = time.time() - start

    start = time.time()
    enhanced_nested_loop(size)
    enhanced_runtimes[index] = time.time() - start

    print(f'Input size {size}: Baseline Time = {baseline_runtimes[index]:.6f}s, Enhanced Time = {enhanced_runtimes[index]:.6f}s')

plt.plot(input_range, baseline_runtimes, 'bo', label='Baseline Function')
plt.plot(input_range, enhanced_runtimes, 'go', label='Enhanced Function')
plt.legend()
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Runtime Comparison: Baseline vs Enhanced Nested Loops')
plt.show()

""" Output:
Input size 1: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 2: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 3: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 4: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 5: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 6: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 7: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 8: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
Input size 9: Baseline Time = 0.000000s, Enhanced Time = 0.000000s
"""