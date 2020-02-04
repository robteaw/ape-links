// Navbar Mobile
$('.navTrigger').click(function () {
  $(this).toggleClass('active');
  console.log("Clicked menu");
  $("#mainListDiv").toggleClass("show_list");
  $("#mainListDiv").fadeIn();

});


// Scroll to top
$(document).ready(function(){
  $(window).scroll(function(){
    if($(window).scrollTop() > 300){
      $('.goTop').css({
        "opacity":"1", "pointer-events":"auto"
      });
    }else{
      $('.goTop').css({
        "opacity":"0", "pointer-events":"none"
      });
    }
  });
  $('.goTop').click(function(){
    $('html').animate({scrollTop:0}, 500);
  });
});

// Function used to shrink nav bar removing paddings and adding black background
  $(window).scroll(function() {
      if ($(document).scrollTop() > 50) {
          $('.nav').addClass('affix');
          console.log("OK");
      } else {
          $('.nav').removeClass('affix');
      }
  });
