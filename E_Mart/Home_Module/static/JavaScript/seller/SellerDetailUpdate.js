var PhoneStatus=true
var CnicStatus=true
var AccountStatus=true
detailUpdateValidation=()=>{
    const shopNam=document.getElementById("shopName")
    const phoneNo=document.getElementById("PhoneNo")
    var cnicNo=document.getElementById("cnic")
    var addres=document.getElementById("address")
    var accountNumber=document.getElementById("account")

    const shopNamEror=document.getElementById("shopEror")
    const phoneNoEror=document.getElementById("phoneEror")
    var cnicNoEror=document.getElementById("cnicEror")
    var addresEror=document.getElementById("AddressEror")
    var accountNumberEror=document.getElementById("AccountEror")

    var submit=true;
    if(shopNam.value.length<1 )
    {
        shopNamEror.innerHTML="you cannot leave this field empty"
        submit= false
    }
    else
    {
        shopNamEror.innerHTML=""
    }
    if(addres.value.length<1)
    {
        addresEror.innerHTML="you cannot leave this field empty"
        submit= false
    }
    else
    {
        addresEror.innerHTML=""
    }
    if(phoneNo.value.length==11){
        phoneNoEror.innerHTML=""
    }
    else{
        phoneNoEror.innerHTML="Phone number should be 11 digits"
        submit= false;
    }
    if(cnicNo.value.length==13){
        cnicNoEror.innerHTML=""
    }
    else{
        cnicNoEror.innerHTML="CNIC should be 13 digits" 
        submit= false    
    }
    if(accountNumber.value.length==14){
        accountNumberEror.innerHTML=""      
    }
    else{
        accountNumberEror.innerHTML="account should be 14 digits"  
        submit= false   

    }
    return submit;
}

function allnumeric(id, er)
{
    const val=document.getElementById(`${id}`)
    const element =document.getElementById(`${er}`)
    var numbers = /^[0-9]+$/;
    if(id=='PhoneNo'){
        if(val.value.match(numbers))
        {
            element.innerHTML=""
            PhoneStatus=true
        }     
        else
        {
            PhoneStatus=false
            element.innerHTML="Enter Digits only"
        }
    }
    
    if(id=='account'){
        if(val.value.match(numbers))
        {
            element.innerHTML=""
             AccountStatus=true
        }     
        else
        {
            element.innerHTML="Enter Digits only"
            AccountStatus=false

        }
    }

    if(id=='cnic'){
        if(val.value.match(numbers))
        {
            element.innerHTML=""
            CnicStatus=true
        }     
        else
        {
            element.innerHTML="Enter Digits only"
            CnicStatus=false

        }
    }
    if(id=='shopName'){
        element.innerHTML=""
    }
    if(id=='address'){
        element.innerHTML=""
    }
    

    if(PhoneStatus&&CnicStatus&&AccountStatus)
    {
        document.getElementById("subbtn").disabled=false;  
    }
    else
    {
        document.getElementById("subbtn").disabled=true; 
    }
   } 