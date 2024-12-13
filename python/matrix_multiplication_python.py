import random      # For generating random numbers
import time        # For measuring the time taken

def generate_random_matrix(n):
    """
    Generate an nxn matrix filled with random float elements
    between 0 and 1
    """
    return [[random.random() for _ in range(n)] for _ in range(n)]

def matrix_multiply(A, B):
    """
    Multiply two nxn matrices A and B
    """
    n = len(A)
    # Initialize the result matrix C with zeros
    C = [[0.0 for _ in range(n)] for _ in range(n)]
    # Triple nested loop for matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Set the minimum size, maximum size, and step size for n
min_size = 2
max_size = 1002  
step = 2

# Lists to store the matrix sizes and corresponding times
sizes = []
times = []

# Loop over the range of matrix sizes
for n in range(min_size, max_size + 1, step):
    # Generate random nxn matrices A and B
    A = generate_random_matrix(n)
    B = generate_random_matrix(n)

    # Measure the time taken to multiply the matrices
    start_time = time.time()
    C = matrix_multiply(A, B)
    end_time = time.time()

    # Compute the elapsed time for this multiplication
    elapsed = end_time - start_time

    # Store the results in the lists
    sizes.append(n)
    times.append(elapsed)
