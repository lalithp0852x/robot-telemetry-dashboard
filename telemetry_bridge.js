/** Dependency-free telemetry bridge prototype.
 * Replace the stdin source with MQTT/ROS2/WebSocket adapters in production.
 */
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
console.log('TELEMETRY BRIDGE ONLINE | waiting for JSON packets');
rl.on('line', line => {
  try {
    const packet = JSON.parse(line);
    if (!packet.robotId || typeof packet.timestamp !== 'number') throw new Error('robotId and numeric timestamp are required');
    const normalized = { robotId: packet.robotId, timestamp: packet.timestamp, pose: packet.pose ?? null, sensors: packet.sensors ?? {}, receivedAt: Date.now() };
    console.log(JSON.stringify({ topic: `robots/${packet.robotId}/telemetry`, payload: normalized }));
  } catch (error) { console.error(JSON.stringify({ error: error.message, input: line })); }
});
