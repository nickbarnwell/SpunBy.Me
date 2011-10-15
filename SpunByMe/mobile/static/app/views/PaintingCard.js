App.views.PaintingCard = Ext.extend(Ext.Panel, {
    initComponent: function(){
        var pane = this,

        imageCard = {
            id:  'image_' + pane.slug,
            cls: 'painting ' + pane.slug,
        },

        infoCard = {
            id: 'info_' + pane.slug,
            cls: 'infocard',
            styleHtmlContent: true,
            tpl: [
                "<div>",
                "  <span>Did you like this song?: <a href=\"#\">yes</a> | <a href=\"#\">no</a></span>",
				'  <br />',
				'<fieldset class="search">',
				'<input type="text" class="box" id="q" name="q" value="Enter a Song or Artist" onclick="if(this.value == \'Enter a Song or Artist\') {this.value = \'\';}" onkeydown="this.style.color = \'#000000\';" />',
				'<button class="btn" title="Submit Search">Search</button>',
				'</fieldset><div id="queryresults"></div>',
				"</div>"
            ]
        },

        toggleButton = {
            text: 'Suggest a Song',
            handler: function() {
                if (this.getText() == 'Suggest a Song') {
                    pane.setActiveItem('info_' + pane.slug);
                    this.setText('Album Art');
                } else {
                    pane.setActiveItem('image_' + pane.slug);
                    this.setText('Suggest a Song');
                }
            }
        };

        Ext.apply(this, {

            layout: 'card',
            cardSwitchAnimation: 'flip',
            cls: 'paintingcard',

            items: [ imageCard, infoCard ],
            
            dockedItems: [
                {
                    xtype: 'toolbar',
                    title: '<img height="100%" style="vertical-align:middle; margin-right: 10px;" src="images/logo_onwhite.png" />' + pane.title + ' -  ' + pane.artist,
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
