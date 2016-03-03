$(document).ready(function () {

    //alert("ready");
    $("p").click(function () {
        //alert("you clicked a p");
    });

    $("button").click(function () {
        //alert("you clicked a button");
        if ($(this).hasClass('story_button')) {
            //alert("you clicked a story button");
            //alert($(this).val());
            $.get($(this).val(), function (data) {
                $('#main_content').html(data); //we need this line to make the connection
            });
        }
    });

    $('input[name=choice]').click(function () {
        //alert("you clicked a choice");
        //alert($(this).val());
        $('#main_content').fadeOut("slow");
        $.get($(this).val(), function (data) {

            $('#main_content').html(data); //we need this line to make the connection

        });
        $('#main_content').hide();
        $('#main_content').fadeIn("slow");
    });
});

//$('#story_content').hide(); //may be in use
