    App.views.PaintingCard = Ext.extend(Ext.Panel, {
    initComponent: function(){
        var pane = this,
        
        imageCard = {
            id:  'image_' + pane.slug,
            cls: 'painting ' + pane.slug,
            html: '<img height="100%" src="' + pane.albumart + '" />'
        },

        infoCard = {
            id: 'info_' + pane.slug,
            cls: 'infocard',
            styleHtmlContent: true,
            tpl: [
                "<div>",
                "  <span class=\"voting\">Did you like this song?: <a class=\"vote_yes\">yes</a> | <a class=\"vote_no\">no</a></span>",
				'  <br />',
				'<fieldset class="search">',
				'<input type="text" class="box q" name="q" value="Enter a Song or Artist" onclick="if(this.value == \'Enter a Song or Artist\') {this.value = \'\';}" onkeydown="this.style.color = \'#000000\';" />',
				'<button class="btn" title="Submit Search">Search</button>',
				'</fieldset><div class="queryresults"></div>',
				"</div>"
            ]
        },

        toggleButton = {
            text: 'Suggest a Song',
            handler: function() {
                if (this.getText() == 'Suggest a Song') {
                    pane.setActiveItem('info_' + pane.slug);
                    this.setText('Album Art');
                    var party = $("#party_id").val();
                    $(".vote_yes").unbind('click');
                    $(".vote_yes").bind('click', function(e) {
                        $(this).parent().fadeOut(function(){
                            var me = this;
                            $.ajax({
                                url:'/vote/?party_id=' + party + '&song_id=' + pane.songid + '&type=up',
                                dataType: 'json',
                                success: function(json) {
                                  $(me).html("This has " + json.votes + " Votes");
                                  $(me).fadeIn();
                                }
                            });
                        });
                    });
                    $(".vote_no").unbind('click');
                    $(".vote_no").bind('click', function(e) {
                        $(this).parent().fadeOut(function(){
                            var me = this;
                            $.ajax({
                                url:'/vote/?party_id=' + party + '&song_id=' + pane.songid + '&type=down',
                                dataType: 'json',
                                success: function(json) {
                                  $(me).html("This has " + json.votes + " Votes");
                                  $(me).fadeIn();
                                }
                            });
                        });
                    });
                    $('.q').unbind('keypress');
                    $('.q').bind('keypress', function(e) {
                        var me = this;
                        if(e.keyCode==13){
                            $.ajax({
                            url: '/search/?q=' + $(me).val() + '/',
                            dataType: 'json',
                            success: function(json) {
                                var html = '<ul>';
                                for (var song in json){
                                    if (json.hasOwnProperty(song)) {
                                        song = json[song];
                                        html += '<li><a href="/party/' + party + '/add_song?artist=' + song['artist'] + '&amp;title=' + song['title']
                                        + '">' + song['title'] + ' - ' + song['artist'] + '</a></li>';
                                    }
                                }
                                $(me).parent().parent().children(".queryresults").html(html + '</ul>');
                            }
                        });
                        }
                    });
                    $(".search .btn").unbind('click');
                    $('.search .btn').bind('click', function(e) {
                        var me = this;
                        $.ajax({
                            url: '/search/?q=' + $(me).parent().children(".box").val() + '/',
                            dataType: 'json',
                            success: function(json) {
                                var html = '<ul>';
                                for (var song in json){
                                    if (json.hasOwnProperty(song)) {
                                        song = json[song];
                                        html += '<li><a href="/party/' + party + '/add_song?artist=' + song['artist'] + '&amp;title=' + song['title']
                                        + '">' + song['title'] + ' - ' + song['artist'] + '</a></li>';
                                    }
                                }
                                $(me).parent().parent().children(".queryresults").html(html + '</ul>');
                            }
                        });
                    });
                } else {
                    pane.setActiveItem('image_' + pane.slug);
                    this.setText('Suggest a Song');
                }
            }
        };
        console.log(pane.albumart);
         // $("#image_" + pane.slug).attr("style", "background-image: url(" + pane.albumart + ");");

        Ext.apply(this, {

            layout: 'card',
            cardSwitchAnimation: 'flip',
            cls: 'paintingcard',

            items: [ imageCard, infoCard ],
            
            dockedItems: [
                {
                    xtype: 'toolbar',
                    title: '<img height="100%" style="vertical-align:middle; margin-right: 10px;" src="http://www.spunby.me/static/logo/logo_onwhite.png" />' + pane.title + ' -  ' + pane.artist,
                    items: [{ xtype: 'spacer' }, toggleButton ]
                }
            ],

            listeners: {
                beforecardswitch: function() {
                    var infoPanel = this.getComponent('info_' + pane.slug);
                    infoPanel.update(pane);
                }
            }
        });

        App.views.PaintingCard.superclass.initComponent.call(this);
    }
});

Ext.reg('paintingcard', App.views.PaintingCard);
