



$(function($) {
   
    var temp = 2;
    var coordinate = [0,50,0,0,0,90,-40,50,30,50];//0:中間 2:中上 4:中下 6:左邊 8:右邊
    $('#float-sentence').mouseover(function() {
//        var dWidth = $(document).width() * 0.7 , // 100 = image width
//            dHeight = $(document).height() * 0.7  , // 100 = image height
//            nextX = Math.floor(Math.random() * dWidth),
//            nextY = Math.floor(Math.random() * dHeight);
       do{var  i = Math.floor(Math.random() * 5);}while(temp == i)
            
            $(this).animate({ left: coordinate[i*2] + 'vw', top: coordinate[i*2+1] + 'vh' },500);
            temp = i;
            
        
       
    });
});

