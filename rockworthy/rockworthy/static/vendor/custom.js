$(document).ready(function(){

    var sticky = new Waypoint.Sticky({
        element: $('#weekend-heading')[0]
    })

    var sticky = new Waypoint.Sticky({
        element: $('#upcoming-heading')[0]
    })

    $('.sticky-wrapper').addClass('hidden-md-up');

    var $grid = $('.grid').imagesLoaded( function(){
        // init Masonry after all images have loaded
        $grid.masonry({
            // options...
            itemSelector: '.grid-item',
            transitionDuration: 0,
        })
        $grid.imagesLoaded().progress(function() {
            // init Masonry
            $grid.masonry('layout');
            $('.card').removeClass('hide');
            $('.loading').addClass('hide');
        
            var waypoint = new Waypoint({
                element: document.getElementById('weekend-events-heading'),
                handler: function(direction) {
                    if(direction === 'down') {
                        $('#weekend-events-tag').removeClass('events-tag-closed');
                        $('#weekend-events-tag').addClass('events-tag-open');
                    } else {
                        $('#weekend-events-tag').addClass('events-tag-closed');                    
                        $('#weekend-events-tag').removeClass('events-tag-open');                    
                    }
        
                }
            })
        
            var waypoint = new Waypoint({
                element: document.getElementById('upcoming-events-heading'),
                handler: function(direction) {
                    if(direction === 'down') {                    
                        $('#weekend-events-tag').addClass('events-tag-closed');
                        $('#upcoming-events-tag').removeClass('events-tag-closed');
                        $('#upcoming-events-tag').addClass('events-tag-open');
                    } else {
                        $('#weekend-events-tag').removeClass('events-tag-closed');                    
                        $('#weekend-events-tag').addClass('events-tag-open');
                        $('#upcoming-events-tag').addClass('events-tag-closed');                    
                        $('#upcoming-events-tag').removeClass('events-tag-open');                    
                    }
        
                }
            })
            
          });
    
      });

      $('.grid').each(function() {
        if( !$.trim($(this).html()).length ) {
            $(this).parent().html('<div class="card" style="padding: 8px; margin: 50px;" align="center"><h1>No Events Yet.</h1></div>')
         }
    })
});