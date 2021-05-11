
/*var smallImg=document.getElemenstByClassName("small-img");
    smallImg[0].onclick=function(){
        ProductImg.src=smallImg[0].src;

    }
    smallImg[1].onclick=function(){
        ProductImg.src=smallImg[1].src;
        
    }
    smallImg[1].onclick=function(){
        ProductImg.src=smallImg[1].src;
        
    }
    smallImg[3].onclick=function(){
        ProductImg.src=smallImg[3].src;
        
    }
    smallImg[4].onclick=function(){
        ProductImg.src=smallImg[4].src;
        
    }*/
    clickMe=(smallImg)=>{
        var ProductImg=document.getElementById("productImg");
        ProductImg.src=smallImg.src;
    }
    document.addEventListener('DOMContentLoaded',()=>{
 
        var id=document.getElementById('table');
        inputs = id.getElementsByTagName("input")
              
        for(var i=0, len=inputs.length; i<len; i++){
            if(inputs[i].type === "hidden"){
            
              calsubTotal(inputs[i].value)
            }
          }
    });
    
    function calsubTotal(id)
    {
        var price=document.getElementById(`p${id}`)
        var p=price.innerText.split(":")
        const qty=document.getElementById(`qty${id}`)
        var sub=document.getElementById(`sub${id}`)
        var diff=parseInt(p[1])*parseInt(qty.value)-parseInt(sub.innerText)
        sub.innerText=parseInt(p[1])*parseInt(qty.value)

        calBill(id)

    
    }
    function calBill(id)
    {
        var chkbox=document.getElementById(`${id}`)
        if(chkbox.checked)
        {
            var total_obj=document.getElementById("sub")
            var str=total_obj.innerText.split(':')
            var sub=document.getElementById(`sub${id}`).innerText
            var checkoutTotal=parseInt(sub)+parseInt(str[1])
            total_obj.innerText="Rs:"+checkoutTotal


           
        }
        else
        {
            console.log("Not checked")
        }

    }
    function recalculateBill(id,diff)