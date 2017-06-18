var c = document.getElementById("UserMap");
c.width = document.body.clientWidth;
c.height = document.body.clientHeight;

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
ctx.fillRect(0, 0, screen.width, screen.height);

var mousePos = {
    x: 900
    , y: 500
};
var CurPos = {
    x: screen.width/2
    , y: screen.height/2
    ,scale:(screen.width*screen.height)/20736 
};
var passerbyPos = {
    x: 500
    , y: 300
};
var moveDir = {
    x: 0
    , y: 0
};
var screenScale = {
    width: screen.width
    ,height: screen.height
};
var users = "";


var ranArray = [0,0,0,0,0,0,0,0,0,0];
var thetaArray = [0,0,0,0,0,0,0,0,0,0];
//no repeat random
for(var i = 0;i<10;i++){  
    randOvalCoordinate(i);
    console.log(i+"("+passerbyPos[i].x+","+passerbyPos[i].y+")");
    // console.log(overlapping);

}
// var overlapping = 0;
function randOvalCoordinate(i){
    // overlapping = 0;
    var r = screenScale.height/2 - CurPos.scale,
    R = screenScale.width/2 - CurPos.scale;
    var _r = Math.sqrt(Math.random()*(R*R-r*r)+r*r);
    var theta = Math.random()*2*Math.PI;
    // var theta = Math.random()*2*Math.PI;
    passerbyPos[i] = {x:Math.abs(_r*Math.cos(theta)+(screenScale.width/2- CurPos.scale*2)),y:Math.abs(_r*Math.sin(theta)/4+(screenScale.height/2- CurPos.scale*2))};
    // plot(_r*Math.cos(theta),_r*Math.sin(theta)/4);
    imgOverlapping(i);
}

function imgOverlapping(i){
    for(var j = 0;j < i;j++){
        // console.log(xJudge(i,j,1)+xJudge(i,j,2)+yJudge(i,j,1)+yJudge(i,j,2));
        // xJudge(1);xJudge(2);yJudge(1);yJudge(2);
        if((xJudge(i,j,1)&&xJudge(i,j,1)) || (xJudge(i,j,1)&&xJudge(i,j,2)) || (xJudge(i,j,2)&&xJudge(i,j,1)) || (xJudge(i,j,2)&&xJudge(i,j,2))){
            // console.log("re1");
            randOvalCoordinate(i);
            // console.log("re2");
            break;
        }

        if(((passerbyPos[i].x+CurPos.scale) > screen.width) || ((passerbyPos.y+CurPos.scale+200) > screen.height)){
            // console.log("out");
            randOvalCoordinate(i);
        }
    }
}
var extraScale = CurPos.scale*2;
function xJudge(i,j,k){
    if(k==1)
        if(passerbyPos[i].x <= (passerbyPos[j].x + CurPos.scale) && (passerbyPos[i].x)>= (passerbyPos[j].x ))
            return 1;
    else
        if((passerbyPos[i].x + CurPos.scale)<= (passerbyPos[j].x + CurPos.scale ) && (passerbyPos[i].x + CurPos.scale)>= (passerbyPos[j].x))
             return 1;
}

function yJudge(i,j,k){
    if(k==1)
        if(passerbyPos[i].y <= (passerbyPos[j].y + CurPos.scale) && (passerbyPos[i].y)>= (passerbyPos[j].y - extraScale))
            return 1;
    else
        if((passerbyPos[i].y + CurPos.scale)<= (passerbyPos[j].y + CurPos.scale) && (passerbyPos[i].y + CurPos.scale)>= (passerbyPos[j].y))
            return 1;
}

var hasAddFriend = [];
var hasAddFriendIndex = 0;
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
        console.log("currentElement.scrollTop: "+currentElement.offsetTop+" ,"+currentElement.scrollTop);
    }
    while (currentElement = currentElement.offsetParent)
    canvasX = event.pageX - totalOffsetX;
    canvasX = event.pageX ;
    // canvasY = event.pageY - totalOffsetY;
    canvasY = event.pageY+50;
    // canvasY = event.pageY-80;
    // console.log("pageX: "+event.pageX+" ,"+event.pageY);

    // console.log("canvasX: "+canvasX+" ,"+canvasY);
    console.log("CurPos",CurPos.x,',',CurPos.y)
    for(var i = 0;i< 10;i++){
        if ((canvasX >= passerbyPos[i].x && canvasX <= (passerbyPos[i].x + CurPos.scale)) && (canvasY >= (passerbyPos[i].y+ CurPos.scale) && canvasY <= (passerbyPos[i].y + CurPos.scale*2))) {
            currentStranger = i;
            $(currentElement).css( 'cursor', 'pointer' );
            $("#introImg").attr("src",icons[Object.keys(icons)[i]].fields.UserIcon);
            // $("#introImg").css('border-radius','60%');
            users = icons[Object.keys(icons)[i]];
            $("#introName").html(users.fields.UserName);
            $("#introLanguage").html(alllanguage[Object.keys(alllanguage)[users.fields.NativeLanguage-1]].fields.Language);
            $('.userintro-sentence').html(friendSentencelist[Object.keys(friendSentencelist)[i]].fields.Content)
            
            $('#message-btn').attr('class','modalbtn addbtn');
            $('#message-btn').attr('onclick','AddFriend()');
            $('#message-btn').html('add friend');
            if(userFriends){
                console.log("true");
                for(var j = 0;j< userFriends.length;j++){
                    if(userFriends[Object.keys(userFriends)[j]].fields.Friend == users.pk){
                        $('#message-btn').attr('class','modalbtn messagebtn');
                        $('#message-btn').attr('onclick','');
                        $('#message-btn').html('message');
                        console.log("are friend");
                        break;
                    }
                }
            }
            for(var j = 0;j< hasAddFriend.length;j++){
                    console.log('array '+hasAddFriend[j]+' ' + users.pk);
                    if(hasAddFriend[j] == users.pk){
                        $('#message-btn').attr('class','modalbtn messagebtn');
                        $('#message-btn').attr('onclick','');
                        $('#message-btn').html('message');
                        console.log("are friend add");
                        break;
                    }
                }
            $("#passerIntro").modal();
           //GetProfile(proPasser);
        }
    }
});
function AddFriend(){
    hasAddFriend[hasAddFriendIndex++] = users.pk;
    var FriendID = icons[Object.keys(icons)[currentStranger]].pk;
    console.log("UID" +FriendID);
    $.get('/addfriend/',{
           UID: FriendID
    },function(data){
        $("#friendlist_certain_content").html(data);
    });
}

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

    DrawIcons(userImg, CurPos.x, CurPos.y,userSentence[Object.keys(userSentence)[0]].fields.Content );

    /*No Picture*/
    for(var i = 0;i< 10;i++){
        if(icons != null && friendSentencelist != null){
            DrawIcons(icons[Object.keys(icons)[i]].fields.UserIcon, passerbyPos[i].x, passerbyPos[i].y,friendSentencelist[Object.keys(friendSentencelist)[i]].fields.Content );
        }
    }
    
}, 30);
// console.log('icon '+icons[1].src);
//image
var DrawIcons = function (isrc, pox, poy, sentence) {
    var ic = new Image();
    ic.src = isrc;
    var sentLenght = CurPos.scale*3.5;
    var textHeight = 10;
    var radius = 15;
    var horn = 10;
    var neck = 20;
    var bubbleX = pox + CurPos.scale;
    var bubbleY = poy;
    ctx.save();//push current state into canvas
    ctx.beginPath();
    ctx.moveTo(bubbleX, bubbleY+horn);
    ctx.lineTo(bubbleX+horn, bubbleY);
    ctx.lineTo(bubbleX+radius, bubbleY);
    ctx.quadraticCurveTo(bubbleX,bubbleY,bubbleX,bubbleY-radius);
    ctx.lineTo(bubbleX, bubbleY-textHeight-radius);
    ctx.quadraticCurveTo(bubbleX,bubbleY-2*radius-textHeight,bubbleX+radius,bubbleY-2*radius-textHeight);
    ctx.lineTo(bubbleX+radius+sentLenght, bubbleY-2*radius-textHeight);
    ctx.quadraticCurveTo(bubbleX+radius*2+sentLenght,bubbleY-2*radius-textHeight,bubbleX+radius*2+sentLenght,bubbleY-textHeight-radius);
    ctx.lineTo(bubbleX+radius*2+sentLenght,bubbleY-radius);
    ctx.quadraticCurveTo(bubbleX+radius*2+sentLenght,bubbleY,bubbleX+radius+sentLenght,bubbleY);
    ctx.lineTo(bubbleX+horn+neck,bubbleY);
    // ctx.lineTo(pox + CurPos.scale, poy - 10);
    ctx.fillStyle = 'rgba(150, 254, 209,0.3)';
    ctx.fill();
    ctx.closePath();
    ctx.clip();
    ctx.fillStyle = "black";
    ctx.fillText(sentence, bubbleX+radius, poy - radius);
    ctx.restore();

    ctx.save();
    ctx.beginPath();
    ctx.arc(pox+CurPos.scale/2, poy+CurPos.scale/2, CurPos.scale/2, 0, 2 * Math.PI);
    // ctx.fillStyle = '#FFFFFF';
    // ctx.fill();
    ctx.closePath();
    ctx.clip();
    
    ctx.drawImage(ic, pox, poy, CurPos.scale, CurPos.scale);
    ctx.restore();
    
};


//message
$('#message-btn').click(function() {
    $('.friendname').html(users.fields.UserName);
    $("#friendimg").attr("src",users.fields.UserIcon);
    $('#passerIntro').appendTo("body").modal('hide');
    $('#messagemodal').appendTo("body").modal('show');
    $.get('/message/'+ users.pk+'/',function(data){
        $('.message-dialogcontent').html(data);
        // $('.message-dialogcontent').animate({ scrollTop: $('.message-dialogcontent').prop("scrollHeight")}, 1000);
        $('.friendmsgcount').html($(".message-historylist li").length);
    });
});

$('#messageform').on('keyup', 'textarea', function (event) {
    if (event.keyCode == 13 && !event.shiftKey) {
        event.preventDefault;
        $('.modalbtn.sendbtn').click();
    }
});
// $('#messageform').attr('action','/message/'+ users.pk+'/');
$('#messageform').submit(function(event) {
    event.preventDefault();
    var $form = $( this ),
    message = $.trim ($('.message-sendframe').val());
    var posting = $.post('/message/'+ users.pk+'/',{
           'message': message
        });

    posting.done(function( data ) {
        $('.message-dialogcontent').html(data);
        $('.message-dialogcontent').animate({ scrollTop: $('.message-dialogcontent').prop("scrollHeight")}, 'toggle');
        // $('.message-dialogcontent').scrollTop($('.message-dialogcontent')[0].scrollHeight);
        // $('#postshow-modal').modal('show');
        $('.friendmsgcount').html($(".message-historylist li").length);
      });
    $('.message-sendframe').val("");
});

/*catch before create*/
// var msgHeader = ".message-username";
// var msgContain = ".message-contain";
// var isMsgVisable = true;
// $("body").on('click', msgHeader, function () {
//     //var windowBottom = $(window).scrollTop() + $(window).height();
//     //alert($(msgContain).position().top);
//     //if ((windowBottom - $(msgContain).position().top) > 0) {
//     if (isMsgVisable) {
//         $(msgContain).css('bottom', '-360px');
//         isMsgVisable = false;
//     }
//     else {
//         $('.message-contain').css('bottom', '0px');
//         isMsgVisable = true;
//     }
// });

// var userPro = "#bigV-message";
// // var CallMessage = function () {
//     $(userPro).click(function () {
//         if ($('#' + users.fields.UserName).length == 0) {
//             $('#message-area').append('<div id="' + users.fields.UserName + '" class="message-contain"><div class="message-username">' + users.fields.UserName + '</div><textarea class="message-textarea" placeholder="message" row="2"></textarea><button class="message-send">Send</button><div class="messages" name="mesag"><div class="message-box"></div></div></div>');
//         }
//     });
// // };
// //chat-box js
// var arr = [];
// var count = 0;
// for (var i = 48; i <= 122; i++) {
//     var res = String.fromCharCode(i);
//     arr[count] = res;
//     count++;
// }
// $('body').on('keyup', 'textarea', function (event) {
//     if (event.keyCode == 13 && !event.shiftKey) {
//         event.preventDefault;
//         $('.message-send').click();
//     }
// });
// //$('.message-send').each(function (i) {
// $('body').each(function (i) {
//     $(this).on('click', '.message-send', function () {
//         message = $('.message-textarea').val();
//         $.get('/message/'+ users.pk+'/',{
//            'message': message
//         },function(data){
            
//         });
//         if ($('.messages').height() > ($('.message-contain').height())) {
//             $('.messages').css('overflowY', 'scroll');
//         }
//         if ($('textarea').val().length > 1) {
//             $('.messages').append('<div class="message-box"><p class="message"></p></div>');
//             $('.message').eq(i - 1).text($('textarea').val()).addClass('push');
//             $('textarea').val('');
//             $('textarea').focus();
//             //reply
//             /*$('.messages').append('<div class="reply-box"><span class="glyphicon glyphicon-bell"></span><p class="reply"></p></div>');
//             $('.reply').eq(i - 1).html(arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()] + arr[(Math.floor((Math.random()) * (arr.length))).toString()]).addClass('push2');
//             $('.reply-box span').addClass('push2');*/
//         }
//         else {
//             $('textarea').val('');
//             $('textarea').focus();
//         }
//         var mesag = document.getElementsByName('mesag');
//         mesag.scrollTop = mesag.scrollHeight;
//     });
// });


// $(function() {
//     $(c ).draggable();
// });
