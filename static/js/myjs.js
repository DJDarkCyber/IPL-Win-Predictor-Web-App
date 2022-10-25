$(document).ready(function() {

    // Login Page Filter 

    // $("#realPass, #confPass, #username").on("keyup", function(){

    //         var username = $("#username").val();
    //         var pattern = new RegExp(/[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/);
    //         var flag = 0;
    //         var flag2 = 0;
    //         if (pattern.test(username)) {
    //             $("#invalidUsernameAlert").css("display", "unset");
    //             flag = 0;
    //         }
    //         else{
    //             $("#invalidUsernameAlert").css("display", "none");
    //             flag = 1;
    //         }
    //         if($("#realPass").val() == $("#confPass").val()){
                
    //             $("#message").css("display", "none");
    //             flag2 = 1;
    //         }
    //         else{
    //             // $(".registerSubmitBtn").css("display", "none");
    //             $("#message").html("Password didn't matches").css("color", "red").css("display", "unset");
    //             flag2 = 0;
    //         }
    //         if(flag == 1 && flag2 == 1){
    //             $(".registerSubmitBtn").css("display", "unset");
    //         }
    //         else{
    //             $(".registerSubmitBtn").css("display", "none");
    //         }
    //     }
    // )

    // $(".alertBoxMark").click(
    //     function(){
    //         $(".alertBoxArea").css("display", "none");
    //     }
    // )
    $("#team1, #team2").on("click", function(){  

            var team1val = $("#team1").val();
            var team2val = $("#team2").val();
            var tossTeam = $("#tossteam").val();
            if(team1val == team2val){
                $("#team2").val("");
            }
            
            var team1val = $("#team1").val();
            var team2val = $("#team2").val();
            var tossTeam = $("#tossteam").val();


            $("#tossteam").empty();
            $("#tossteam").append('<option value="'+ team1val +'"> ' + team1val + '</option>');
            $("#tossteam").append('<option value="'+ team2val +'"> ' + team2val + '</option>');
        }
    )




});