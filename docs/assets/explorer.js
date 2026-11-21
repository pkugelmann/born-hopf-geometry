/* Static, client-side research index. No servers, third-party search or telemetry. */
(function(){'use strict';
const d=window.BH_EXPLORER, root=document.getElementById('explore-results');
if(!d||!root)return;
const $=id=>document.getElementById(id), E=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const kinds=[['labels','Source labels',d.counts.anchors],['nodes','DAG nodes',d.counts.canonicalNodes],['obligations','Proof obligations',d.counts.obligations],['audits','Audit reports',d.counts.reports],['diagrams','Geometry diagrams',d.counts.diagrams]];
const params=new URLSearchParams(location.search);
let kind=kinds.some(k=>k[0]===params.get('type'))?params.get('type'):'labels';
const q=$('explore-q'),paper=$('explore-paper'),latest=$('explore-latest'),count=$('explore-count'),buttons=$('explore-types');
q.value=params.get('q')||'';
latest.checked=params.get('latest')==='1';
const papers=[...new Set(d.labels.map(x=>x.paper))].sort((a,b)=>{let aa=a.match(/\d+/),bb=b.match(/\d+/);return Number(aa?.[0])-Number(bb?.[0])||a.localeCompare(b)});
paper.innerHTML='<option value="">All papers</option>'+papers.map(p=>`<option value="${E(p)}">${E(p.replace('Paper','Paper '))}</option>`).join('');
if(papers.includes(params.get('paper')))paper.value=params.get('paper');
buttons.innerHTML=kinds.map(k=>`<button class="filter-pill" type="button" data-kind="${k[0]}">${E(k[1])}<small>${k[2].toLocaleString()}</small></button>`).join('');
const currentSource=x=>x&&x.file?`https://github.com/pkugelmann/born-hopf-geometry/blob/main/docs/manuscripts/${encodeURIComponent(x.file)}#L${encodeURIComponent(x.line||1)}`:'';
const manuscript=p=>`paper.html?paper=${encodeURIComponent(p)}`;
const paperLink=p=>p&&p!=='Cross-paper'?`<a href="${manuscript(p)}">${E(p)}</a>`:'';
const cards={
 labels:x=>`<article class="explorer-card"><div class="paper-code">${E(x.paper)} · ${x.new?'<span class="edge-new">NEW v3.077 SOURCE</span>':'source label'} · line ${E(x.line)}</div><h3>${E(x.title||x.id)}</h3>${x.title?`<p class="id-string">${E(x.id)}</p>`:''}<div class="explorer-links">${paperLink(x.paper)}<a href="${currentSource(x)}" target="_blank" rel="noopener">View current TeX line ↗</a></div></article>`,
 nodes:x=>`<article class="explorer-card"><div class="paper-code">${E(x.paper)} · ${E(x.type||'node')} · ${x.current_anchor?'current anchor':'historical graph node'}</div><h3>${E(x.title||x.id)}</h3><p class="id-string">${E(x.id)}</p><div class="explorer-links">${paperLink(x.paper)}${x.current_anchor?`<a href="${currentSource({file:x.source_file,line:x.source_line})}" target="_blank" rel="noopener">Current source ↗</a>`:''}</div></article>`,
 obligations:x=>`<article class="explorer-card"><div class="paper-code">${E(x.paper)} · retained audit v1.83</div><h3>${E(x.id)}</h3><p>${E(x.description)}</p><p class="id-string">${E(x.status.replaceAll('_',' '))}</p><div class="explorer-links">${paperLink(x.paper)}<a href="verification/registries/Paper00-RemainingProofObligations-v1_3.json" target="_blank" rel="noopener">Original registry ↗</a></div></article>`,
 audits:x=>`<article class="explorer-card"><div class="paper-code">${E(x.paper)} · original report</div><h3>${E(x.name.replace(/\.md$/,''))}</h3><p>Historical audit; its paper source may predate v3.077.</p><div class="explorer-links">${paperLink(x.paper)}<a href="${E(x.href)}">Read audit ↗</a></div></article>`,
 diagrams:x=>`<article class="explorer-card explorer-diagram"><a href="geometry/${encodeURIComponent(x.file)}" target="_blank" rel="noopener"><img src="geometry/${encodeURIComponent(x.file)}" loading="lazy" alt="${E(x.name)}"/></a><h3>${E(x.name)}</h3><div class="explorer-links"><a href="geometry/${encodeURIComponent(x.file)}" target="_blank" rel="noopener">Open diagram ↗</a></div></article>`
};
let cache={};
function searchable(x){return [x.id,x.title,x.name,x.paper,x.description,x.status,x.type,x.file,x.recorded_source].filter(Boolean).join(' ').toLowerCase()}
function syncUrl(){const u=new URL(location.href);u.searchParams.set('type',kind);if(q.value.trim())u.searchParams.set('q',q.value.trim());else u.searchParams.delete('q');if(paper.value)u.searchParams.set('paper',paper.value);else u.searchParams.delete('paper');if(latest.checked&&kind==='labels')u.searchParams.set('latest','1');else u.searchParams.delete('latest');history.replaceState(null,'',u)}
function render(){
 const term=q.value.trim().toLowerCase(), selected=paper.value;
 if(!cache[kind])cache[kind]=d[kind].map(x=>({...x,_search:searchable(x)}));
 const rows=cache[kind].filter(x=>(!selected||x.paper===selected)&&(!term||x._search.includes(term))&&(!(kind==='labels'&&latest.checked)||x.new));
 const matches=rows.length,view=rows.slice(0,80);
 count.textContent=matches.toLocaleString()+' matches'+(matches>80?' · showing first 80':'');
 root.innerHTML=matches?view.map(cards[kind]).join(''):'<div class="empty">No matching records. Try fewer terms, clear the paper filter, or choose another index.</div>';
 [...buttons.querySelectorAll('button')].forEach(el=>{const yes=el.dataset.kind===kind;el.classList.toggle('active',yes);el.setAttribute('aria-pressed',String(yes))});
 $('explore-latest-box').style.display=kind==='labels'?'flex':'none';
 $('explore-source-note').textContent=kind==='nodes'?'Canonical DAG nodes are inherited, not a proof audit of v3.077. Current line anchors are shown only where found in the current source map.':kind==='obligations'?'These 130 rows are the retained v1.83 issue registry, not a new judgment on every v3.077 revision.':kind==='labels'?'A label is a verified source locator, NOT a proof-status certificate. The newest 55 labels are source-integrated, pending independent global E3/E4 review.':kind==='audits'?'Every audit is preserved with its original source-version and status scope.':'These 13 diagrams are source-preserved visual aids, not physical-observable certificates.';
 syncUrl();
}
buttons.addEventListener('click',e=>{const b=e.target.closest('button[data-kind]');if(!b)return;kind=b.dataset.kind;render()});
q.addEventListener('input',render);paper.addEventListener('change',render);latest.addEventListener('change',render);
$('explore-clear').addEventListener('click',()=>{q.value='';paper.value='';latest.checked=false;render()});
render();
})();
