"""Forward kinematics for a 2-link planar robotic arm."""
import math

def forward_kinematics(lengths, angles):
    x = y = heading = 0.0
    joints = [(x, y)]
    for length, angle in zip(lengths, angles):
        heading += math.radians(angle)
        x += length * math.cos(heading)
        y += length * math.sin(heading)
        joints.append((round(x, 3), round(y, 3)))
    return joints

links = [1.0, 0.7]
for angles in [(30, 45), (60, -20), (90, 30)]:
    print(f'angles={angles} -> joints={forward_kinematics(links, angles)}')
