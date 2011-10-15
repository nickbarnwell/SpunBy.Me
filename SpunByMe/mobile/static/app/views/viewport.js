App.views.Viewport = Ext.extend(Ext.Carousel, {
    fullscreen: true,
    initComponent: function() {
	     intialItems = new Array();
		 var party = document.getElementById('party_id').value;
		 $.ajax({
            url: '/party/' + party + '/queue',
            dataType: 'json',
            success: function(json) {
            	console.log(json)
                for (var song=0; song<json.length; song++){
                	song = json[song];
                	intialItems.push({
					slug: '',
					title: song['title'],
					artist: song['artist'],
					songid: song['song_id'],
					videoid: song['video_id']
					});
                }
                console.log(intialItems);
                
            }
        });
        Ext.apply(this, {

            defaults: {
                xtype: 'paintingcard',
            },            
            items: intialItems,
			listeners: {
            	beforecardswitch: function() {
					var me = this;
					$.ajax({
		                url: '/party/' + party + '/next',
		                dataType: 'json',
		                success: function(json) {
		                    var item = {
								slug: '',
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
        console.log(intialItems);
    }
});
