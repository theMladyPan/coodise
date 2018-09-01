$(document).ready(function(){

  $('.file_content.disabled').click(
    function(){
      return false;
    }
  );

  $('.modal.fade').on('show.bs.modal', function(){
    // if modal is shown
    var preview_div = $(this).find('.picture_preview');
    // <img class="rounded preview" src=""/>
    var img = $("<img />").attr('src', preview_div.text());
    img.attr('class', 'rounded preview');
    preview_div.text("");
    preview_div.append(img);

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
