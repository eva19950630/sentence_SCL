$('.fields input').on('focus', function() {
  $('.fields label').addClass('filled focused');
});

$('.fields input').on('blur', function() {
  $('.fields label').removeClass('focused');
  
  if (this.value === '') {
    $('.fields label').removeClass('filled')
  }
});

$(document).ready(function(){
	$('#post-btn').click(function() {
		$('#post-modal').appendTo("body").modal('show');
	});
});