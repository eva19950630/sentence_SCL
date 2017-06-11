$(function(){
    var len = 40; // 超過40個字以"..."取代
    $(".postcard-content").each(function(i){
        if($(this).text().length>len){
            $(this).attr("title",$(this).text());
            var text=$(this).text().substring(0,len-1)+"...";
            $(this).text(text);
        }
    });

  	$("#newmorelink").click(function() {
  		console.log("new")

  		 $.get('/search/', {
                rankType:1
            },function(data){
              console.log(data);
            });

  	});


  	$("#popumorelink").click(function() {
  		$.get('/search/',{
  			rankType:0
  		},function(data){});

  	});
});


/*search page: scrollbar*/
