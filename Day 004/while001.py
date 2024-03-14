pv = 1000  # Present value
r = 0.04   # Interest rate

fv = pv * 2  # Future value (double the present value)
n = 0        # Initialize the number of periods (years)

# Calculate the number of years using the compound interest formula
while pv < fv:
    pv *= (1 + r)  # Calculate the future value after one year
    n += 1         # Increment the number of years

print(f"Future value: {pv:.2f} USD. Number of periods: {n} years")
