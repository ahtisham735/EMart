
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
        if (id==null)
            return
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
        if(qty.type!=="number"){
            sub.innerText=parseInt(p[1])*parseInt(qty.innerText)
            return
        }
        sub.innerText=parseInt(p[1])*parseInt(qty.value)
        var chkbox=document.getElementById(`${id}`)
        if(chkbox!==null&&chkbox.checked)
            calBill(id,diff,p[1])

    
    }
    function calBill(id,diff=0,price=0)
    {
     
        var chkbox=document.getElementById(`${id}`)
        var total_obj=document.getElementById("sub")
        var str=total_obj.innerText.split(':')
        var sub=document.getElementById(`sub${id}`).innerText
        var checkoutTotal=0
        var totalBill=document.getElementById("total_bill")
        var noOfItems=document.getElementById("noOfItems")
        const qty=document.getElementById(`qty${id}`)

        if(chkbox.checked)
        {
           
            if(diff===0){
                noOfItems.innerText=parseInt(qty.value)+parseInt(noOfItems.innerText)
                checkoutTotal=parseInt(sub)+parseInt(str[1])
            }
            else{
                var noOfItemsChanged=diff/price
                noOfItems.innerText=parseInt(noOfItems.innerText)+noOfItemsChanged
                checkoutTotal=diff+parseInt(str[1])

            }           
        }
        else
        {
        
            if(parseInt(noOfItems.innerText)-parseInt(qty.value)>=0)
                noOfItems.innerText=parseInt(noOfItems.innerText)-parseInt(qty.value)
            checkoutTotal=parseInt(str[1])-parseInt(sub)
            if (checkoutTotal<0)
                checkoutTotal=0          
        }
        total_obj.innerText="Rs:"+checkoutTotal
        totalBill.innerText="Rs:"+checkoutTotal

    }
    