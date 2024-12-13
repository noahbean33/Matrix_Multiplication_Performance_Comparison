# # **Matrix Multiplication Performance Comparison**

This repository contains the implementation and analysis of matrix multiplication using Python, C, and SystemVerilog. It explores the performance, scalability, and trade-offs between these methods for various matrix sizes.

---

## **Overview**
Matrix multiplication is a fundamental algorithm widely used in scientific computing, signal pprocessing, and machine learning. This project evaluates different implementations of matrix multiplication by comparing their execution times in order to assess the quantitive and qualitative trade-offs involved. 

---

## **Features**
1. **Implementations:**
   - **Python:** Basic triple-loop and optimized NumPy implementations.
   - **C:** Unoptimized and compiler-optimized (`-O3`) implementations.
   - **SystemVerilog:** Hardware-based implementation.

2. **Performance Analysis:**
   - Comparison across varying matrix sizes (2×2 to 1002×1002).
   - Execution time measurements and scalability evaluation in units of seconds.

3. **Trade-offs:**
   - Ease of implementation versus computational efficiency.
   - Hardware complexity versus software complexity.

4. **Challenges Addressed:**
   - Developing scalable HDL implementations for arbitrary matrix sizes.
   - Overcoming hardware synthesis limitations.

---

## **Files and Directory Structure**

### **Source Files**
- `python/`: Contains Python scripts for basic and NumPy-based implementations.
- `c/`: Includes C Program.
- `verilog/`: Contains the SystemVerilog modules and testbenches for HDL-based implementation.

### **Reports**
- `report.pdf`: Detailed analysis of implementation results, challenges, and lessons learned.
- `results/`: Contains raw data and plots comparing execution times.

---

## **How to Run**

### **1. Prerequisites**
- Python 3 with NumPy installed.
- GCC or any standard C compiler.
- Xilinx Vivado, EDA Playgrounnd, or any Verilog simulation tool.

### **2. Steps**
1. Clone the repository:
```bash
   git clone https://github.com/yourusername/matrix_multiplication_comparison.git
   cd matrix_multiplication_comparison
```

   ### **2. Steps**   
#### **Run Python implementations**:
   ```bash
cd python
python3 basic.py
python3 numpy.py
```

#### Run C implementations:
   ```bash
cd c
gcc -o basic basic.c
./basic
gcc -O3 -o optimized optimized.c
./optimized
   ```

#### Run SystemVerilog implementations:
   ```bash
cd SystemVerilog
xrun -sv -timescale 1ns/1ns -access +rw testbench.sv (Cadence Xcelium 23.09)
   ```

# Additional Details

**Assuming Cadence Xcelium 23.09 or similar tools.**

## Results

The performance evaluation highlighted the following:

- **Python (Basic):** Easy to implement but slow for large matrices.
- **NumPy:** Leveraged optimized C libraries for the fastest performance.
- **C (Optimized):** Balanced speed and control, suitable for most use cases.
- **SystemVerilog:** Achieved hardware-level parallelism, demonstrating excellent scalability and speed but with higher complexity.

For detailed graphs and analysis, see `report.pdf` in the repository.

---

## Lessons Learned

- Hardware-level parallelism is critical for scaling computationally intensive tasks.
- Simulation tools like Xilinx Vivado streamline rapid prototyping.
- Compiler optimizations significantly improve software performance with minimal effort.

---

## Future Work

- Implement floating-point support in HDL.
- Deploy on advanced FPGA hardware to confirm simulation results.
- Explore hybrid software-hardware approaches for computational efficiency.

---

## Contributions

Contributions to enhance the implementations or add new features are welcome! Please create a pull request or open an issue with your suggestions.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgments

Thanks to the authors of the referenced books, tools, and tutorials that supported this project.
