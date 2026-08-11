import React from 'react'
import { Brain, Inbox, ListChecks, FileText, AlertTriangle, Sparkles } from 'lucide-react'

const metrics = [
  { label: 'Priority Items', value: '2', icon: Inbox, detail: 'High focus items detected' },
  { label: 'Action Items', value: '5', icon: ListChecks, detail: 'From notes and inbox inputs' },
  { label: 'Risks', value: '3', icon: AlertTriangle, detail: 'Potential blockers to review' },
  { label: 'Briefs', value: 'Ready', icon: FileText, detail: 'Executive summary draft' },
]

export default function App() {
  return (
    <main className="shell">
      <section className="hero">
        <div>
          <p className="eyebrow">AI portfolio project</p>
          <h1>AI Productivity Command Center</h1>
          <p className="subtitle">A clean productivity dashboard that turns messages, notes and tasks into priorities, risks and executive-ready summaries.</p>
        </div>
        <div className="orb"><Brain size={58} /></div>
      </section>

      <section className="metrics">
        {metrics.map((item) => {
          const Icon = item.icon
          return (
            <article className="card" key={item.label}>
              <Icon size={28} />
              <h2>{item.value}</h2>
              <p className="label">{item.label}</p>
              <p className="muted">{item.detail}</p>
            </article>
          )
        })}
      </section>

      <section className="workspace">
        <div className="panel large">
          <div className="panelHeader"><Sparkles size={22} /><h2>Recommended Focus</h2></div>
          <ol>
            <li>Review urgent decision requests first.</li>
            <li>Confirm owners for open action items.</li>
            <li>Batch routine updates into one review window.</li>
          </ol>
        </div>
        <div className="panel">
          <h2>Product Idea</h2>
          <p>One command center for clearer priorities, faster summaries and better daily focus.</p>
        </div>
      </section>
    </main>
  )
}
