$(document).ready(function () {

    //alert("ready");
    $("p").click(function () {
        //alert("you clicked a p");
    });

    $("button").click(function () {
        //alert("you clicked a button");
        if ($(this).hasClass('story_start_button')) {
            //alert($('.story_start_button').val());
            $('#main_content').fadeOut("slow");
            $('#main_content').promise().done(function () {
                $.get($('.story_start_button').val(), function (data) {
                    $('#main_content').hide();
                    $('#main_content').html(data); //we need this line to make the connection
                    $('#main_content').hide();
                    $('#main_content').fadeIn("slow");
                });
            });

        } else if ($(this).hasClass('story_button')) {
            //alert($('.story_start_button').val());
            $('#main_content').fadeOut("slow");

            $.get($(this).val(), function (data) {
                $('#main_content').hide();
                $('#main_content').html(data); //we need this line to make the connection
                $('#main_content').hide();
                $('#main_content').fadeIn("slow");
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
