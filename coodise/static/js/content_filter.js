$(document).ready(function(){
  $("#filterInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    // console.log(value)
    $(".list-group a").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
