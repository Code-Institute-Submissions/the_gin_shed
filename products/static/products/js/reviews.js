$("label").click(function() {
    $(this).parent().find("label").css({'background-color' : "white"});
    $(this).css({'background-color' : "#788e5c"});
    $(this).nextAll().css({'background-color' : "#788e5c"});
});