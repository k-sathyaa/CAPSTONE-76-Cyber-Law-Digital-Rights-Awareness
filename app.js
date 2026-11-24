document.addEventListener("DOMContentLoaded",()=>{
 const form=document.getElementById("quiz-form");
 if(form){form.addEventListener("submit",async e=>{e.preventDefault();const answers={};new FormData(form).forEach((v,k)=>answers[k]=v);
 const res=await fetch("/api/quiz",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({answers})});const data=await res.json();
 document.querySelectorAll(".explanation").forEach(x=>x.style.display="block");
 document.getElementById("quiz-result").innerHTML=`<div class="result"><strong>Your score: ${data.score}/${data.total}</strong><p>${data.message}</p></div>`;});}
 const checks=[...document.querySelectorAll(".checklist input[type=checkbox]")];
 function update(){const n=checks.filter(x=>x.checked).length;const t=document.getElementById("progress-text");const b=document.getElementById("progress-bar");if(t)t.textContent=`${n} of ${checks.length} completed`;if(b)b.style.width=(n/checks.length*100)+"%";}
 checks.forEach(x=>x.addEventListener("change",update));update();
});