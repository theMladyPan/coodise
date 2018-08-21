$(document).ready(function(){
  $(".badge").hover(
    function(){
      $(this).parent().css("pointer-events: none;");
    }, function(){
      $(this).parent().removeClass("disabled");
    }
  );
});
