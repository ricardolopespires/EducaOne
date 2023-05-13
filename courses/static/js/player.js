




function upload(){

  // create the video element but don't add it to the page
  var vid = document.createElement('video');
  document.querySelector('#duration').addEventListener('change', function() {
    // create url to use as the src of the video
    var fileURL = URL.createObjectURL(this.files[0]);
    vid.src = fileURL;
    // wait for duration to change from NaN to the actual duration
    vid.ondurationchange = function() {

      var hour = Math.floor(this.duration / 3600);
      var min = Math.floor(this.duration / 60 );
      var seg = Math.floor(((this.duration / 60) % 1) * 60)

      if( hour<10 ){

        hour = "0" + String(hour);
      }
      if (min < 10){
        min = "0" + String(min);
      }else if(min > 59){
        min = min - (Math.floor(min / 60) * 60);
      }
      if(seg<10){

        seg = "0" + String(seg)
      }

      document.getElementById('tempo').value = hour +":"+String(min)+":"+String(seg) ;
    };
  });

}


upload();