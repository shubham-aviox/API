$(document).ready(function(){
    $('#signin').on('click', function(){
        var email = $('#email').val();
        var password = $('#password').val();

        if (email == '') {
            alert("Please enter your email")
            return false
        }
        if (password == '') {
            alert("Please enter your password")
            return false
        }

        return true
    })
})