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
            	console.log(json);
                for(song in json) {
                	var idx = song;
                	var song = json[song];
	                initialItems.push({
					slug: idx,
					title: song['title'],
					artist: song['artist'],
					songid: song['song_id'],
					albumart: song['albumart']
				});
				console.log(song['albumart'])
            }}
        });
        console.log(initialItems)
        Ext.apply(this, {

            defaults: {
                xtype: 'paintingcard',
            },

            items: initialItems.slice(0,-2),
			listeners: {
            	beforecardswitch: function() {
					var me = this;
					/*$.ajax({
						async:false,
		                url: '/party/' + party + '/next',
		                dataType: 'json',
		                success: function(json) {
		     //                var item = {
							// 	slug:  json['song_id'],
							// 	title: json['title'],
							// 	artist: json['artist'],
							// 	songid: json['song_id'],
							// 	albumart: json['albumart']
							// };
							// if(me.getItem().peek().songid != item.songid){
							// 	me.add(item);
							// 	this.doLayout();
							// }
		                }
		            });*/
					
            	}
        	}
        });
        console.log(initialItems)
        App.views.Viewport.superclass.initComponent.apply(this, arguments);
    }
});
