$(document).ready(function() {
  $.getJSON('http://phoenix.dyn.cs.washington.edu:8000/party/1/queue',function(data) {
    for (track in data) {
      generateEntry(track);
    }
  });
});

function generateEntry(track) {
  $entry = $('<div class="entry">');
  $info = $('<div class="info">');
  $vote = $('<div class="vote">');
    $upvote = $('<div class="upvote">');
    $votecount = $('<div class="votecount">10</div>');//10
    $downvote = $('<div class="downvote">');

  $song_title = $('<h2>Around the World</h2>');
  $song_title.text(track.title);
  $artist = $('<h3>Daft Punk</h3>');
  $artist.text(track.artist);

  $upvote.appendTo($vote);
  $votecount.appendTo($vote);
  $downvote.appendTo($vote);

  $vote.appendTo($info);
  $song_title.appendTo($info);
  $artist.appendTo($info);

  $info.appendTo($entry);

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
