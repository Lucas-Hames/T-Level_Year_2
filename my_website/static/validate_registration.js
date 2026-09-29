function validate(){
    varUname = document.getElementById("uname").value;
    varEmail = document.getElementById("email").value;
    varPwd = document.getElementById("pwd").value;
    varAge = document.getElementById("age").value;
    varSite = document.getElementById("site").value;
    varDob = document.getElementById("dob").value;
    varGender = document.querySelector('input[name = "gender"\]:checked');
    varLang = document.querySelectorAll('input[name = "lang"\]:checked');
    if (varUname == "" || varEmail == "" || varPwd == "" || varAge == "" || varSite == "" || varDob == ""){
        alert("You must fill all the fields");
        return false;
    } else if (varGender === null) {
        alert("Select a gender");
        return false;
    } else if (varLang.length === 0) {
        alert("Select at least one programming language");
        return false;
    } else {
        return true;
    }
}