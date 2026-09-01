    const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;

    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(!entry.isIntersecting)return;entry.target.classList.add('in');observer.unobserve(entry.target)}),{threshold:.12,rootMargin:'0px 0px -5%'});
    document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

    const getEasternNow=()=>{const parts=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'short',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).formatToParts(new Date());return Object.fromEntries(parts.map(({type,value})=>[type,value]))};
    const updateVenueState=()=>{const now=getEasternNow(),day=now.weekday,minutes=Number(now.hour)*60+Number(now.minute);let barOpen=false;if(day==='Mon')barOpen=minutes>=660;else if(day==='Sun')barOpen=minutes<60||minutes>=750;else barOpen=minutes<60||minutes>=660;let kitchenOpen=false;if(day==='Sun')kitchenOpen=minutes>=750&&minutes<1320;else kitchenOpen=minutes>=660&&minutes<1380;document.querySelector('#open-label').textContent=barOpen?'Open now':'Closed now';document.querySelector('#status-text').textContent=`${barOpen?'Bar open':'Bar closed'} · ${kitchenOpen?'kitchen serving':'kitchen closed'}`;document.querySelector('#status-text').classList.toggle('open',barOpen);document.querySelector('#bar-hours').textContent=day==='Sun'?'Sun 12:30 PM–midnight':'Mon–Sat 11 AM–1 AM';document.querySelector('#kitchen-hours').textContent=day==='Sun'?'Sun 12:30 PM–10 PM':'Mon–Sat 11 AM–11 PM'};
    updateVenueState();setInterval(updateVenueState,60000);

    const scanCard=document.querySelector('#photo-scan'),scanToggle=document.querySelector('#scan-toggle');
    scanToggle.addEventListener('click',()=>{const active=scanCard.dataset.scan!=='off';scanCard.dataset.scan=active?'off':'on';scanToggle.textContent=active?'Show scan':'Hide scan';scanToggle.setAttribute('aria-pressed',String(!active))});

    document.querySelectorAll('.menu-tab').forEach(button=>button.addEventListener('click',()=>{const category=button.dataset.category;document.querySelectorAll('.menu-tab').forEach(tab=>tab.setAttribute('aria-selected',String(tab===button)));document.querySelectorAll('.menu-item').forEach(item=>{item.hidden=item.dataset.category!==category})}));

    const roomMedia=document.querySelector('#room-media'),roomCaption=document.querySelector('#room-caption-text'),roomCapacity=document.querySelector('#room-capacity');
    document.querySelectorAll('.mode').forEach(button=>button.addEventListener('click',()=>{const view=button.dataset.view;roomMedia.dataset.view=view;document.querySelectorAll('.mode').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));roomCaption.textContent=view==='layout'?'Conceptual layout guide · final arrangements confirmed by Tierney\'s':'Real upstairs performance · photo via BiZZBoard';roomCapacity.textContent=view==='layout'?'55–60 seated · up to 135 standing':'Up to 135 standing'}));

    document.querySelector('#map-load').addEventListener('click',event=>{const card=document.querySelector('#map-card'),iframe=document.createElement('iframe');iframe.title="Map showing Tierney's Tavern at 138 Valley Road, Montclair, New Jersey";iframe.src='https://www.google.com/maps?q=40.822509225043,-74.219748973846&z=18&output=embed';iframe.loading='lazy';iframe.referrerPolicy='no-referrer-when-downgrade';iframe.allowFullscreen=true;card.prepend(iframe);document.querySelector('#map-placeholder').remove();event.currentTarget.remove()},{once:true});

    if(!reduceMotion&&'WebGLRenderingContext'in window){
      try{
        const THREE=await import('https://cdn.jsdelivr.net/npm/three@0.185.1/build/three.module.js');
        const canvas=document.querySelector('#hero-scan-canvas'),card=document.querySelector('#photo-scan');
        const renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:false,powerPreference:'low-power'});renderer.setPixelRatio(Math.min(devicePixelRatio,1.35));renderer.setClearColor(0x000000,0);
        const scene=new THREE.Scene(),camera=new THREE.OrthographicCamera(-1,1,1,-1,.1,10);camera.position.z=2;
        const group=new THREE.Group();scene.add(group);
        const lineMaterial=new THREE.LineBasicMaterial({color:0x62ff9d,transparent:true,opacity:.46});
        const paths=[[-.83,.54,-.4,.78,.02,.56,.55,.44,.86,.08],[-.84,-.42,-.84,.54],[-.4,.78,-.14,.04],[-.14,.04,.36,-.2,.84,.08],[-.67,-.02,.5,-.02],[-.52,-.43,-.52,.01],[.17,-.43,.17,-.02]];
        paths.forEach(points=>{const vectors=[];for(let i=0;i<points.length;i+=2)vectors.push(new THREE.Vector3(points[i],points[i+1],0));const geometry=new THREE.BufferGeometry().setFromPoints(vectors);group.add(new THREE.Line(geometry,lineMaterial.clone()))});
        const particleCount=innerWidth<700?55:120,positions=new Float32Array(particleCount*3);for(let i=0;i<particleCount;i++){positions[i*3]=Math.random()*2-1;positions[i*3+1]=Math.random()*2-1;positions[i*3+2]=0}const particleGeo=new THREE.BufferGeometry();particleGeo.setAttribute('position',new THREE.BufferAttribute(positions,3));const particles=new THREE.Points(particleGeo,new THREE.PointsMaterial({color:0x62ff9d,size:.008,transparent:true,opacity:.42}));scene.add(particles);
        const resize=()=>{const rect=card.getBoundingClientRect();renderer.setSize(Math.max(1,rect.width),Math.max(1,rect.height),false)};new ResizeObserver(resize).observe(card);resize();
        let visible=true;new IntersectionObserver(([entry])=>visible=entry.isIntersecting,{threshold:.02}).observe(card);document.addEventListener('visibilitychange',()=>visible=!document.hidden);
        const clock=new THREE.Clock();const animate=()=>{requestAnimationFrame(animate);if(!visible||scanCard.dataset.scan==='off')return;const t=clock.getElapsedTime();group.position.y=Math.sin(t*.35)*.008;group.material?.opacity;particles.rotation.z=t*.008;renderer.render(scene,camera)};renderer.render(scene,camera);animate();
      }catch(error){console.warn('Three.js scan overlay unavailable; the real photograph remains fully visible.',error)}
    }
