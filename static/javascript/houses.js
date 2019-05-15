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
var csrftoken = getCookie('csrftoken');

$(document).on('click', '#fav_button', (e) =>{
    e.preventDefault();
    const el = $(e.currentTarget);
    house_id = el.data("id");
    set = "";
    if (el.children()[0].innerHTML === "turned_in_not"){
        set = "set";
        el.children()[0].innerHTML = "turned_in"
    }
    else if(el.children()[0].innerHTML === "turned_in"){
        el.children()[0].innerHTML = "turned_in_not"
    }
    $.ajax({
            url: `profile/toggleWishListItem/${house_id}/?${set}`,
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
        $.ajax({
            url: url,
            type: 'GET',

            success: function(resp) {
                let newHtml;
                let houseshtml = $('.housess');
                console.log(resp.data.length);
                if(resp.data.length === 0){

                    houseshtml.html(`
                                             <h3 class="red-text center" style="margin-top: 5em"</h3>
                                                 <p>Engar niðurstöður fundust við þessar upplýsingar</p>
                                            <i style="font-size: 2em" class="center material-icons">error</i>
                                                `);
                }
                else{
                    newHtml = resp.data.map(d => {
                        console.log(d.street_nr)
                        return `
                            <section>
    <div class="col s12 m6 l4">
        <div class="card">
            <div class="card-image">
                <img style="height: 250px"  alt="${ d.address }" src="${ d.img_src }">
            </div>
            <div class= "card-content">
                <article>
                    <span class="card-title">${ d.address }<div style="width: 30px!important; margin: 0 auto" class="right">
                            <a id="fav_button" data-id="${d.id}" href="#">
                                <i style="font-size: 1.5em;" class="material-icons">turned_in_not</i>
                            </a>
                        </div>
                    </span>

                    <small>${ d.p_code } <span class="right">${ d.price  } kr</span></small>
                    <p class="truncate">${d.desc }</p>
                    <br>
                    <p>
                        <b>${d.type }</b> sem að er <b>${d.size }</b> fermetrar og hefur <b>${d.rooms }</b> herbergi</p>
                    <small>${d.sellingdate }</small>
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
                // TODO nett TODO
                console.error(error)
            }

        })

    })
});