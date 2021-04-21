var PhoneStatus=false
var CnicStatus=false
var AccountStatus=false

detailValidation=()=>{
    const shopNam=document.getElementById("shopName")
    const phoneNo=document.getElementById("PhoneNo")
    var cnicNo=document.getElementById("cnic")
    var addres=document.getElementById("address")
    var accountNumber=document.getElementById("account")
    var submit=true;
    if(shopNam.value.length<1 )
    {
        shopEror.innerHTML="you cannot leave this field empty"

    }
    else
    {
        shopEror.innerHTML=""
    }
    if(addres.value.length<1)
    {
        AddressEror.innerHTML="you cannot leave this field empty"

    }
    else
    {
        AddressEror.innerHTML=""
    }
    if(phoneNo.value.length===11){
        phoneEror.innerHTML=""
    }
    else{
        phoneEror.innerHTML="Phone number should be 11 digits"
        submit= false;
    }
    if(cnicNo.value.length==13){
        cnicEror.innerHTML=""
    }
    else{
        cnicEror.innerHTML="CNIC should be 13 digits" 
        submit= false    
    }
    if(account.value.length==14){
        AccountEror.innerHTML=""      
    }
    else{
        AccountEror.innerHTML="account should be 14 digits"  
        submit= false   

    }
    return submit;
}

function allnumeric(id)
{
    const val=document.getElementById(`${id}`)
    const element =document.getElementById(`${id}Error`)
    var numbers = /^[0-9]+$/;
    if(id==='PhoneNo'){
        if(val.value.match(numbers))
        {
            phoneEror.innerHTML=""
            PhoneStatus=true
        }     
        else
        {
            PhoneStatus=false
            phoneEror.innerHTML=""
            phoneEror.innerHTML="Enter Digits only"
        }
    }
    
    if(id==='account'){
        if(val.value.match(numbers))
        {
            AccountEror.innerHTML=""
             AccountStatus=true
        }     
        else
        {
            AccountEror.innerHTML=""
            AccountEror.innerHTML="Enter Digits only"
            AccountStatus=false

        }
    }

    if(id==='cnic'){
        if(val.value.match(numbers))
        {
            cnicEror.innerHTML=""
            CnicStatus=true
        }     
        else
        {
            cnicEror.innerHTML=""
            cnicEror.innerHTML="Enter Digits only"
            CnicStatus=false

        }
    }
    if(id==='shopName'){
        shopEror.innerHTML=""
    }
    if(id==='address'){
        AddressEror.innerHTML=""
    }
    

    if(PhoneStatus&&CnicStatus&&AccountStatus)
    {
        subbtn.disabled=false;  
    }
    else
    {
        subbtn.disabled=true; 
    }
   } 


function openRegister()
{
    var card=document.getElementById("card");
    card.style.transform = "rotateY(-180deg)";
}
function openLogin()
{
    var card=document.getElementById("card");
    card.style.transform = "rotateY(0deg)";
} 
