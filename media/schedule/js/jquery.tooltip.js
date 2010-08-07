(function($){

	$.fn.tooltip = function(instanceSettings){
		
		$.fn.tooltip.defaultsSettings = {
			attributeName:'title',
			borderColor:'#ccc',
			borderSize:'1',
			cancelClick:0,
			followMouse:1,
			height:'auto',
			hoverIntent:{sensitivity:7,interval:100,timeout:0},
			loader:0,
			loaderHeight:0,
			loaderImagePath:'',
			loaderWidth:0,
			positionTop: 12,
			positionLeft: 12,
			width:'auto',
			titleAttributeContent:'',
			tooltipBGColor:'#fff',
			tooltipBGImage:'none', // http path
			tooltipHTTPType:'get',
			tooltipPadding:10,
			tooltipSource:'attribute', //inline, ajax, iframe, attribute
			tooltipSourceID:'',
			tooltipSourceURL:'',
			tooltipID:'tooltip'
		};
		
		//s = settings
		var s = $.extend({}, $.fn.tooltip.defaultsSettings , instanceSettings || {});
		
		var positionTooltip = function(e){
			
			var posx = 0;
			var posy = 0;
			if (!e) var e = window.event;
			if (e.pageX || e.pageY) 	{
				posx = e.pageX;
				posy = e.pageY;
			}
			else if (e.clientX || e.clientY) 	{
				posx = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
				posy = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
			}
			
			var p = {
				x: posx + s.positionLeft, 
				y: posy + s.positionTop,
				w: $('#'+s.tooltipID).width(), 
				h: $('#'+s.tooltipID).height()
			}
			
			var v = {
				x: $(window).scrollLeft(),
				y: $(window).scrollTop(),
				w: $(window).width() - 20,
				h: $(window).height() - 20
			};
				
			//don't go off screen
			if(p.y + p.h > v.y + v.h && p.x + p.w > v.x + v.w){
				p.x = (p.x - p.w) - 45;
				p.y = (p.y - p.h) - 45;
			}else if(p.x + p.w > v.x + v.w){
				p.x = p.x - (((p.x+p.w)-(v.x+v.w)) + 20);
			}else if(p.y + p.h > v.y + v.h){
				p.y = p.y - (((p.y+p.h)-(v.y+v.h)) + 20);
			}
			
			$('#'+s.tooltipID).css({'left':p.x + 'px','top':p.y + 'px'});
		}
		
		var showTooltip = function(){
			$('#tooltipLoader').remove();
			$('#'+s.tooltipID+' #tooltipContent').show();
			
			if($.browser.version == '6.0'){//IE6 only
				$('#'+s.tooltipID).append('<iframe id="tooltipIE6FixIframe" style="width:'+($('#'+s.tooltipID).width()+parseFloat(s.borderSize)+parseFloat(s.borderSize)+20)+'px;height:'+($('#'+s.tooltipID).height()+parseFloat(s.borderSize)+parseFloat(s.borderSize)+20)+'px;position:absolute;top:-'+s.borderSize+'px;left:-'+s.borderSize+'px;filter:alpha(opacity=0);"src="blank.html"></iframe>');
			};
		}
		
		var hideTooltip = function(valueOfThis){
			$('#'+s.tooltipID).fadeOut('fast').trigger("unload").remove();
			if($(valueOfThis).filter('[title]')){
				$(valueOfThis).attr('title',s.titleAttributeContent);
			}
		}
		
		var urlQueryToObject = function(s){
			  var query = {};
			  s.replace(/b([^&=]*)=([^&=]*)b/g, function (m, a, d) {
				if (typeof query[a] != 'undefined') {
				  query[a] += ',' + d;
				} else {
				  query[a] = d;
				}
			  });
			  return query;
		};
		
		return this.each(function(index){
			
			if(s.cancelClick){
				$(this).bind("click", function(){return false});
			}
			
			if($.fn.hoverIntent){
				$(this).hoverIntent({
					sensitivity:s.hoverIntent.sensitivity,
					interval:s.hoverIntent.interval,
					over:on,
					timeout:s.hoverIntent.timeout,
					out:off
				});
			}else{
				$(this).hover(on,off);
			}
					  
			function on(e){	
		
				$('body').append('<div id="'+s.tooltipID+'" style="background-repeat:no-repeat;background-image:url('+s.tooltipBGImage+');padding:'+s.tooltipPadding+'px;display:none;height:'+s.height+';width:'+s.width+';background-color:'+s.tooltipBGColor+';border:'+s.borderSize+'px solid '+s.borderColor+'; position:absolute;z-index:100000000000;"><div id="tooltipContent" style="display:none;"></div></div>');
				
				var $tt = $('#'+s.tooltipID);
				var $ttContent = $('#'+s.tooltipID+' #tooltipContent');
				
				if(s.loader && s.loaderImagePath != ''){
					$tt.append('<div id="tooltipLoader" style="width:'+s.loaderWidth+'px;height:'+s.loaderHeight+'px;"><img src="'+s.loaderImagePath+'" /></div>');	
				}
				
				if($(this).attr('title')){
					s.titleAttributeContent = $(this).attr('title');
					$(this).attr('title','');
				}
				
				if($(this).is('input')){
					$(this).focus(function(){ hideTooltip(this); });
				}
				
				e.preventDefault();//stop
				positionTooltip(e);
				
				$tt.show();
				
				//get values from element clicked, or assume its passed as an option
				s.tooltipSourceID = $(this).attr('href') || s.tooltipSourceID;
				s.tooltipSourceURL = $(this).attr('href') || s.tooltipSourceURL;
				
				switch(s.tooltipSource){
					case 'attribute':/*/////////////////////////////// attribute //////////////////////////////////////////*/
						$ttContent.text(s.titleAttributeContent);
						showTooltip();
					break;
					case 'inline':/*/////////////////////////////// inline //////////////////////////////////////////*/
						$ttContent.html($(s.tooltipSourceID).children());
						$tt.unload(function(){// move elements back when you're finished
							$(s.tooltipSourceID).html($ttContent.children());				
						});
						showTooltip();
					break;
					case 'ajax':/*/////////////////////////////// ajax //////////////////////////////////////////*/	
						if(s.tooltipHTTPType == 'post'){
							var urlOnly, urlQueryObject;
							if(s.tooltipSourceURL.indexOf("?") !== -1){//has a query string
								urlOnly = s.windowSourceURL.substr(0, s.windowSourceURL.indexOf("?"));
								urlQueryObject = urlQueryToObject(s.tooltipSourceURL);
							}else{
								urlOnly = s.tooltipSourceURL;
								urlQueryObject = {};
							}
							$ttContent.load(urlOnly,urlQueryObject,function(){
								showTooltip();
							});
						}else{
							if(s.tooltipSourceURL.indexOf("?") == -1){ //no query string, so add one
								s.tooltipSourceURL += '?';
							}
							$ttContent.load(
								s.tooltipSourceURL + '&random=' + (new Date().getTime()),function(){
								showTooltip();
							});
						}
					break;
				};
				
				return false;
				
			};
			
			
			function off(e){
				hideTooltip(this);
				return false;
			};
			
			if(s.followMouse){
				$(this).bind("mousemove", function(e){
					positionTooltip(e);
					return false;
				});
			}
			
		});
	};
	
})(jQuery);
