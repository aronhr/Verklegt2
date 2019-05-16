$(document).ready(function() {
    $('textarea').characterCounter();
    $('select').formSelect();
    $('.tabs').tabs();
    $('.forward').on('click', function () {
        $('#1').removeClass('active');
        $('#2').addClass('active');
        $('.tabs').tabs();
    });
    $('.forward_2').on('click', function () {
        $('#2').removeClass('active');
        $('#3').addClass('active');
        $('.tabs').tabs()
    });
    $('.back').on('click', function () {
        $('#2').removeClass('active');
        $('#1').addClass('active');
        $('.tabs').tabs()
    })
    $('.back_2').on('click', function () {
        $('#3').removeClass('active');
        $('#2').addClass('active');
        $('.tabs').tabs()
    })
});