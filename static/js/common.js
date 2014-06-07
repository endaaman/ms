$(function() {
    $('head').append(
    '<style type="text/css">#wrap{display:none;}'
    );
    $(window).load(function() {
        $('#page-loading').fadeOut("slow");
        $('#wrap').fadeIn("slow");
    });
})