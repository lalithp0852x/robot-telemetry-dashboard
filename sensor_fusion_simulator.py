"""Educational 2D sensor-fusion demo using a simple Kalman filter.
Run: python sensor_fusion_simulator.py
"""
import random

def update(x, p, measurement, measurement_noise=4.0, process_noise=0.05):
    p += process_noise
    gain = p / (p + measurement_noise)
    x += gain * (measurement - x)
    p *= 1 - gain
    return x, p

position, uncertainty = 0.0, 1.0
true_position = 0.0
print("step | true position | lidar | fused estimate | uncertainty")
for step in range(1, 31):
    true_position += 1.0
    lidar = true_position + random.gauss(0, 2.0)
    position, uncertainty = update(position + 1.0, uncertainty, lidar)
    print(f"{step:>4} | {true_position:>13.2f} | {lidar:>5.2f} | {position:>14.2f} | {uncertainty:>11.2f}")
