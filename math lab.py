name = "Lý Thị Hoàng Yến"
student_id = 2601766
date_returned = "04.03.2026"

from IPython.display import Markdown, display
import numpy as np
import matplotlib.pyplot as plt
import labx as mx

# Create the x array with a step size of 0.001
# It must range from -10 to 10
x = np.arange(-10, 10, 0.001)

# Calculate y values using the provided function and your student_id
y = mx.lab_1_problem_1(x, student_id)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)

# Add labels and formatting for a professional look
plt.title(f"Function f(x) for student {student_id}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True) # Helps locate where the function crosses y=0

plt.show()


# Example for one of the intersection points
# You will need to adjust xlim and ylim based on where your graph crosses y=1
plt.figure(figsize=(7, 5))
plt.plot(x, y)

# Adjust these limits based on the visual inspection of your graph
plt.xlim(-7.5, -6.5)
plt.ylim(0, 2)

# Add the y=1 line for clear visualization
plt.axhline(y=1, color='r', linestyle='--')

plt.title('Point 1 - Zoomed view')
plt.grid(True)
plt.show()

# Zoomed graph for Point 1
plt.figure(figsize=(7, 5))
plt.plot(x, y)

# ADJUST THESE LIMITS to focus on where your graph crosses y=1
plt.xlim(-7.5, -6.5) # Change these numbers based on your graph
plt.ylim(0, 2)       # Ensure this includes 0 and 1

# Show the y=1 line
plt.axhline(y=1, color='r', linestyle='--')

plt.title('Point 1 - Zoomed view')
plt.grid(True)
plt.show()