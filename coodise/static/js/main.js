$(document).ready(function(){

  $("input").addClass("form-control")

  $('.modal.fade').on('show.bs.modal', function()
    {
      // if modal is shown
      var preview_div = $(this).find('.picture_source');
      var modal_body = $(this).find('.modal-body');
      var img_exist = $(this).find('.rounded.preview').length;
      if (img_exist == 0) {
        var img = $("<img />").attr('src', preview_div.text());
        img.attr('class', 'rounded preview');
        modal_body.append(img);
      }
    }
  );

  $('.badge.spoiler').click(
    // when clicked on badge inside link
    function(event){
      $(this).parent().prop("title","Doubleclick to open link");
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
