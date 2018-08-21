$(document).ready(
  function(){
    //after document is loaded:

    //select last item from navbar
    $(".navbar-nav:first li:last").addClass("active");

    // padding of top of webpage
    var navHeight = $("#topNavbar").height() + 50;
    $("#mainContainer").css("margin-top",navHeight+"px");
    console.log("margin-top:"+navHeight+"px");
  }
);
