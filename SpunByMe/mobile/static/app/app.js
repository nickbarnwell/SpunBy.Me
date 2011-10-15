App = new Ext.Application({
    name: "App",

    launch: function() {
        this.views.viewport = new this.views.Viewport();
    }
});
$(document).ready( function(){
	var party = $("#party_id").val();
	$('#q').bind('keypress', function(e) {
        if(e.keyCode==13){
        	$.ajax({
            url: 'search/?q=' + $(this).val() + '/',
            dataType: 'json',
            success: function(json) {
                var html = '<ul>';
				for (song in json){
					html += '<li><a href="add_song/party/' + party + '/?artist=' + song['artist'] + '&amp;title=' + song['title']
					+ '">' + song['title'] + ' - ' + song['artist'] + '</a></li>';
				}
				$("#queryresults").html(html + '</ul>');
            }
        });
        }
	});
	$('.search .btn').click('keypress', function(e) {
        if(e.keyCode==13){
        	$.ajax({
            url: 'search/?q=' + $(this).val() + '/',
            dataType: 'json',
            success: function(json) {
                var html = '<ul>';
				for (song in json){
					html += '<li><a href="add_song/party/' + party + '/?artist=' + song['artist'] + '&amp;title=' + song['title']
					+ '">' + song['title'] + ' - ' + song['artist'] + '</a></li>';
				}
				$("#queryresults").html(html + '</ul>');
            }
        });
        }
	});
});
