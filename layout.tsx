import './globals.css'
import type { Metadata } from 'next'
export const metadata: Metadata = { title: 'Robot Telemetry Dashboard', description: 'Real-time robotics telemetry monitoring interface' }
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body>{children}</body></html> }
