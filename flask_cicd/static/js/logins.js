function Login(){
    var q=document.getElementById("uname");
    var w=document.getElementById("pass");
    var numlen = w.value.replace(/[^0-9]/g,"").length;
    var spelen = w.value.replace(/[a-zA-Z0-9 ]/gi,"").length;

    if(q.value==""){
    window.alert("please enter the username");
    q.focus();
    return false;
}
    if(w.value==""){
    window.alert("please enter the password");
    w.focus();
    return false;
}

if(w.value.length != 8){
    window.alert("The password length should be 8 characters");
    w.focus();
    return false;
}
if(numlen != 1){
    window.alert("The password must contain only one number, please check the password");
    w.focus();
    return false;
}

if(spelen != 1){
    window.alert("The password must contain only one special character, please check the password");
    w.focus();
    return false;
}

  return true;
};
