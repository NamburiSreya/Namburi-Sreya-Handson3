import time
import numpy as np
import matplotlib.pyplot as plt

def nested_loop_counter(limit):
    """Increment a counter using nested loops."""
    total = 1
    for outer in range(1, limit + 1):
        for inner in range(1, limit + 1):
            total += 1
    return total

# Generate a sequence of input sizes
size_range = np.arange(1, 101)
duration_log = np.zeros_like(size_range, dtype=float)

# Measure execution time for each input size
for index, current_size in enumerate(size_range):
    start = time.time()
    nested_loop_counter(current_size)
    duration_log[index] = time.time() - start

# Plot the measured execution times
plt.plot(size_range, duration_log, 'bo', label='Data Points')

# Compute and plot a quadratic fit
quadratic_params = np.polyfit(size_range, duration_log, 2)
estimated_curve = np.polyval(quadratic_params, size_range)
plt.plot(size_range, estimated_curve, 'r-', linewidth=2, label='Fitted Curve')

# Add legend and display the plot
plt.legend()
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Runtime Analysis of Nested Loop Function')
plt.show()