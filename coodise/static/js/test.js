function add(a,b){
  return a + b;
}

function sum(){
  var i, sum = 0;
  for(i = 0; i < arguments.length; i++){
    sum += arguments[i];
  }
  return sum;
}

$(document).ready(
  function(){
    // just note
    $('a[href*=#]').addClass('red');
    $('a[href*="http://"]').addClass('green');
    $('a[href$=pdf]').after(' – PDF subor');
    $('a[href$=xls]').after(' – XLS subor');
    console.log(add(1,2));
    console.log(sum(1,2,3,4,5));
  }
);
