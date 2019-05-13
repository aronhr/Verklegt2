$(document).ready(function() {

    const from_to_param = (name) => {
        let url = "";
        const selected_from_price_el = $(`#${name}_from option:selected`)[0];
        const selected_from_price = $(selected_from_price_el).val();
        if(selected_from_price !== ""){
            url += `&${name}_from=${selected_from_price}`
        }

        const selected_to_price_el = $(`#${name}_to option:selected`)[0];
        const selected_to_price = $(selected_to_price_el).val();
        if(selected_to_price !== ""){
            url += `&${name}_to=${selected_to_price}`
        }

        return url
    };




    const checkbox_url_param = (selector, name) => {
        const is_selected = $(selector).is(":checked");
        if(is_selected){
            return `&${name}=${true}`
        }
        return ""

    }
    const url_builder = () => {

        let url = '/?ajax';
        const selected_rooms = $('#rooms option:selected');
        $.each(selected_rooms, (ix, el) => {
            const selected_rooms = $(el).val();
            if (selected_rooms !== '') {
                url += `&rooms=${selected_rooms}`
            }
        });


        const selected_postal = $('#postal_codes option:selected');
        $.each(selected_postal, (ix, el) => {
            const p_code = $(el).val();
            if (p_code !== '') {
                url += `&p_code=${p_code}`
            }
        });

        const selected_types = $('#types option:selected');
        $.each(selected_types, (ix, el) => {
            const selected_types = $(el).val();
            if (selected_types !== '') {
                url += `&types=${selected_types}`
            }
        });


        url += from_to_param('price');
        url += from_to_param('size');

        url += checkbox_url_param('#garage', 'garage');
        url += checkbox_url_param('#new_house', 'elevator');
        url += checkbox_url_param('#extra_apart', 'extra_apartment');
        url += checkbox_url_param('#special_eterance', 'new_building');
        url += checkbox_url_param('#lift', 'entrance');



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