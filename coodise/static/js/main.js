$(document).ready(function(){

  $('.badge').click(
    // when clicked on badge inside link
    function(){
      // console.log("Clicked on",this);
      $(this).parent().click(
        // overide links click functionality and do not redirect
        function(){
          return false;
        }
      )
    }
  )
});
