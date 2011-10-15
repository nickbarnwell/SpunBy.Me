$.getJSON('party/1/queue',function(data) {
  console.log(data);
});

function generateEntry(item) {
  $entry = <div class="entry">
  $info = <div class="info">
  $vote = <div class="vote">
  $upvote = <div class="upvote"></div>
    <div class="votecount">10</div>
    <div class="downvote"></div>
  </div>
  <h2>Around the World</h2>
  <h3>Daft Punk</h3>
</div> <!-- close info -->
</div> <!-- close entry -->
}


/*
 * Change out the video that is playing
 */

// Update a particular HTML element with a new value
function updateHTML(elmId, value) {
  document.getElementById(elmId).innerHTML = value;
}

// Loads the selected video into the player.
function loadVideo() {
  var selectBox = document.getElementById("videoSelection");
  var videoID = selectBox.options[selectBox.selectedIndex].value
  
  if(ytplayer) {
    ytplayer.loadVideoById(videoID);
  }
}

// This function is called when an error is thrown by the player
function onPlayerError(errorCode) {
  alert("An error occured of type:" + errorCode);
}

// This function is automatically called by the player once it loads
function onYouTubePlayerReady(playerId) {
  ytplayer = document.getElementById("ytPlayer");
  ytplayer.addEventListener("onError", "onPlayerError");
}

// The "main method" of this sample. Called when someone clicks "Run".
function loadPlayer(videoID) {
  // Lets Flash from another domain call JavaScript
  var params = { allowScriptAccess: "always" };
  // The element id of the Flash embed
  var atts = { id: "ytPlayer" };
  // All of the magic handled by SWFObject (http://code.google.com/p/swfobject/)
  swfobject.embedSWF("http://www.youtube.com/v/" + videoID + 
                     "?version=3&enablejsapi=1&playerapiid=player1", 
                     "videoDiv", "480", "295", "9", null, null, params, atts);
}
function _run() {
  loadPlayer("ylLzyHk54Z0");
}
google.setOnLoadCallback(_run);