var c = document.getElementById("UserMap");
var ctx = c.getContext("2d");
ctx.font = "18px Georgia";
// Create gradient
var xEnd  = 0;
var yEnd = 400;
var grd = ctx.createLinearGradient(0, 0, xEnd, yEnd);
grd.addColorStop(0, "white");
grd.addColorStop(1, "#05a3d6");
// Fill with gradient
ctx.fillStyle = grd;
ctx.fillRect(0, 0, 2000, 1000);


/*var icon = new Image();
icon.src = "";*/
/*icon.id="myIntro";
icon.style.bolder = '2px solid red';
*/
var mousePos = {
    x: 900
    , y: 500
};
var CurPos = {
    x: 800
    , y: 500
};
var passerbyPos = {
    x: 500
    , y: 300
};
var moveDir = {
    x: 0
    , y: 0
};
//var PosChange = false;
/*var proPasser = {
    'nickname': "BigV"
    , 'level': 1
    , 'TDSent': "I have a pen."
    , 'Languages': 'English'
    , 'icon': 'Imgae/whale.png'
};*/
//Click icons
$(c).on("click", function (event) {
    var totalOffsetX = 0;
    var totalOffsetY = 0;
    var canvasX = 0;
    var canvasY = 0;
    var currentElement = this;
    do {
        totalOffsetX += currentElement.offsetLeft - currentElement.scrollLeft;
        totalOffsetY += currentElement.offsetTop - currentElement.scrollTop;
    }
    while (currentElement = currentElement.offsetParent)
    canvasX = event.pageX - totalOffsetX;
    canvasY = event.pageY - totalOffsetY;
    if ((canvasX >= passerbyPos.x && canvasX <= passerbyPos.x + 100) && (canvasY >= passerbyPos.y && canvasY <= passerbyPos.y + 100)) {
        $(currentElement).css( 'cursor', 'pointer' );
        $("#passerIntro").modal();
       //GetProfile(proPasser);
    }
});
/*var GetProfile = function (pro) {
    var userID = pro.nickname + "Intro";
    if ($(userID).length == 0) {
        $('.intro').append('<div role="dialog" class="modal fade" id="' + userID + '"></div>');
        $('.intro').attr('Tittle',userID, pro.nickname);
        $(userID).dialog({
            autoOpen: true
            , buttons: [
                {
                    text: 'Message'
                    , class: 'btn btn-primary'
                    , click: CallMessage()
                }, {
                    text: 'Add'
                    , class: "btn btn-default"
                    , click: function () {
                        $(this).dialog('close')
                    }
                }
            ]
        });
    }
    $('.intro').append('<div role="dialog" class="modal fade" id="'+userID+'"> <div class="modal-dialog"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal">&times;</button><h4 class="modal-title">'+pro.nickname+'</h4> </div><div class="modal-body"><div class="row"><div class="col-lg-2"> <img src="'+pro.icon+'"> </div><div class="col-lg-6 user-profile"><h5>LV.'+pro.level+'</h5><h5>'+pro.TDSent+'</h5><h5>'+pro.Languages+'</h5> </div></div></div><div class="modal-footer"><i class="fa fa-lg fa-commenting-o" fa-inverse></i><button type="button" class="btn btn-primary" id="bigV-message" onclick="CallMessage()" data-dismiss="modal">message</button><button type="button" class="btn btn-default" data-dismiss="modal">add</button></div></div></div></div>');
};*/
document.addEventListener('mousedown', function (e) {
    //ctx.clearRect(0, 0, c.width, c.height);
    mousePos = {
        x: e.clientX
        , y: e.clientY
    };
    moveDir = {
        x: mousePos.x - CurPos.x
        , y: mousePos.y - CurPos.y
    };
}, false);
setInterval(function () {
    if ((Math.abs(CurPos.x - mousePos.x) >= 0.1) && (Math.abs(CurPos.y - mousePos.y) >= 0.1)) {
        grd.addColorStop(0, "white");
        grd.addColorStop(1, "#05a3d6");
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, 2000, 1000);
        CurPos.x += moveDir.x * 0.1;
        CurPos.y += moveDir.y * 0.1;
    }
    
    /*No Picture*/
    
    DrawIcons(icons[0].src, passerbyPos.x, passerbyPos.y, "у меня есть яблоко.");
    DrawIcons(icons[1].src, CurPos.x-50, CurPos.y-100, userSentence);
    
    
}, 30);
console.log('icon '+icons[1].src);
//image
var DrawIcons = function (isrc, pox, poy, sentence) {
    var ic = new Image();
    ic.src = isrc;
   // ic.onload=function(){
        // console.log();
        var sentLenght = sentence.length * 10;
        ctx.beginPath();
        ctx.moveTo(pox + 100, poy - 5);
        ctx.lineTo(pox + 100, poy - 40);
        ctx.lineTo(pox + 100 + sentLenght, poy - 40); //x:+250
        ctx.lineTo(pox + 100 + sentLenght, poy - 10); //x:+250
        ctx.lineTo(pox + 110, poy - 10);
        ctx.fillStyle = '#FFFFFF';
        ctx.fill();
        ctx.closePath();
        // ic.onload=function(){
        ctx.drawImage(ic, pox, poy, 100, 100);
        ctx.fillStyle = "black";
        ctx.fillText(sentence, pox + 110, poy - 18);
        // }
   // };
};
//message
/*catch before create*/
var msgHeader = ".message-username";
var msgContain = ".message-contain";
var isMsgVisable = true;
$("body").on('click', msgHeader, function () {
    //var windowBottom = $(window).scrollTop() + $(window).height();
    //alert($(msgContain).position().top);
    //if ((windowBottom - $(msgContain).position().top) > 0) {
    if (isMsgVisable) {
        $(msgContain).css('bottom', '-360px');
        isMsgVisable = false;
    }
    else {
        $('.message-contain').css('bottom', '0px');
        isMsgVisable = true;
    }
});
var users = "BigV";
var userPro = "#bigV-message";
var CallMessage = function () {
    $(userPro).click(function () {
        if ($('#' + users).length == 0) {
            $('#message-area').append('<div id="' + users + '" class="message-contain"><div class="message-username">' + users + '</div><textarea class="message-textarea" placeholder="message" row="2"></textarea><button class="message-send">Send</button><div class="messages" name="mesag"><div class="message-box"></div></div></div>');
        }
    });
};
//chat-box js
var arr = [];
var count = 0;
for (var i = 48; i <= 122; i++) {
    var res = String.fromCharCode(i);
    arr[count] = res;
    count++;
}
$('body').on('keyup', 'textarea', function (event) {
    if (event.keyCode == 13 && !event.shiftKey) {
        event.preventDefault;
        $('.message-send').click();
    }
});
//$('.message-send').each(function (i) {
$('body').each(function (i) {
    $(this).on('click', '.message-send', function () {
        if ($('.messages').height() > ($('.message-contain').height())) {
            $('.messages').css('overflowY', 'scroll');
        }
        if ($('textarea').val().length > 1) {
            $('.messages').append('<div class="message-box"><p class="message"></p></div>');
            $('.message').eq(i - 1).text($('textarea').val()).addClass('push');
            $('textarea').val('');
            $('textarea').focus();
            //reply
            /*$('.messages').append('<div class="reply-box"><span class="glyphicon glyphicon-bell"></span><p class="reply"></p></div>');
            $('.reply').eq(i - 1).html(arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()]).addClass('push2');
            $('.reply-box span').addClass('push2');*/
        }
        else {
            $('textarea').val('');
            $('textarea').focus();
        }
        var mesag = document.getElementsByName('mesag');
        mesag.scrollTop = mesag.scrollHeight;
    });
});

// $(function() {
//     $(c ).draggable();
// });
