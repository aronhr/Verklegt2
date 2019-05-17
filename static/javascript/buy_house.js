$(document).ready(function(){
    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }
    $('.modal').modal();
    $('#modal2').modal('open');


    $('#tilbod').on('click', () => {
        var price = $('#id_price').val();
        $('#price_modal').html(numberWithCommas(price));
    });

    $(document).keydown(function (event) {
        if(event.keyCode == 13){
            $('#modal1').modal('open');
        }
    });


});


