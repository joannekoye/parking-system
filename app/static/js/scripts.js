$(document).ready(function () {
    var clicked;
    clicked = $(this).attr("name");
    $.ajax({
        type: 'POST',
        url: "{{url_for('test')}}",
        contentType: 'application/json;charset=UTF-8',
        data: { 'data': clicked }
    });
});