$(function(){
  var topOfOthDiv = $(".hideshare").offset().top;
  $(window).scroll(function() {
      if($(window).scrollTop() > topOfOthDiv) { //scrolled past the other div?
          $(".share").hide(); //reached the desired point -- show div
      }
      else{
        $(".share").show();
      }
  });
});



$('.btn-search').click(function(){
  $('.searchbar').toggleClass('clicked');
  $('.stage').toggleClass('faded');

  
  if($('.searchbar').hasClass('clicked')){
    $('.btn-extended').focus();
  }
  
});