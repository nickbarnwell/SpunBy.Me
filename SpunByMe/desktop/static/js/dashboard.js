var ytQueue = [];
var currentSong = "";
var ytplayer;

$(document).ready(function() {
  $(".search .btn").click(function(evt) {
    return false;
  });
});

function SongEntry() {
  this.html = "";
  this.video_id = "";
  this.id = "";
}

function getQueue() {
  var pid = $('#party_id').val();
  $.getJSON('/party/'+pid+'/queue/',function(data) {
    $("#playlist .entry").remove();
    ytQueue = [];
    if(currentSong) {
      currentSong.html.css("backgroundColor","#33CC33");
      currentSong.html.appendTo($('#playlist'));
    }
    for (track in data) {
      var newSong = new SongEntry();
      $html = generateEntry(data[track]);
      newSong.html = $html;
      newSong.id = data[track].id;
      newSong.html.appendTo($("#playlist"));
      newSong.video_id = data[track].video_id;
      ytQueue.push(newSong);
    }
  }); 
};

function generateEntry(track) {
  var $entry = $('<div class="entry">');
  var $info = $('<div class="info">');
  var $vote = $('<div class="vote">');
  //var $upvote = $('<div class="upvote">');
  var vv = '[' + ((track.votes != undefined) ? track.votes : '-') + ']';
  var $votecount = $('<div class="votecount">'+vv+'</div>');
  //var $downvote = $('<div class="downvote">');

  var $song_title = $('<h2></h2>');
  $song_title.text(track.title);
  var $artist = $('<h3></h3>');
  $artist.text(track.artist);

  //$upvote.appendTo($vote);
  $votecount.appendTo($vote);
  //$downvote.appendTo($vote);

  $vote.appendTo($info);
  $song_title.appendTo($info);
  $artist.appendTo($info);

  $info.appendTo($entry);
  // $entry.appendTo($("#playlist"));
  return $entry;
}


/*
 * Change out the video that is playing
 */

// Update a particular HTML element with a new value
function updateHTML(elmId, value) {
  document.getElementById(elmId).innerHTML = value;
}

// Loads the selected video into the player.
function loadVideo(songEntry) {
  // var selectBox = document.getElementById("videoSelection");
  // var videoID = selectBox.options[selectBox.selectedIndex].value
  
  if(ytplayer) {
    ytplayer.loadVideoById(songEntry.video_id);
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
  ytplayer.addEventListener("onStateChange", "processStateChange");
  if(currentSong) {
    loadVideo(currentSong);
  }
}

function processStateChange(code) {
  if (code === 0) {
    currentSong.html.fadeOut();
    getNextSong();
  }
}

function getNextSong() {
  var pid = $('#party_id').val();
  $.getJSON('/party/'+pid+'/next',function(data) {
    if(data.status == 'Failure') {
    } else {
      var newSong = new SongEntry();
      $html = generateEntry(data);
      newSong.html = $html;
      newSong.id = data.id;
      newSong.video_id = data.video_id;
      currentSong = newSong;
      loadVideo(currentSong);
    }
  });
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
                     "videoDiv", "460", "295", "9", null, null, params, atts);
}

function getQueueTimer(timer) {
  if (timer) {
    clearTimeout(timer);
  }
  getQueue();
  setTimeout(getQueueTimer,1000);
}
function _run() {
  loadPlayer("ylLzyHk54Z0");
  getQueueTimer();
  if (ytQueue.length > 0) {
    currentSong = ytQueue.pop();
    loadVideo(currentSong);
  }
  var pid = $('#party_id').val();
  $.getJSON('/party/'+pid+'/playing', function(data) {
    if(data.status == 'Failure') {
      getNextSong();
    } else {
      var newSong = new SongEntry();
      var $html = generateEntry(data);
      newSong.html = $html;
      newSong.id = data.id;
      newSong.video_id = data.video_id;
      currentSong = newSong;
      loadVideo(currentSong);
    }
  });
}
google.setOnLoadCallback(_run);
