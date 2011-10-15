App.views.Viewport = Ext.extend(Ext.Carousel, {
    fullscreen: true,
    initComponent: function() {
	     var intialItems = new Array();
		 var party = document.getElementById('party_id').value;
		 $.ajax({
            url: 'http://phoenix.dyn.cs.washington.edu:8000/party/' + party + '/',
            dataType: 'json',
            success: function(json) {
                items.push({
					slug: '',
					title: json['title'],
					artist: json['artist'],
					songid: json['song_id'],
					videoid: json['video_id']
				});
            }
        });
		$.ajax({
            url: 'http://phoenix.dyn.cs.washington.edu:8000/party/' + party + '/next',
            dataType: 'json',
            success: function(json) {
                items.push({
					slug: '',
					title: json['title'],
					artist: json['artist'],
					songid: json['song_id'],
					videoid: json['video_id']
				});
            }
        });
        Ext.apply(this, {

            defaults: {
                xtype: 'paintingcard',
            },

            items: [intialItems],
			listeners: {
            	beforecardswitch: function() {
					var me = this;
					$.ajax({
		                url: 'http://phoenix.dyn.cs.washington.edu:8000/party/' + party + '/next',
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
    }
});
