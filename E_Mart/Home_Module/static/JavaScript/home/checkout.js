document.addEventListener('DOMContentLoaded',()=>{
    populate()
});

function populate(){
    var s1=document.getElementById('s1');
    var s2=document.getElementById('s2');
    var city=document.getElementById('city')
    console.log(city.value)
    if(s1.value=="Pakistan"){
        var optionArray=['Lahore|Lahore','Karachi|Karachi','Islamabad|Islamabad','Peshawar|Peshawar'];
    }
	else if(s1.value=="Turkey"){
		var optionArray=['Istanbul|Istanbul','Ankara|Ankara','Izmir|Izmir','Bursa|Bursa'];
	}
    var cityoption=document.createElement("option");
        if(city.value!=null){
		    cityoption.innerHTML=city.value;
            s2.options.add(cityoption)
        }
	for(var option in optionArray){
		var pair=optionArray[option].split("|");
		var newoption=document.createElement("option");
        if(pair[0]!=city.value && pair[1]!=city.value)
        {
            newoption.value=pair[0];
		newoption.innerHTML=pair[1];
		s2.options.add(newoption);

        }

        

        
	}


}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function checkout()
    {
        var id=document.getElementById('table');
        if (id==null)
            return
        inputs = id.getElementsByTagName("input")
        const chkboxes=[]
        var orders=[]
        for(var i=0, len=inputs.length; i<len; i++){
        
           
            if(inputs[i].type === "checkbox"){
                if (inputs[i].checked)
                    chkboxes.push(inputs[i])
                  
            }
        }
        var error= document.getElementById("checkoutError")
        if (chkboxes.length===0)
        {
            error.innerHTML="Please check atleast one product"
            return 
        }
        else
        {
            error.innerHTML=""
            for(var i=0;i<chkboxes.length;i++)
            {

                const qty=document.getElementById(`qty${chkboxes[i].id}`)
                var order={"cart id":chkboxes[i].id,"quantity":qty.value}
                orders.push(order)     
            }
            const csrftoken = getCookie('csrftoken');
            fetch('http://localhost:8000/cart/', {
            method: "POST",
            body: JSON.stringify(orders),
            headers: { 'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrftoken },
            })
            .then(response=>{
                window.location.href = "http://localhost:8000/shipping/shipping/";

            })
            .catch(error=>{
                alert(error)
            })

        }

    }

/* Error Messages */