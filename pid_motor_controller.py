"""PID motor-speed controller simulation for closed-loop robotics control."""
import math

target = 1.0
current, integral, previous_error = 0.0, 0.0, 0.0
kp, ki, kd = 2.0, 0.35, 0.15
dt = 0.1
print('time | target | speed | control | error')
for step in range(1, 61):
    error = target - current
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = kp * error + ki * integral + kd * derivative
    current += (control - 0.25 * current) * dt
    previous_error = error
    print(f'{step*dt:4.1f} | {target:6.2f} | {current:5.2f} | {control:7.2f} | {error:5.2f}')
