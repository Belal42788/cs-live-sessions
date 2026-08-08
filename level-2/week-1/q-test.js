const { JSDOM } = require('C:/Users/asama/AppData/Local/Temp/opencode/node_modules/jsdom');
const fs = require('fs');
const html = fs.readFileSync('C:/Users/asama/AppData/Local/Temp/opencode/w1-page.html','utf8');
const dom = new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,beforeParse(w){w.IntersectionObserver=class{constructor(cb){this.cb=cb;}observe(el){this.cb([{isIntersecting:true,target:el}],this);}unobserve(){}disconnect(){}};}});
const w=dom.window; const d=w.document;
setTimeout(()=>{
  // verify all quiz options use optlet badge and have no "X — " prefix
  const opts=d.querySelectorAll('.q-opt');
  let badgeOk=true, prefixClean=true;
  opts.forEach(o=>{
    if(!o.querySelector('.optlet')) badgeOk=false;
    if(/^[A-D]\s*—/.test(o.textContent.trim())) prefixClean=false;
  });
  console.log('opts total:', opts.length);
  console.log('all have optlet badge:', badgeOk);
  console.log('no A— prefix left:', prefixClean);
  // interaction still works
  const trig=d.querySelector('.quiz-reveal-trigger');
  trig.click();
  const opts2=d.querySelectorAll('.quiz .q-opt');
  const correct=[...opts2].find(o=>o.getAttribute('data-r')==='1');
  correct.click();
  const fb=correct.parentElement.querySelector('.q-fb.green').style.display;
  console.log('correct feedback shown:', fb==='block');
},300);
