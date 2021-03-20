var emailStatus=true
var usernameStatus=false
var passwordStatus=false
var cnfrmPasswordStatus=false
var loginpaswd=false
var loginName=false
handleLoginUserName=()=>
{
    const x=document.getElementById("username").value;
    if(x.length<1)
    {
        document.getElementById("nameError").innerHTML = "Required field";
        loginName=false;
    }
    else
    {
        document.getElementById("nameError").innerHTML = "";
        loginName=true;
    }
   
  
}
function handleLoginPaswd()
{
    const y=document.getElementById("password").value;
    var passwdPattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    if(!passwdPattern.test(y)){
        document.getElementById("pswdError").innerHTML="use 8 or more letters having atleast one lowercase,one uppercase and one special character";
        loginpaswd=false;
    }
    else{
        document.getElementById("pswdError").innerHTML="";
        loginpaswd=true;
    }
        
}
handleFocus=(id)=>{
    
    const val=document.getElementById(`${id}`)
    const element =document.getElementById(`${id}Error`)
    if(val.value.length<1){
       
        element.innerHTML="it is a required field";
               
    }    
}

handleChangeRegister=(id)=>{
    const val=document.getElementById(`${id}`)
    const element =document.getElementById(`${id}Error`)
    if(val.value.length===0){
       
        element.innerHTML="it is a required field";
        return;
                             
    }

    if(id==='email'){
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
    else if(id==='username'){
        fetch(`http://localhost:8000/customer/${val.value}`)
        .then(response=>response.json())
        .then(data=>{
           if(data!==null){
            element.innerHTML="This username has already taken"
                usernameStatus=false;
           }
           else{
                usernameStatus=true;
            element.innerHTML=""
           }
        })
    }
    else if(id==='password')
    {
        const cnfrmPasswd=document.querySelector('#cnfrmPassword')
        if(cnfrmPasswd.value.length!=0){
           if(!PasswordValidation()){
                cnfrmPasswordStatus=false;
            
           }else{
                cnfrmPasswordStatus=true;
           }

        }
        var passwdPattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*])(?=.{8,})") 
       if(!passwdPattern.test(val.value)){
            element.innerHTML="use 8 or more letters having atleast one lowercase,one uppercase and one special character";
                passwordStatus=false;
    }
       else{
            passwordStatus=true;
        element.innerHTML="";
       }

    }
    else if(id==="cnfrmPassword"){
        if(!PasswordValidation()){
            cnfrmPasswordStatus=false;
        }else{
            cnfrmPasswordStatus=true;
        }
    }
    
   
}

PasswordValidation=()=>{
    
    const passwd=document.getElementById('password')
    const cnfrmPasswd=document.getElementById('cnfrmPassword')
    const element=document.getElementById('cnfrmPasswordError')
    if(passwd.value!==cnfrmPasswd.value){
        element.innerHTML="Password not matched"
        return false;
    }
    else{
        element.innerHTML=""
        return true;
    }


}
loginSubmit=()=>
{
    if(loginpaswd&&loginName){      
            return true;
    }else{
        return false;
    }
};
regSubmit=()=>{
    f=document.getElementById("register")

    if(email&&password&&cnfrmPassword&&username){
       
        const chkbox=document.querySelector('#chkbox')
        if(chkbox.checked){
            return true;
            
        }
    }else{
        return false;
    }
};
function login(){
    
    var x=document.getElementById("login");
    var y=document.getElementById("register");
    var z=document.getElementById("btn_back");  
    x.style.left="50px";
    y.style.left="450px";
    z.style.left="0px";
    }
    
function register(){
    var x=document.getElementById("login");
    var y=document.getElementById("register");
    var z=document.getElementById("btn_back");
    x.style.left="-400px";
    y.style.left="50px";
    z.style.left="110px";
}