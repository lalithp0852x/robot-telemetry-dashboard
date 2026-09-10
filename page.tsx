'use client'
import { useEffect, useState } from 'react'
import { Activity, Battery, Cpu, Gauge, Radio, Wifi } from 'lucide-react'

type Telemetry = { speed:number; battery:number; temperature:number; cpu:number; signal:number }
const initial: Telemetry = { speed: 1.42, battery: 87, temperature: 38.4, cpu: 31, signal: 96 }
export default function Dashboard() {
  const [data, setData] = useState(initial)
  const [connected, setConnected] = useState(true)
  useEffect(() => { const id=setInterval(() => setData(d => ({...d, speed: +(1.1+Math.random()*.7).toFixed(2), temperature:+(37+Math.random()*3).toFixed(1), cpu:Math.round(25+Math.random()*18), signal:Math.round(92+Math.random()*7)})), 1200); return () => clearInterval(id) }, [])
  const cards = [{label:'Linear velocity',value:`${data.speed} m/s`,icon:<Gauge/>},{label:'Battery level',value:`${data.battery}%`,icon:<Battery/>},{label:'CPU usage',value:`${data.cpu}%`,icon:<Cpu/>},{label:'Signal strength',value:`${data.signal}%`,icon:<Wifi/>}]
  return <main><header><div className="brand"><Radio size={22}/><span>ROVER<span className="accent">·01</span></span></div><div className="status"><i className={connected?'online':''}/>{connected?'SYSTEM ONLINE':'DISCONNECTED'}<button onClick={()=>setConnected(!connected)}>{connected?'Disconnect':'Reconnect'}</button></div></header>
    <section className="hero"><div><p className="eyebrow">MISSION CONTROL / LIVE TELEMETRY</p><h1>Robot Telemetry Dashboard</h1><p className="muted">Monitor rover health, motion, and onboard compute in real time.</p></div><div className="updated">LAST PACKET<br/><strong>just now</strong></div></section>
    <section className="grid">{cards.map(c=><article className="card" key={c.label}><div className="cardtop"><span>{c.label}</span><span className="icon">{c.icon}</span></div><strong>{c.value}</strong><div className="bar"><span style={{width:`${c.label==='Battery level'?data.battery:c.label==='Signal strength'?data.signal:Math.min(100,data.cpu*2)}%`}}/></div></article>)}</section>
    <section className="lower"><article className="panel chart"><div className="panelhead"><div><p className="eyebrow">MOTION TELEMETRY</p><h2>Velocity over time</h2></div><span className="live"><i className="online"/> LIVE</span></div><div className="chartarea"><div className="ylabels"><span>2.0</span><span>1.5</span><span>1.0</span><span>0.5</span><span>0</span></div><svg viewBox="0 0 700 220" preserveAspectRatio="none"><path className="gridline" d="M0 20H700M0 70H700M0 120H700M0 170H700M0 215H700"/><path className="line" d="M0 150 C45 140 60 165 100 125 S155 105 190 130 S240 70 280 110 S330 145 370 90 S420 100 455 75 S510 105 545 60 S600 85 640 40 S680 65 700 35"/></svg></div><div className="xlabels"><span>10:32</span><span>10:36</span><span>10:40</span><span>10:44</span><span>10:48</span></div></article>
      <article className="panel"><div className="panelhead"><div><p className="eyebrow">HEALTH CHECK</p><h2>Onboard systems</h2></div><Activity className="green"/></div><div className="checks">{[['Motor controller','Nominal'],['IMU / orientation','Nominal'],['Lidar sensor','Nominal'],['WebSocket link','Connected']].map(x=><div className="check" key={x[0]}><i className="online"/><span>{x[0]}</span><b>{x[1]}</b></div>)}</div><div className="note">Telemetry is simulated locally to demonstrate a real-time monitoring workflow.</div></article></section>
    <footer>ROVER·01 / SIMULATION MODE <span>WebSockets-ready architecture · Built with Next.js + TypeScript</span></footer></main>
}
