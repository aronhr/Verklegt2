$(document).ready(function() {
    const url_builder = () =>{
        let url = '/?ajax'
        const selected_rooms = $('#rooms option:selected')
        $.each(selected_rooms,(ix,el) => {
            url += `&rooms=${$(el).val()}`
        })

        const selected_postal = $('#postal_codes option:selected')
        $.each(selected_postal,(ix,el) => {
            const p_code = $(el).val()
            if(p_code !== ''){
                url += `&p_code=${p_code}`
            }

        })


        return url

    }
    $('#submit_button').on('click', function(e) {
        const url = url_builder();
        e.preventDefault();
        var search_choice = $('#type_choice').val();
        $.ajax({
            url: url,
            type: 'GET',
            success: function(resp) {
                // data er það sem að ég skýrði í views gæjanum data : form
                // map fer fer í gegnum göögnin og skilar nýjum lista af gögnum
                for (x in resp.data) {
                    console.log(resp.data[x])
                }
                var newHtml = resp.data.map(d => {
                    return `
<section>
    <div class="col s9 m6 l4">
      <div class="card">
        <div class="card-image">
          <img alt="${ d.address}" src="${ d.img_src }">
          <span class="card-title">${ d.address}</span>
        </div>
        <div class="card-content">
            <article>
                <small>${ d.p_code } <span class="right">${ d.price } kr</span></small>
                <p>Desc: ${ d.desc }</p>
                <p>Type: ${ d.type }</p>
                <p>Rooms: ${ d.rooms }</p>
                <p>Fermetrar: ${ d.size }</p>
                <small>${ d.sellingdate }</small>
            </article>
        </div>
        <div class="card-action">
          <a class="black-text" href="/house/${ d.id }">Skoða nánar</a>
        </div>
      </div>
    </div>
</section>`
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