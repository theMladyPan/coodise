$(document).ready(function(){

  $('.file_content.disabled').click(
    function(){
      return false;
    }
  );

  $('.badge.spoiler').click(
    // when clicked on badge inside link
    function(event){
       $(this).parent().click(
        // overide links click functionality and do not redirect
        function(event){
          event.preventDefault();
        }
      ).dblclick(
        function(){
          window.location = this.href;
          return false;
        }
      );
    }
  );

});
