App.views.Viewport = Ext.extend(Ext.Carousel, {
    fullscreen: true,
    initComponent: function() {
	     var initialItems = new Array();
		 var party = document.getElementById('party_id').value;
		 $.ajax({
            url: '/party/' + party + '/queue',
            dataType: 'json',
            async: false,
            success: function(json) {
                for(song in json) {
                	var song = json[song];
	                initialItems.push({
					slug: song['song_id'],
					title: song['title'],
					artist: song['artist'],
					songid: song['song_id'],
					videoid: song['video_id']
				});
            }}
        });

        Ext.apply(this, {

            defaults: {
                xtype: 'paintingcard',
            },

            items: initialItems,
			listeners: {
            	beforecardswitch: function() {
					var me = this;
					$.ajax({
						async:false,
		                url: '/party/' + party + '/next',
		                dataType: 'json',
		                success: function(json) {
		                    var item = {
								slug:  json['song_id'],
								title: json['title'],
								artist: json['artist'],
								songid: json['song_id'],
								videoid: json['video_id']
							};
							if(this.getItems().peek().songid != item.songid){
								me.add(item);
								this.doLayout();
							}
		                }
		            });
					
            	}
        	}
        });
        App.views.Viewport.superclass.initComponent.apply(this, arguments);
    }
});
