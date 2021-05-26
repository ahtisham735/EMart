document.addEventListener('DOMContentLoaded',()=>{

    inputs = document.getElementsByTagName("input")
              
        for(var i=0, len=inputs.length; i<len; i++){
            if(inputs[i].type === "hidden"){
                var price=document.getElementById(`p${inputs[i].value}`)
                var qty=document.getElementById(`qty${inputs[i].value}`)
                console.log(qty.innerHTML)
                console.log(price.innerHTML)
                document.getElementById(`sub${inputs[i].value}`).innerHTML=parseInt(qty.innerHTML)*parseInt(price.innerHTML)
    
            }
        }

   
     


})