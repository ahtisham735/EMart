const Email=document.getElementById("email");
const user_name=document.getElementById("username")
const pass=document.getElementById("password")
const cnfrm_Password=document.getElementById("cnfrmPassword")
const form=document.getElementById("login")

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