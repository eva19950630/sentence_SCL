var width;
$(document).on('click',function(){
  width = $( document ).width();
  if(width >= 767 && !($('input[type="search-mobile"]').is(":focus"))){
    $('.ao_menu_close').hide(); 
  }
  if(width <= 767 && !($('input[type="search-mobile"]').is(":focus"))){
      $('.ao_menu_list').slideDown(500);
      $('.ao_menu_close').hide(); 
  }
  
  
})
$(document).ready(function(){
  $(".chuj").on('click',function () {
  alert('dsa')
});
 
    $('.ao_menu_close').hide();
    $('input[type="search-mobile"] , .search-icon-loupe').click(function() { 
      
    $('.search-icon-loupe').addClass('chuj');  
    $('input[type="search-mobile"]').focus();
    $('.ao_menu_close').show();
    width = $( document ).width();
        if(width <= 767){
           $('.ao_menu_list').slideUp(500);
           
        }
   
    
   });
   $('.ao_menu_close').click(function() { 
        $('.ao_menu_close').hide();
        width = $( document ).width();
        if(width <= 767){
           $('.ao_menu_list').slideDown(500); 
           
        }
     
   });
});

$(document).ready(function(){
	$('#login-btn').click(function() {
		$('#login-modal').appendTo("body").modal('show');
	});

	$('#signup-btn').click(function() {
		$('#signup-modal').appendTo("body").modal('show');
	});
  
});

$('.nav li a').click(function(e) {
    e.preventDefault();
    $('li').removeClass('active');
    $(this).addClass('active');
});

