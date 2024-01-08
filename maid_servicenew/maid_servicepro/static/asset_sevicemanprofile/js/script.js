// add user

$(document).ready(function(){
    $('#sub').click(function()
    {
        if($("#first_name").val()==""){
            alert("Enter valid name")
        }       
        if(!$("#first_name").val().match('^[a-zA-Z]{3,}$')){
            alert("Please Enter Atleast 3 characters")
            return false;                
        }
        
        if(!$("#email").val().match(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]+?\.[a-zA-Z]{2,50}$/)){
            if(!$("#email").val().match(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,50}$/)){
            alert("invalid email id"); 
            return false;
        } 
    }
        
        {
        if(!$("#password").val().match("^(?=.*[a-zA-Z0-9$#%!]).{4,20}$")){
            alert("Please Enter Atleast 4 Characters")
            return false
        }
        {
        if($("#last_name").val().length!=10){
            alert("Contact should be 10 digits ");
            return false;
        } 
        {
            if($("#first_name").val()==""){
                alert("Please enter address")
                return false;
            }

        }
        
        }
        }
    });
    
    });