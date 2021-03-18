var status={email:false,username:false,password:false,cnfrmPassword:false}
handleFocus=(id)=>{
    
    const val=document.getElementById(`${id}`)
    const element =document.getElementById(`${id}Error`)
    if(val.value.length===0){
       
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
            status.email=true;   
        }
        else
        {
            status.email=false; 
            element.innerHTML="";
        }

    }
    else if(id==='username'){
        fetch(`http://localhost:8000/customer/${val.value}`)
        .then(response=>response.json())
        .then(data=>{
           if(data!==null){
            element.innerHTML="This username has already taken"
            status.username=false;
           }
           else{
            status.username=true;
            element.innerHTML=""
           }
        })
    }
    else if(id==='password')
    {
        const cnfrmPasswd=document.querySelector('#cnfrmPassword')
        if(cnfrmPasswd.value.length!=0){
           if(!PasswordValidation()){
            status.cnfrmPassword=false;
            
           }else{
            status.cnfrmPassword=true;
           }

        }
        var passwdPattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*])(?=.{8,})") 
       if(!passwdPattern.test(val.value)){
            element.innerHTML="use 8 or more letters having atleast one lowercase,one uppercase and one special character";
            status.password=false;
    }
       else{
        status.password=true;
        element.innerHTML="";
       }

    }
    else if(id==="cnfrmPassword"){
        if(!PasswordValidation()){
            status.cnfrmPassword=false;
        }else{
            status.cnfrmPassword=true;
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

regSubmit=(e)=>{
    console.log(e)
    e.preventDefault();
    if(status.email&&status.password&&status.cnfrmPassword&&status.username){
       
        const chkbox=document.querySelector('#chkbox')
        if(chkbox.checked){
            alert("sdsds")
            fetch('http://localhost:8000/customer/',{
                method:'POST',
                body:new FormData(e)
            })
            .then(response=>response.text())
            .then(data=>{
                alert(data)
            })
        }
    }else{
        return;
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