# Import 3D module
from vpython import *

# Create 3D model
scene = canvas(title = "均速直線運動", width = 800, height = 600, x = 0, y = 0, center = vec(0, 0.1, 0), color = color.blue)

# Create flat plane
base = box(pos = vector(0, 0, 0), size = vector(1, 0.01, 0.5), color = color.blue)

# Create moving object
block = box(pos = vector(-0.45, 0.055, 0), size = vector(0.1, 0.1, 0.1), color = color.red)

# Create graph
gd = graph(title = "位置時間曲線", width = 800, height = 400, x = 0, y = 600, xtitle = "時間 (s)", ytitle = "位置 (m)")
xt = gcurve(graph = gd, color = color.red)

gd2 = graph(title = "速度時間曲線", width = 800, height = 450, x = 0, y = 1050, xtitle = "時間 (s)", ytitle = "速度 (m/s)")
vt = gcurve(graph = gd2, color = color.red)

# Define arrow and label
vector_v = arrow(color = color.yellow, shaftwidth = 0.01)  # Arrow for velocity
v_label = label(text = "V", htight = 30, opacity = 0, box = False)  # Label for velocity

vector_scale = 10

# Setting initial state and physic condition
v = 0.03
t = 0
dt = 0.001

# Simulation
while(block.pos.x <= 0.45):
    rate(1000)
    block.pos.x = block.pos.x + v*dt  # New position based on velocity

    xt.plot(t, block.pos.x)  # Plot position and time
    vt.plot(t, v)      # Plot velocity and time

    vector_v.pos = block.pos     # Set the position of velocity arrow
    vector_v.axis = vector(v, 0, 0)*vector_scale   # Set the size of arrow of velocity
    v_label.pos = vector_v.pos + 1.2*vector_v.axis   # Set position of label of velocity

    t = t + dt

# Print the exercise duration time
print("t = ", t)

    
