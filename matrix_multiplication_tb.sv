module matrix_multiplication_tb;
    logic [71:0] A, B;               // Test input matrices A and B (1D representation)
    logic [71:0] C;                  // Output matrix C (1D representation)
    logic Clock, reset, Enable;      // Control signals
    logic done;                      // Indicates when multiplication is complete
    logic [7:0] matC [2:0][2:0];     // Temporary 2D matrix for verification
    integer i, j;                    // Loop indices for verification
    parameter Clock_period = 10;     // Define the clock period (in time units)

    // Initial block for test stimulus
    initial begin
        Clock = 0;                   // Initialize clock to 0
        reset = 1;                   // Assert reset
        #100; reset = 0;             // De-assert reset after 100 ns
        #Clock_period;               // Wait for one clock period

        // Define input matrices A and B
        A = {8'd9, 8'd8, 8'd7, 8'd6, 8'd5, 8'd4, 8'd3, 8'd2, 8'd1}; // Row-major order
        B = {8'd1, 8'd9, 8'd8, 8'd7, 8'd6, 8'd5, 8'd4, 8'd3, 8'd2};
        Enable = 1;                  // Enable matrix multiplication
        wait(done);                  // Wait for the done signal
        #Clock_period;               // Wait for half a clock cycle

        // Verify output matrix by converting C to a 2D format
        foreach (matC[i, j]) begin
            matC[i][j] = C[(i * 3 + j) * 8 +: 8]; // Extract 8-bit elements
        end

        Enable = 0;                  // Disable multiplication
        #Clock_period;
        $stop;                       // End the simulation
    end

    // Generate a clock signal
    always #(Clock_period / 2) Clock = ~Clock;

    // Instantiate the DUT (Device Under Test)
    matrix_mult dut (
        .Clock(Clock),
        .reset(reset),
        .Enable(Enable),
        .A(A),
        .B(B),
        .C(C),
        .done(done)
    );
endmodule
