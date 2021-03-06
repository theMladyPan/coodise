(function ($, window) {

    $.fn.contextMenu = function (settings) {

        return this.each(function () {

            // Open context menu
            $(this).on("contextmenu", function (e) {
                // return native menu if pressing control
                if (e.ctrlKey) return;
                //open menu
                var $menu = $(settings.menuSelector)
                    .data("invokedOn", $(e.target))
                    .show()
                    .css({
                        position: "absolute",
                        left: getMenuPosition(e.clientX, 'width', 'scrollLeft'),
                        top: getMenuPosition(e.clientY, 'height', 'scrollTop')
                    })
                    .off('click')
                    .on('click', 'a', function (e) {
                        $menu.hide();

                        var $invokedOn = $menu.data("invokedOn");
                        var $selectedMenu = $(e.target);

                        settings.menuSelected.call(this, $invokedOn, $selectedMenu);
                    });

                return false;
            });

            //make sure menu closes on any click
            $('body').click(function () {
                $(settings.menuSelector).hide();
            });
        });

        function getMenuPosition(mouse, direction, scrollDir) {
            var win = $(window)[direction](),
                scroll = $(window)[scrollDir](),
                menu = $(settings.menuSelector)[direction](),
                position = mouse + scroll;

            // opening menu would pass the side of the page
            if (mouse + menu > win && menu < mouse)
                position -= menu;

            return position;
        }

    };
})(jQuery, window);

function copyText(text){
  var dummy = document.createElement("input");
  document.body.appendChild(dummy);
  dummy.setAttribute("id", "dummy_id");
  document.getElementById("dummy_id").value=text;
  dummy.select();
  document.execCommand("copy");
  document.body.removeChild(dummy);
  }

function renameItem(item){
  var path = item.getAttribute("data-path").split("/"); // backend side file
  path = path[path.length -1]
  var $modal = $("#modal-rename");
  $modal.find(".modal-title").text("Rename " + path);
  $modal.find('input[name="new_name"]').val(path)
  $("#id_old_name").val(path);
  $modal.modal("show")
}

function deleteItem(item){
  var path = item.getAttribute("data-path"); // backend side file
  var $modal_body = $("#modal-delete").find(".modal-body");
  $modal_body.find('input[name="item_to_delete"]').val(path);
  path=path.split("/");
  path = path[path.length -1]
  var $message = $modal_body.find(".message");
  $message.html("<p>Do you really want to <strong>delete "+path+"</strong>? This operation can <strong>not</strong> be undone.</p>");

  // find if directory have any subdirectories
  if (item.getAttribute("data-type") === "directory"){
    nOfFiles = $(item).find(".n-of-files").text().split("/")
    if (nOfFiles[0] > 0 || nOfFiles[1] > 0){
      $message.append('<p class="alert alert-danger">Warning! Directory contains files or other subdirectories.</p>')
    }
  }
  $("#modal-delete").modal("show");
}

$(".menu-items").contextMenu({
    menuSelector: "#contextMenu",
    menuSelected: function (invokedOn, selectedMenu) {
      var menuNumber = selectedMenu[0].getAttribute("tabindex");
      switch (menuNumber){
        case "1":
          // Rename
          renameItem(invokedOn[0]);
          break;
        case "2":
          // Copy link
          var href =  invokedOn[0].getAttribute("href");
          if (href[0] === "/"){
            var text2copy = window.location.protocol + "//" + window.location.host + href;
          }else{
            var text2copy = window.location.href.replace(/#.*$/,'') + href;
          }
          console.log("Copied into clipboard:", text2copy);
          copyText(text2copy);
          break;
        case "-1":
          // Delete
          deleteItem(invokedOn[0])
          break;
        default:
          break;
      }
        var msg = "You selected the menu item '" + selectedMenu.text() +
            "' on the value '" + invokedOn.text() + "'";
        // alert(msg);
    }
});
