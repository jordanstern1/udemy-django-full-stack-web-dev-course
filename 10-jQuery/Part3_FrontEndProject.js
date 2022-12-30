var p1 = prompt("Player One: Enter Your Name, you will be Blue")
var p2 = prompt("Player Two: Enter Your Name, you will be Red")

var i = 1 // index to count how many moves have been played
var className = 'turnBlue';
// var lastClicks =

$('.circle').click(function() {
  var id = $(this).attr('id');
  remainder = id % 7;
  colNum = (remainder === 0) ? 7 : remainder;

  
  if (i % 2 == 0) {
    className = 'turnBlue';
  }
  else {
    className = 'turnRed';
  }

  console.log('i' + i)
  console.log('id' + id)
  
  $('#' + id).toggleClass(className)
 
  i++;
  
});


// $('h3').text()

var circle_id = $('.circle').click(function() {
  i++;
  if (i % 2 == 0) {
    className = 'turnBlue';
  }
  else {
    className = 'turnRed';
  }
  $(this).data("id");
})

var click_count = 0;
remainder = click_count % 7;
if (remainder == 1) {

} else if (remainder == 2) {
  
}