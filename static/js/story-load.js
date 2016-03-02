$(document).ready(function () {

    $('#trigger').click(function () {
        $.get('/zombies/story-change/', function (data) {
            //$('#story_content').html(data);
            //we need this line to make the connection
        });
        $('#story_content').hide();
    });

});

