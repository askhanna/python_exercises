import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def plot_circle_with_lines(N, p):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Set axis to be equal and remove ticks
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Generate N equally spaced angles around a circle
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    
    # Compute the (x, y) coordinates of each point on the circle
    points = np.array([(np.cos(angle), np.sin(angle)) for angle in angles])
    
    # Plot the points (dots) on the circumference of the circle
    for point in points:
        ax.plot(point[0], point[1], 'o', markersize=5, color='blue')
    
    # For each pair of points, draw a line with probability p
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < p:
                ax.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], color='gray', lw=0.5)

    # Set limits to ensure the circle is fully visible
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <N> <p>")
        sys.exit(1)
    
    # Parse command-line arguments
    N = int(sys.argv[1])
    p = float(sys.argv[2])
    
    # Check if the probability is valid
    if not (0 <= p <= 1):
        print("Error: p should be between 0 and 1")
        sys.exit(1)
    
    # Plot the circle with lines based on the arguments
    plot_circle_with_lines(N, p)
