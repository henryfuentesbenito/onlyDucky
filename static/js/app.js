const form=document.querySelector('#chat-form');
if(form){const body=document.querySelector('#chat-body'),input=document.querySelector('#chat-input'),slug=body.dataset.slug;
 document.querySelectorAll('.suggestions button').forEach(b=>b.onclick=()=>{input.value=b.textContent;input.focus()});
 form.addEventListener('submit',async e=>{e.preventDefault();const msg=input.value.trim();if(!msg)return;body.insertAdjacentHTML('beforeend',`<div class="bubble user"></div>`);body.lastElementChild.textContent=msg;input.value='';body.scrollTop=body.scrollHeight;
 const wait=document.createElement('div');wait.className='bubble bot';wait.textContent='Pensando…';body.appendChild(wait);
 try{const r=await fetch(`/api/chat/${slug}`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:msg})});const d=await r.json();wait.textContent=d.reply||d.error}catch{wait.textContent='No he podido responder. Comprueba que Flask sigue ejecutándose.'}body.scrollTop=body.scrollHeight;});}
