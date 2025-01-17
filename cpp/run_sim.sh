#!/bin/bash

# Compile the C++ files
g++ -std=c++11 test_wind_turbine.cpp wind_turbine.cpp -o wind_turbine_test

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Running the program..."
    # Run the compiled program
    ./wind_turbine_test
else
    echo "Compilation failed. Please check your code for errors."
fi
