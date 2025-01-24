
import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a basic line plot
plt.plot(x, y, label="Line 1", color="blue", marker="o")  # Plot the data

# Add labels and title
plt.xlabel("X-axis")          # Label for the X-axis
plt.ylabel("Y-axis")          # Label for the Y-axis
plt.title("Basic Line Plot")  # Title of the plot

# Add a legend
plt.legend()

# Show the plot
plt.show()
