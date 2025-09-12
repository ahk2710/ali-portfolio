<style>
:root { --bg:#0b1220; --text:#e9eef7; --muted:#9aa7b7; --accent:#3b82f6; --card:#111827; }
*{box-sizing:border-box}
body{font-family:-apple-system,Segoe UI,Inter,Roboto,Arial,sans-serif;line-height:1.5}
a{color:var(--accent);text-decoration:none;font-weight:600}
.hero{margin:16px 0;padding:24px;border-radius:16px;background:linear-gradient(135deg,#0b1220,#101826);color:var(--text);display:flex;gap:18px;align-items:center;border:1px solid #1f2937}
.hero img{width:72px;height:72px}
.btn{display:inline-block;padding:10px 14px;border-radius:10px;background:var(--accent);color:#fff;margin-right:8px}
.btn.secondary{background:transparent;border:1px solid var(--accent);color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.card{background:var(--card);color:var(--text);border:1px solid #1f2937;border-radius:16px;padding:16px}
.card img{width:100%;border-radius:12px;margin-top:10px}
.tags{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}
.tag{background:#0f172a;border:1px solid #263043;color:#cbd5e1;border-radius:999px;padding:4px 10px;font-size:12px}
.section{margin:24px 0}
.muted{color:var(--muted)}
</style>

<div class="hero">
  <img src="assets/plane.svg" alt="plane">
  <div>
    <h1>Ali Khan — Analytics &amp; Ops</h1>
    <p class="muted">Charlotte-based ops/analytics. Crisp charts, clear decisions.</p>
    <a class="btn" href="showcase/001-open-meteo-airport-weather/">View Project 001</a>
    <a class="btn secondary" href="assets/001_clt_temp.png">See Latest Chart</a>
  </div>
</div>

<div class="section">
  <h2>Projects</h2>
  <div class="grid">
    <div class="card">
      <div style="display:flex;align-items:center;gap:8px">
        <img src="assets/plane.svg" alt="plane" style="width:20px;height:20px">
        <strong>001 — Airport Weather (Open-Meteo)</strong>
      </div>
      <p class="muted">Fetches hourly weather for CLT and auto-updates a temperature chart every hour.</p>
      <div class="tags">
        <span class="tag">Python</span><span class="tag">pandas</span><span class="tag">matplotlib</span><span class="tag">API</span>
      </div>
      <img src="assets/001_clt_temp.png" alt="CLT temp (next 72h)">
      <p><a href="showcase/001-open-meteo-airport-weather/">Project page</a> ·
         <a href="https://github.com/ahk2710/ali-portfolio/tree/main/projects/001-open-meteo-airport-weather">Code on GitHub</a></p>
    </div>
  </div>
</div>

<div class="section">
  <h2>About</h2>
  <ul>
    <li>Ops performance analyst turning noisy operational data into clear decisions.</li>
    <li>Tooling: Python (pandas, requests, matplotlib), SQL, Tableau/Alteryx.</li>
    <li>Domains: airlines ✈️, logistics, reliability, decision science.</li>
  </ul>
</div>
