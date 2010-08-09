/*
 * Hacker News Office Hours
 */

/* Compatibility with stupid browsers */
if(!Array.prototype.indexOf){Array.prototype.indexOf=function(elt){var len=this.length>>>0;var from=Number(arguments[1])||0;from=(from<0)?Math.ceil(from):Math.floor(from);if(from<0)from+=len;for(;from<len;from++){if(from in this&&this[from]===elt)return from}return-1}}

/*
 * To add more colors, add a CSS color name or hex to the array
 * Any place you have a list of tags that are supposed to be colored, make sure
 * they can be selected by "ul.skill > li"
 *
 * Colors are not consistent across pages. To do that, coloring would have to be
 * done by django
 *
 * An alternate way of doing this is to build a dict of what color for each tag
 * on the fly in the first loop. This avoids the potentially costly .indexOf
 *
 */
(function colorTags(){
  var colors = ['#46B423','#C465C3','BlueViolet','Brown','CadetBlue','Chocolate','CornflowerBlue','Crimson','DarkBlue',
    'DarkCyan','DarkGoldenRod','DarkGreen','DarkMagenta','DarkRed','DarkSlateBlue','DarkTurquoise','DarkViolet','DeepPink',];

  $(function(){
    var allTags = [];
    $('ul.skill > li')
      .each(function(){
        var tag = $.trim(this.innerHTML);
        if (allTags.indexOf(tag) === -1) allTags.push(tag);
      })
      .each(function(){
        var tag = $.trim(this.innerHTML);
        $(this).css('background-color',colors[allTags.indexOf(tag) % colors.length]);
      });
  });
})();


/*
 * Hook up availability buttons, 1st pass
 */
$(function(){
  var $availability = $('#nav > a.setAvailability');
  $availability.click(function(){
    var self = this;
    $.getJSON(this.href,function(data){
      if (data.status == "success") {
        $availability.removeClass('btn');
        $availability.eq(!data.availability).addClass('btn');
      }
    });
    return false;
  });
});