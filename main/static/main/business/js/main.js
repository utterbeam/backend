
(function($) {
	
	"use strict";


	/* ==============================================
     Portfolio carousel  -->
     =============================================== */

      $('#Portfolios').owlCarousel({
          loop:true,
          margin:10,
          responsiveClass:true,
          responsive:{
              0:{
                  items:1,
                  nav:true
              },
              600:{
                  items:2,
                  nav:false
              },
              1000:{
                  items:3,
                  nav:true,
                  loop:false
              }
          }
      })


	/* ==============================================
     Nivo Lightbox  -->
     =============================================== */

    $('#Portfolios a').nivoLightbox({
        effect: 'fadeScale'

	 });


    /* ==============================================
     Target menu section  -->
     =============================================== */

  $('.btn-wrap').find('a[href*=#]:not([href=#])').on('click', function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: (target.offset().top - 0)
                }, 1000);
                if ($('.navbar-toggle').css('display') != 'none') {
                    $(this).parents('.container').find(".navbar-toggle").trigger("click");
                }
                return false;
            }
        }     
    });


    /* ==============================================
     Mailchimp  -->
     =============================================== */

    $('#mc-form').ajaxChimp({
        url: 'http://codextree.us10.list-manage.com/subscribe/post?u=b02e4f21e264536eff4820875&amp;id=4d57faf2cb'
            /* Replace Your AjaxChimp Subscription Link */
    });


     /* ==============================================
     scorll animation  -->
     =============================================== */

      window.sr = ScrollReveal();

      sr.reveal('.reveal-bottom', {
        origin: 'bottom',
        distance: '20px',
        duration: 800,
        delay: 400,
        opacity: 1,
        scale: 0,
        easing: 'linear',
        reset: true
      });

      sr.reveal('.reveal-top', {
        origin: 'top',
        distance: '20px',
        duration: 800,
        delay: 400,
        opacity: 1,
        scale: 0,
        easing: 'linear',
        reset: true
      });

      sr.reveal('.reveal-left', {
        origin: 'left',
        distance: '20px',
        duration: 800,
        delay: 400,
        opacity: 1,
        scale: 0,
        easing: 'linear',
        reset: true
      });

      sr.reveal('.reveal-right', {
        origin: 'right',
        distance: '20px',
        duration: 800,
        delay: 400,
        opacity: 1,
        scale: 0,
        easing: 'linear',
        reset: true
      });
        
      sr.reveal('.reveal-left-fade', {
        origin: 'left',
        distance: '20px',
        duration: 800,
        delay: 0,
        opacity: 0,
        scale: 0,
        easing: 'linear',
        mobile: false
      });

      sr.reveal('.reveal-right-fade', {
        origin: 'right',
        distance: '20px',
        duration: 800,
        delay: 0,
        opacity: 0,
        scale: 0,
        easing: 'linear',
        mobile: false
      });
        
      sr.reveal('.reveal-right-delay', {
        origin: 'right',
        distance: '20px',
        duration: 1000,
        delay: 0,
        opacity: 0,
        scale: 0,
        easing: 'linear',
        mobile: false
      }, 500);
        
      sr.reveal('.reveal-bottom-fade', {
        origin: 'bottom',
        distance: '20px',
        duration: 800,
        delay: 0,
        opacity: 0,
        scale: 0,
        easing: 'linear',
        mobile: false
      });


})(window.jQuery);