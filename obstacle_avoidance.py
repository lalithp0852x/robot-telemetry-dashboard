"""Reactive obstacle-avoidance simulator for a differential-drive rover."""
import random

def choose_motion(left, front, right, safe=1.0):
    if front < safe:
        return ('TURN_LEFT', left > right) if left >= right else ('TURN_RIGHT', right > left)
    if left < safe: return 'TURN_RIGHT'
    if right < safe: return 'TURN_LEFT'
    return 'FORWARD'

print('ROVER OBSTACLE AVOIDANCE / SIMULATION')
for tick in range(1, 21):
    sensors = [round(random.uniform(.4, 3.0), 2) for _ in range(3)]
    action = choose_motion(*sensors)
    if isinstance(action, tuple): action = action[0]
    print(f'tick={tick:02d} left={sensors[0]:.2f}m front={sensors[1]:.2f}m right={sensors[2]:.2f}m -> {action}')
