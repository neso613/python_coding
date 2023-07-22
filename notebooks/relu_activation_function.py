import numpy as np

def relu(x):
    return np.maximum(0, x)


input_data = np.array([-2, -1, 0, 1, 2])
output_data = relu(input_data)
print("Output after applying ReLU activation:", output_data)
