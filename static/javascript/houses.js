function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');

$(document).on('click', '#fav_button', (e) =>{
    e.preventDefault();
    const el = $(e.currentTarget);
    let house_id = el.data("id");
    let set = "";
    if (el.children()[0].innerHTML === "turned_in_not"){
        set = "set";
        el.children()[0].innerHTML = "turned_in"
    }
    else if(el.children()[0].innerHTML === "turned_in"){
        el.children()[0].innerHTML = "turned_in_not"
    }
    $.ajax({
            url: `/profile/toggleWishListItem/${house_id}/?${set}`,
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            success: (resp) => {

            }
        }
    )
});

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

    };

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

            const elem = $(`#order option:selected`);
            const selected_order = $(elem).val();
            if (selected_order !== '') {
                url += `&order=${selected_order}`
            }

            const search = $(`input.autocomplete`);
            const search_param = $(search).val();
            url += `&search=${search_param}`
        });

        url += from_to_param('price');
        url += from_to_param('size');

        url += checkbox_url_param('#garage', 'garage');
        url += checkbox_url_param('#new_house', 'new_building');
        url += checkbox_url_param('#extra_apart', 'extra_apartment');
        url += checkbox_url_param('#special_eterance', 'new_building');
        url += checkbox_url_param('#lift', 'elevator');

        return url
    };

    $('input, select').on('change', function(e) {
        const url = url_builder();
        e.preventDefault();
        $.ajax({
            url: url,
            type: 'GET',
            success: function(resp) {
                let newHtml;
                let houseshtml = $('.housess');
                if(resp.data.length === 0){
                    houseshtml.html(`
                     <h3 class="red-text center">
                        Engar niðurstöður fundust við þessar upplýsingar
                        <br>
                        <i style="font-size: 2em" class="center material-icons">error</i>
                    </h3>`);
                }
                else{
                    newHtml = resp.data.map(d => {
                        moment.locale("is"); // Make Momentjs Icelandic
                        let date = moment(d.sellingdate).format("DD. MMMM YYYY"); // Format date
                        let icon = 'turned_in_not'; // Bookmark default
                        if (d.favorate === true) // If House is Bookmarked change Bookmark icon
                            icon = 'turned_in';

                        return `
                            <section>
    <div class="col s12 m6 l4">
        <div class="card">
            <div class="card-image">
                <img style="height: 250px"  alt="${ d.address }" src="${ d.img_src }">
            </div>
            <div class= "card-content">
                <article>
                    <span class="card-title"><strong>${ d.address }</strong><div style="width: 30px!important; margin: 0 auto" class="right">
                            <a id="fav_button" data-id="${d.id}" href="#">
                                <i style="font-size: 1.5em;" class="material-icons">${ icon }</i>
                            </a>
                        </div>
                    </span>
                    <p><strong>${ d.price } kr</strong></p>
                    <br>
                    <div style="margin-bottom: 0px" class="row">
                        <div class="col s6 m6 l6">
                            <p>Tegund: <strong>${d.type }</strong></p>
                        </div>
                        <div class="col s6 m6 l6">
                            <p class="right-align">Stærð <strong>${d.size } m²</strong></p>
                        </div>
                    </div>
                    <hr>
                    <div style="margin-bottom: 0px" class="row">
                        <div class="col s6 m6 l6">
                            <p>Byggt: <strong>${ d.year }</strong></p>
                        </div>
                        <div class="col s6 m6 l6">
                            <p class="right-align">Herbergi: <strong>${d.rooms }</strong></p>
                        </div>
                    </div>
                    <hr>
                    <small>${ date }</small>
                </article>
            </div>
            <div style="height: 75px" class="card-action">
                <a class="btn waves-effect blue darken-3 col s12 m12 l12" style="color: white" href="/house/${ d.id }">SJÁ NÁNAR</a>
            </div>
        </div>
    </div>
</section>`
                    });
                }
                houseshtml.html(newHtml.join(''));
            },
            error: function(xhr, status, error) {
                console.error(error)
            }
        })
    })
});