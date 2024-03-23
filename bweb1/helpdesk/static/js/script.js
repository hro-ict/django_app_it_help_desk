$(document).ready(function() {

    $('#lettertype').change(function() {
        var selectedValue = $(this).val();

        $("body").removeClass()
         $("body").addClass(selectedValue)

    });

    //lettrsize

       $('input[name="inlineRadioOptions"]').change(function() {
        // Haal de geselecteerde waarde op
        var selectedValue = $('input[name="inlineRadioOptions"]:checked').val();
         $("body").css("font-size", selectedValue+"px")

    });


$("body").onchange("click", ".user_delete", function (){
    console.log("merhaba")
})

});





//depracated

$(document).ready(function(){
    // $("#search").submit(function(e) {
    //     console.log("Submitted")
    //     e.preventDefault();
    //     var baseUrl = "/dashboard/all_tickets/";
    //     var  search_item= $("#search_item").val()
    //     window.location.href= baseUrl+search_item

    // });
    $("#search_btn").click(function(){

        var  search_item= $("#search_item").val()
        var search_area= $("#search_area").val()
        var current_url= window.location.pathname+"/";
        if (search_item){
            window.location.href= current_url+search_area+"/"+search_item
        }
        else {
           Swal.fire({
            title: "Zoekveld is leeg",
            icon: "error"
           })
        }

        console.log(search_area)

    })


    defaults = {
        color             : '#64bd63'
      , secondaryColor    : 'red'
      , jackColor         : '#fff'
      , jackSecondaryColor: null
      , className         : 'switchery'
      , disabled          : false
      , disabledOpacity   : 0.5
      , speed             : '0.1s'
      , size              : 'default'
    }
    var elems = document.querySelectorAll('.js-switch');
      for (var i = 0; i < elems.length; i++) {
        var init = new Switchery(elems[i], defaults);
      }



$(".js-switch").change(function(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var id= $(this).attr("id")
    let state;
    let message;
    if ($(this).is(':checked')) {
        state= true
        message= "active"
    }
    else {
        state= false
        message= "active"
    }


    var post_data= {id:id, state:state}
    $.ajax({
        type: 'POST',
        url:'/dashboard/users/update',
        data: post_data,
        beforeSend: function (xhr){
          xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success:function(data){


          Swal.fire({
            title: `Gebruiker is ${message} gezet`,
            confirmButtonText: "OK",
            icon: "success"

          }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {
              location.reload()
            }
          });





        },
        error: function(){
        }
       });



})
})





$(document).ready(function(){
    // Bu fonksiyon, sayfa tamamen yüklendiğinde çalışacak olan işlevlerinizi içerir
    console.log("Sayfa tamamen yüklendi!");
    // DOM öğeleri hazır olduğunda başka işlemler yapabilirsiniz
});



  // $(".intrekken").click(function(){
  // var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  // var id= $(this).attr("id")
  // post_data= {id:id}
  //
  //
  //
  // Swal.fire({
  //         showDenyButton: true,
  //         title: "Wil je ticket intrekken?",
  //         confirmButtonText: "JA",
  //         denyButtonText: "NEE",
  //         icon: "question"
  //
  //       }).then((result) => {
  //         /* Read more about isConfirmed, isDenied below */
  //         if (result.isConfirmed) {
  //           $.ajax({
  //     type: 'POST',
  //     url:'/dashboard/user_tickets/delete',
  //     data: post_data,
  //     beforeSend: function (xhr){
  //       xhr.setRequestHeader('X-CSRFToken', csrftoken);
  //     },
  //     success:function(data){
  //       Swal.fire({
  //         icon: "success",
  //         title: `Ticket ${id} verwijderd`
  //       }).then((result)=>{
  //          if (result.isConfirmed){
  //           location.reload()
  //          }
  //       })
  //
  //
  //     },
  //     error: function(){
  //     }
  //    });
  //         }
  //       });
  //











// document.getElementById("search").addEventListener("submit", function(event) {
//     event.preventDefault();

//     var zoekterm = document.getElementById("search_item").value;
//     alert(zoekterm)
//     var baseUrl = "/dashboard/all_tickets/";


//     var nieuweUrl = baseUrl + zoekterm;
//     window.location.href = nieuweUrl;
// });



