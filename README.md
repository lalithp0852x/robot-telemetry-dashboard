# Robot Telemetry Dashboard

A polished, responsive robotics monitoring interface built for a simulated rover. It demonstrates frontend and real-time systems thinking relevant to robotics software and systems integration roles.

## Highlights

- Live simulated telemetry for velocity, battery, CPU, temperature, and signal strength
- Health checks for motor controller, IMU, lidar, and WebSocket link
- Responsive dashboard layout with motion telemetry chart
- WebSocket-ready component structure for connecting a real robot data stream

## Run locally

```bash
npm install
npm run dev
```

Open http://localhost:3000.

## Next steps

Replace the local simulation interval with a Node.js WebSocket service that publishes ROS2 or MQTT telemetry packets, then persist mission history in PostgreSQL.
