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

# Generate a range of input sizes
input_range = np.arange(1, 101)
runtime_measurements = np.zeros_like(input_range, dtype=float)

# Measure execution time for each input size
for index, size in enumerate(input_range):
    start = time.time()
    nested_loop_counter(size)
    runtime_measurements[index] = time.time() - start

# Visualize the runtime data
plt.plot(input_range, runtime_measurements, 'bo', label='Observed Runtimes')

# Compute quadratic best-fit curve
quadratic_coeffs = np.polyfit(input_range, runtime_measurements, 2)
estimated_curve = np.polyval(quadratic_coeffs, input_range)
plt.plot(input_range, estimated_curve, 'r-', linewidth=2, label='Quadratic Approximation')

# Identify the point where actual runtime exceeds the estimated curve
divergence_point = np.argmax(runtime_measurements > estimated_curve)

# Extract and display the critical values
critical_size = input_range[divergence_point]
critical_runtime = runtime_measurements[divergence_point]

print(f"Estimated critical input size: {critical_size}")
print(f"Runtime at critical size: {critical_runtime} seconds")

# Highlight the critical point on the plot
plt.axvline(x=critical_size, color='g', linestyle='--', label='Critical Size')

plt.legend()
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Runtime Analysis with Critical Point')
plt.show()


""" Output:
Estimated critical input size: 28
Runtime at critical size: 0.015628337860107422 seconds
"""