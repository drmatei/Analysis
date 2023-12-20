import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the function f(x) = 1/2 * x^T * A * x
def f(x, A):
    return 0.5 * np.dot(x.T, np.dot(A, x))


# Calculate the gradient of f(x)
def gradient(x, A):
    return np.dot(A, x)


A = np.array([[2, 1],
              [1, 3]])

# Generate a grid of points for plotting
x_range = np.linspace(-5, 5, 100)
y_range = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x_range, y_range)
z = np.array([[f(np.array([xi, yi]), A) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(x, y)])

# Choose three points for gradient calculation
points = np.array([[2, 2], [-3, 4], [4, -3]])

# Create the figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.7, rstride=100, cstride=100)

# Plot contour lines
ax.contour(x, y, z, zdir='z', offset=np.min(z), cmap='viridis', linestyles="solid")

# Plot gradient at three different points
for point in points:
    grad = gradient(point, A)
    ax.quiver(point[0], point[1], f(point, A), grad[0], grad[1], 0, color='red', label='Gradient', length=0.5)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X)')
ax.set_title('3D Surface Plot with Contour Lines and Gradient')

# Show the plot
plt.show()
