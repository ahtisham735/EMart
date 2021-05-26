var PhoneNoStatus=true
var zipStatus=true

var CardNoStatus=false
var CvvStatus=false
var holdrStatus=false
var countryStatus=false

document.addEventListener('DOMContentLoaded',()=>{
    populate()
});

function validateInput(id, er)
 {
    const val=document.getElementById(`${id}`)
    const element =document.getElementById(`${er}`)
    var numbers = /^[0-9]+$/;
    if(id=='phone'){
        if(val.value.match(numbers))
        {
            element.innerHTML=""
            PhoneNoStatus=true
        }     
        else
        {
            PhoneNoStatus=false
            element.innerHTML="Enter Digits only"
        }
    }
    if(id=='zip'){
        if(val.value.match(numbers))
        {
            element.innerHTML=""
            zipStatus=true
        }     
        else
        {
            zipStatus=false
            element.innerHTML="Enter Digits only"
        }
    }
    if(id=="email")
    {
        var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if(!filter.test(val.value)){
            element.innerHTML="invalid email";             
            emailStatus=false   
        }
        else
        {
            emailStatus=true; 
            element.innerHTML="";
        }
    }
    if(id=='fname'){
        element.innerHTML=""
    }
    if(id=='lname'){
        element.innerHTML=""
    }
    if(id=='address'){
        element.innerHTML=""
    }
    if(PhoneNoStatus && zipStatus)
    {
        document.getElementById("ShipingSubBtn").disabled=false;  
    }
    else
    {
        document.getElementById("ShipingSubBtn").disabled=true; 
    }
   
 }

 
shipValidation=()=>{
    var firstName = document.forms["shipingDetail"]["fname"].value;
    var lastName = document.forms["shipingDetail"]["lname"].value;
    var adddres = document.forms["shipingDetail"]["address"].value;
    var phoneN=document.forms["shipingDetail"]["phone"].value
    var zipcod = document.forms["shipingDetail"]["zip"].value;
    var emailAdd = document.forms["shipingDetail"]["email"].value;
    
    var fnEror=document.getElementById("fname_error")
    var lnEror=document.getElementById("lname_error")
    var addEror=document.getElementById("address_error")
    var phnEror=document.getElementById("phone_error")
    var emailEror=document.getElementById("email_error")
    var zipEror=document.getElementById("zip_error")
    var countryError=document.getElementById("country_error")

   
   

    if (firstName == "" || firstName==null) {
      fnEror.innerHTML="first name is required "
      return false;
    }
    else
    {
        fnEror.innerHTML=""
    }
    if (lastName == "" || lastName==null) {
        lnEror.innerHTML="Lastname is required"
        return false;
    }
    else
    {
        lnEror.innerHTML=""
    }
    if (adddres == "" || adddres==null) {
        addEror.innerHTML="Address is required"
        return false;
    }
    else
    {
        addEror.innerHTML=""
    }
    if (countryStatus) {
        countryError.innerHTML=""
    }
    else
    {   
        countryError.innerHTML="Select Country please!"
        return false; 
    }
    if(zipcod.length!=5)
    {
        zipEror.innerHTML="Zip length should be 5."
        return false
    }
    else
    {
        zipEror.innerHTML=""
    }
    if(phoneN.length!=11)
    {
        phnEror.innerHTML="Phone length should be 11."
        return false
    }
    else
    {
        phnEror.innerHTML=""
    }
   
    if (emailAdd == "" || emailAdd==null) {
        emailEror.innerHTML="Email is required "
        return false;
    }
    else
    {
        emailEror.innerHTML=""
    }
      return true
}

function populate(){
    var s1=document.getElementById('s1');
    var s2=document.getElementById('s2');
    var city=document.getElementById('city');
    var country=document.getElementById('country');
    console.log(city.value)
    console.log(s1.value)
    console.log(country.value)
    if(s1.value=="Pakistan"){
        var optionArray=['Lahore|Lahore','Karachi|Karachi','Islamabad|Islamabad','Peshawar|Peshawar'];
        countryStatus=true
        countryError.innerHTML=""
    }
	else if(s1.value=="Turkey"){
		var optionArray=['Istanbul|Istanbul','Ankara|Ankara','Izmir|Izmir','Bursa|Bursa'];
        countryStatus=true
        countryError.innerHTML=""
	}
    else if(s1.value=="Saudia"){
        var optionArray=['riyadh|Riyadh','jeddah|Jeddah','makkah|Makkah','abuk|Tabuk'];
        countryStatus=true
        countryError.innerHTML=""
    }
	else if(s1.value=="China"){
		var optionArray=['shanghai|Shanghai','tianjin|Tianjin','shenzhen|Shenzhen','shenyang |Shenyang '];
        countryStatus=true
        countryError.innerHTML=""
	}
    else if(s1.value=="China"){
		var optionArray=['Chongqing|Chongqing','Hong Kong|Hong Kong','Beijing|Beijing','Macua|Macua'];
	}
    else
    {
        countryStatus=false
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