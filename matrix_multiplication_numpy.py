import numpy as np         # NumPy for numerical operations
import time                # time module to measure elapsed time

min_size = 2
max_size = 1002
step = 2

# Lists to store the matrix sizes and the corresponding times taken.
sizes = []
times = []

# Loop over the range of matrix sizes from min_size to max_size,
for n in range(min_size, max_size + 1, step):
    # Generate random nxn matrices A and B using NumPy's random.rand function.
    # Each element in A and B is a float in [0,1).
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    # Record the start time before performing the multiplication.
    start_time = time.time()

    # Perform the matrix multiplication using NumPy's @ operator.
    # NumPy uses optimized BLAS.
    C = A @ B

    # Record the end time after the multiplication.
    end_time = time.time()

    # Calculate the elapsed time as the difference between end_time and start_time.
    elapsed = end_time - start_time

    # Store the current matrix size and the elapsed time in the respective lists.
    sizes.append(n)
    times.append(elapsed)
