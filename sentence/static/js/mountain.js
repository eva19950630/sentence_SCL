(function() {
  var Mountain, MountainRange, dt, mountainRanges, sketch, allI;

  sketch = Sketch.create();

  sketch.mouse.x = sketch.width / 10;

  sketch.mouse.y = sketch.height;

  mountainRanges = [];

  

  dt = 1;

  Mountain = function(config) {
    return this.reset(config);
  };

  Mountain.prototype.reset = function(config) {
    this.layer = config.layer;
    this.x = config.x;
    this.y = config.y;
    this.width = config.width;
    this.height = config.height;
    return this.color = config.color;
  };

  MountainRange = function(config) {
    this.x = 0;
    this.mountains = [];
    this.layer = config.layer;
    this.width = {
      min: config.width.min,
      max: config.width.max
    };
    this.height = {
      min: config.height.min,
      max: config.height.max
    };
    this.speed = config.speed;
    this.color = config.color;
    this.populate();
    return this;
  };

  MountainRange.prototype.populate = function() {
    var newHeight, newWidth, results, totalWidth;
    totalWidth = 0;
    results = [];
    while (totalWidth <= sketch.width + (this.width.max * 4)) {
      console.log(totalWidth);
      newWidth = round(random(this.width.min, this.width.max));
      newHeight = round(random(this.height.min, this.height.max));
      this.mountains.push(new Mountain({
        layer: this.layer,
        x: this.mountains.length === 0 ? 0 : this.mountains[this.mountains.length - 1].x + this.mountains[this.mountains.length - 1].width,
        y: sketch.height - newHeight,
        width: newWidth,
        height: newHeight,
        color: this.color
      }));
      results.push(totalWidth += newWidth);
    }
    return results;
  };
 var nowX = 0;
  MountainRange.prototype.update = function() {
    var firstMountain, lastMountain, newHeight, newWidth;
    this.x -= (sketch.mouse.x * this.speed) * dt;
    nowX= this.x;
    firstMountain = this.mountains[0];
    if (firstMountain.width + firstMountain.x + this.x < -this.width.max) {
      newWidth = round(random(this.width.min, this.width.max));
      newHeight = round(random(this.height.min, this.height.max));
      lastMountain = this.mountains[this.mountains.length - 1];
      firstMountain.reset({
        layer: this.layer,
        x: lastMountain.x + lastMountain.width,
        y: sketch.height - newHeight,
        width: newWidth,
        height: newHeight,
        color: this.color

      });
      return this.mountains.push(this.mountains.shift());
    }
  };
var resetX = 1000;
var resetCount = resetX;
  MountainRange.prototype.render = function() {
    var c, d, i, j, pointCount, ref;

    sketch.save();
    sketch.translate(this.x, (sketch.height - sketch.mouse.y) / 20 * this.layer);

    sketch.beginPath();
    pointCount = this.mountains.length;
    // console.log(pointCount);
    sketch.moveTo(this.mountains[0].x, this.mountains[0].y);
    for (i = j = 0, ref = pointCount - 2; j <= ref; i = j += 1) {
      // console.log(i+' '+this.mountains[i].x+' '+this.mountains[i].y);
      // console.log(ref+' '+i+' '+this.mountains.sentLenghtngth);
      c = (this.mountains[i].x + this.mountains[i + 1].x) / 2;
      d = (this.mountains[i].y + this.mountains[i + 1].y) / 2;
      
      if (allI == 4 && i == 12) { 

        // resetCount  = nowX/this.speed/1000 ;
        // // console.log(resetCount);
        // if(resetCount <= 0){
        //   resetX += 1000;
        //   resetCount = 1000;
        // }
        // console.log(this.x);
        DrawIcons(icons[0].src, resetX, 450, "у меня есть яблоко.");
        // console.log(resetX);
      //   console.log("currentx  " + resetCount);
      }
      // if (allI == 0 && i == 0 ) { 
        
      //   // console.log(this.x);
      //   DrawIcons(icons[1].src, this.mountains[i].x, 550, "у меня есть яблоко.");
      //   // console.log(resetX);
      // }
      sketch.quadraticCurveTo(this.mountains[i].x, this.mountains[i].y, c, d);
    }
    sketch.lineTo(sketch.width - this.x, sketch.height);
    sketch.lineTo(0 - this.x, sketch.height);
    sketch.closePath();
    
    sketch.fillStyle = this.color;
    sketch.fill();
    return sketch.restore();
  };

  //image
  var DrawIcons = function (isrc, pox, poy, sentence) {
      var ic = new Image();
      ic.src = isrc;
     // ic.onload=function(){
          // console.log();
          var sentLenght = sentence.length * 10;
          // sketch.beginPath();
          // sketch.moveTo(pox + 100, poy - 5);
          // sketch.lineTo(pox + 100, poy - 40);
          // sketch.lineTo(pox + 100 + sentLenght, poy - 40); //x:+250
          // sketch.lineTo(pox + 100 + sentLenght, poy - 10); //x:+250
          // sketch.lineTo(pox + 110, poy - 10);
          // sketch.fillStyle = '#FFFFFF';
          // sketch.fill();
          // sketch.closePath();
          // ic.onload=function(){
          sketch.drawImage(ic, pox, poy, 100, 100);
          sketch.fillStyle = "black";
          sketch.fillText(sentence, pox + 110, poy - 18);
          // }
     // };
  };

  sketch.setup = function() {
    var i, results;
    i = 5;
    results = [];
    while (i--) {
      results.push(mountainRanges.push(new MountainRange({
        layer: i + 1,
        width: {
          min: (i + 1) * 50,
          max: (i + 1) * 70
        },
        height: {
          min: 200 - (i * 40),
          max: 300 - (i * 40)
        },
        speed: (i + 1) * .003,
        color: 'hsl( 195, ' + (((i + 1) * 1) + 60) + '%, ' + (80 - (i * 13)) + '% )'
      })));
    }

    return results;
  };

  sketch.clear = function() {
    return sketch.clearRect(0, 0, sketch.width, sketch.height);
  };

  sketch.update = function() {
    var i, results;
    dt = sketch.dt < .1 ? .1 : sketch.dt / 16;
    dt = dt > 5 ? 5 : dt;
    i = mountainRanges.length;
    results = [];
    while (i--) {
      results.push(mountainRanges[i].update(i));
    }
    return results;
  };

  sketch.draw = function() {
    var i, results;
    i = mountainRanges.length;
    // console.log(i);
    results = [];
    while (i--) {
      allI = i;
      results.push(mountainRanges[i].render(i));
    }
    return results;
  };

  $(window).on('mousemove', function(e) {
    sketch.mouse.x = e.pageX;
    return sketch.mouse.y = e.pageY;
  });

}).call(this);