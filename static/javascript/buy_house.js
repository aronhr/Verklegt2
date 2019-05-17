$(document).ready(function(){
    $('.modal').modal();
    $('#modal2').modal('open');
    $('#tilbod').on('click', () => {
        var price = $('#id_price').val();
        console.log(price);
        var model = $('#price_modal');
        console.log(model.innerHTML);
        model.html = price;
        console.log()
    })
});

