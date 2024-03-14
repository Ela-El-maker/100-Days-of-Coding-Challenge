# Step 1: Define the starting point
w_0 = -1

# Step 2: Define the maximum number of iterations
max_iters = 10000

# Step 3: Define the variable to control the step size
previous_step_size = 1

# Step 4: Define the learning rate
learning_rate = 0.01

# Step 5: Define the precision
precision = 0.000001

# Step 6: Define the derivative of the function
derivative = lambda w: 2 * w - 4

# Initialize the iteration counter
iters = 0

# Stochastic gradient descent algorithm
while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_0 - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1

# Print the result
print(f"A local minimum in point: {w_0:.2f}")
