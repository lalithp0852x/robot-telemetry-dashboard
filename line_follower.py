"""Dependency-free line-following controller using three virtual reflectance sensors."""
def steering(left, center, right):
    error = (right - left) / max(left + center + right, 0.001)
    if center < 0.25 and left < 0.25 and right < 0.25: return 'SEARCH'
    correction = round(error * 2.0, 2)
    return {'error': correction, 'left_motor': round(1.0 + correction, 2), 'right_motor': round(1.0 - correction, 2)}

samples = [(0.8, 0.2, 0.1), (0.3, 0.9, 0.2), (0.1, 0.4, 0.8), (0.1, 0.1, 0.1)]
print('LINE FOLLOWER / SENSOR-TO-MOTOR OUTPUT')
for sensors in samples: print(f'sensors={sensors} -> {steering(*sensors)}')
