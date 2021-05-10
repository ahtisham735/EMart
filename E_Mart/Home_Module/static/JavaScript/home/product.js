
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
  