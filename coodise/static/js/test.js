$(document).ready(
  function(){
    // just note
    var input = $(".test").addClass("red");
    // alert("found "+ input.length);
    $(".test li:last").hover(function() {
      $(this).addClass("green");
    },function(){
      $(this).removeClass("green");
    });

    $("#prvyUl li:first").hover(
      function(){
        $(this).addClass("blue");
      },function(){
        $(this).removeClass("blue");
        $(this).removeClass("red");
      }
    );

  }
);
