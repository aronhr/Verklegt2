$(document).ready(function() {
    $('#submittion').on('click', function(e) {
        e.preventDefault();
        var search_choice = $('#type_choice').val();
        $.ajax({
            url: '/search_filter=' + search_choice,
            type: 'GET',
            success: function(resp) {
                // data er það sem að ég skýrði í views gæjanum data : form
                // map fer fer í gegnum göögnin og skilar nýjum lista af gögnum
                var newHtml = resp.data.map(d => {
                    return `<div class="well_house">
                                <a href="/house/${d.id}">
                                herna kemur þá nýtt html sem eg stíla eins og á 'mynd'
                                </a>
                            

                            </div>`
                });
                $('.housess').html(newHtml.join(''));
                $('#type_choice').val('')
                // vil samt segja að typechoice eigi samt að vera haka í þarf að finna útúr því

            },
            error: function(xhr, status, error) {
                // TODO nett TODO
                console.error(error)
            }
        })

    })
});