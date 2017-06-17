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

//random position
// for(var i =0;i<10;i++){
//     var x = Math.random()*900+100;
//     var y = Math.random()*500+100;
//     passerbyPos[i] = {x:x,y:y};
// }
//var PosChange = false;
/*var proPasser = {
    'nickname': "BigV"
    , 'level': 1
    , 'TDSent': "I have a pen."
    , 'Languages': 'English'
    , 'icon': 'Imgae/whale.png'
};*/

var ranArray = [0,0,0,0,0,0,0,0,0,0];
var thetaArray = [0,0,0,0,0,0,0,0,0,0];
//no repeat random
for(var i = 0;i<10;i++){
    // var ranInterval = Math.round(Math.random()*50);
    // ranArray[i]= ranInterval;
    // ranNoRepeat(ranInterval,i);

    // console.log("rand ranInterval "+ranArray[i]);
    // var x = (ranArray[i] % 10 )*Math.round((screen.width-200)/10);
    // var y = Math.floor(ranArray[i] / 10 )*Math.round((screen.height-200)/5);
    // passerbyPos[i] = {x:x,y:y};   
    randOvalCoordinate(i);
    console.log(i+"("+passerbyPos[i].x+","+passerbyPos[i].y+")");

}

function randOvalCoordinate(i){
    var r = screenScale.height/2 - CurPos.scale,
    R = screenScale.width/2 - CurPos.scale;
    var _r = Math.sqrt(Math.random()*(R*R-r*r)+r*r);
    var theta = Math.random()*2*Math.PI;
    // var theta = Math.random()*2*Math.PI;
    passerbyPos[i] = {x:Math.abs(_r*Math.cos(theta)+(screenScale.width/2- CurPos.scale*2)),y:Math.abs(_r*Math.sin(theta)/4+(screenScale.height/2- CurPos.scale*2))};
    // plot(_r*Math.cos(theta),_r*Math.sin(theta)/4);
    imgOverlapping(i);
}

// function NormalDistribution(){
//     var rand = 0;

//     for (var i = 0; i < 6; i += 1) {
//         rand += Math.random();
//     }

//     return rand / 6;
// }

// function gaussianRandom(start, end) {
//   return Math.floor(start + NormalDistribution() * (end - start + 1));
// }

// function ranNoRepeat(num,i,list) {
//     for(var j = i-1;j >=0 ;j--){
//         if(list[i] != list[j]){
//             list[i] = num;
//             // console.log("if true");
//         }else{
//             // console.log("in repeat");
//             ranNoRepeat(Math.round(Math.random()*50),i);
//             break;
//             // console.log("out repeat");
//         }
//     }
// }

function imgOverlapping(i){
    for(var j = 0;j < i;j++){
        if(passerbyPos[i].x <= (passerbyPos[j].x + CurPos.scale) && (passerbyPos[i].x + CurPos.scale)>= passerbyPos[j].x
            && passerbyPos[i].y <= (passerbyPos[j].y + CurPos.scale) && (passerbyPos[i].y + CurPos.scale) >= passerbyPos[j].y){
            randOvalCoordinate(i);
            break;
        }

        if(((passerbyPos[i].x+passerbyPos[i].scale) > screen.width) || ((passerbyPos.y+passerbyPos[i].scale+200) > screen.height)){
            console.log("out");
            randOvalCoordinate(i);
        }
    }
}

var currentStranger;
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
    // canvasY = event.pageY - totalOffsetY;
    canvasY = event.pageY+50;
    // console.log("pageX: "+event.pageX+" ,"+event.pageY);

    // console.log("canvasX: "+canvasX+" ,"+canvasY);
    console.log("CurPos",CurPos.x,',',CurPos.y)
    for(var i = 0;i< 10;i++){
        if ((canvasX >= passerbyPos[i].x && canvasX <= (passerbyPos[i].x + CurPos.scale)) && (canvasY >= (passerbyPos[i].y+ CurPos.scale) && canvasY <= (passerbyPos[i].y + CurPos.scale*2))) {
            currentStranger = i;
            $(currentElement).css( 'cursor', 'pointer' );
            $("#introImg").attr("src",icons[Object.keys(icons)[i]].fields.UserIcon);
            // $("#introImg").css('border-radius','60%');
            $("#introName").html(icons[Object.keys(icons)[i]].fields.UserName);
            $("#passerIntro").modal();
           //GetProfile(proPasser);
        }
    }
});
function AddFriend(){
    var FriendID = icons[Object.keys(icons)[currentStranger]].pk;
    console.log("UID" +FriendID);
    $.get('/addfriend/',{
           UID: FriendID
    },function(data){
        $("#friendlist_certain_content").html(data);
    });
}
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
   // ic.onload=function(){
        // console.log();
        // var sentLenght = sentence.length * 10;
        // ctx.beginPath();
        // ctx.moveTo(pox + 100, poy - 5);
        // ctx.lineTo(pox + 100, poy - 40);
        // ctx.lineTo(pox + 100 + sentLenght, poy - 40); //x:+250
        // ctx.lineTo(pox + 100 + sentLenght, poy - 10); //x:+250
        // ctx.lineTo(pox + 110, poy - 10);
        // ctx.fillStyle = '#FFFFFF';
        // ctx.fill();
        // ctx.closePath();
        // ic.onload=function(){
        ctx.drawImage(ic, pox, poy, CurPos.scale, CurPos.scale);
        ctx.fillStyle = "black";
        ctx.fillText(sentence, pox + (0.000053*(screen.width*screen.height)), poy - (0.00000868*(screen.width*screen.height)));
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
