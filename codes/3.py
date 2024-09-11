import time
import numpy as np
import matplotlib.pyplot as plt

def nested_loop_operation(size):
    """Perform a nested loop operation that increments a counter."""
    counter = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            counter += 1
    return counter

input_sizes = np.arange(1, 101)
runtime_data = np.zeros_like(input_sizes, dtype=float)

for index, current_size in enumerate(input_sizes):
    start = time.time()
    nested_loop_operation(current_size)
    runtime_data[index] = time.time() - start

# Compute quadratic approximation
quadratic_params = np.polyfit(input_sizes, runtime_data, 2)
quadratic_curve = np.polyval(quadratic_params, input_sizes)

# Calculate cubic upper bound (Big-O)
cubic_params = np.polyfit(input_sizes, runtime_data, 3)
cubic_curve = np.polyval(cubic_params, input_sizes)
cubic_expression = np.poly1d(cubic_params)

# Determine linear lower bound (Big-Omega)
linear_params = np.polyfit(input_sizes, runtime_data, 1)
linear_curve = np.polyval(linear_params, input_sizes)
linear_expression = np.poly1d(linear_params)

# Display polynomial expressions
print("Quadratic Approximation:", np.poly1d(quadratic_params))
print("Cubic Upper Bound (Big-O):", cubic_expression)
print("Linear Lower Bound (Big-Omega):", linear_expression)

# Visualize results
plt.figure()
plt.plot(input_sizes, runtime_data, 'bo', label='Measured Runtimes')
plt.plot(input_sizes, quadratic_curve, 'r-', linewidth=2, label='Quadratic Fit')
plt.plot(input_sizes, cubic_curve, 'g--', linewidth=2, label='Cubic Upper Bound')
plt.plot(input_sizes, linear_curve, 'm--', linewidth=2, label='Linear Lower Bound')
plt.legend()
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Runtime Analysis with Bounds')
plt.show()

'''
Quadratic Approximation:            2
1.041e-08 x + 4.48e-06 x - 0.0001052
Cubic Upper Bound (Big-O):             3             2
-8.134e-09 x + 1.243e-06 x - 4.555e-05 x + 0.0003263
Linear Lower Bound (Big-Omega):  
5.531e-06 x - 0.0001231  '''