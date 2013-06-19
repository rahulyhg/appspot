var menu_node = false; 
var data_dict = {};
function menu_select(){
	ndx=parseInt($(".menu_item_hover").attr("id").replace("id_item_",''));
	$("#id_menu2").hide();
	var info = $(menu_node).data("info");
	info.selected=ndx;
	$(menu_node).html(data_dict[info.text][ndx]);
	$(menu_node).click();
} 
function update_node(node) {
	var newnode = $("<span></span>");
	newnode.html(data_dict[node.data][0]);
	$(newnode).data("info", {text:node.data, selected:0});
	$(node).replaceWith(newnode);
}
$(document).ready(function() {
	$('.SriShell_div').keypress(function(e){
		if($("#id_menu2").is(":visible") && (e.keyCode == 10 || e.keyCode == 13)){
			e.preventDefault();
			menu_select();
		}
	});
	$('.SriShell_div').live('keyup', function(e) {
		$(".SriShell_div p").each(function(){
			$(this).after("<br>");
			$(this).replaceWith($(this).html());
		});
		if($("#id_menu2").is(":visible")){
			if(e.which==27) {
				$("#id_menu2").hide();
				$(menu_node).data("info", false);
				menu_node=false;
			}
			else if(e.which==40) {
				$(".menu_item_hover").next().addClass("menu_item_hover");
				$(".menu_item_hover:first").removeClass("menu_item_hover");
				if(!$(".menu_item_hover").length)
					$(".menu_item:first").addClass("menu_item_hover");
			}
			else if(e.which==38) {
				$(".menu_item_hover").prev().addClass("menu_item_hover");
				$(".menu_item_hover:last").removeClass("menu_item_hover");
				if(!$(".menu_item_hover").length)
					$(".menu_item:last").addClass("menu_item_hover");
			} else {
				$("#id_menu2").hide();
				$(menu_node).data("info", false);
			}
		}

		if(String.fromCharCode(e.which).match(/\w/))
			return;

		$(".SriShell_div span").each(function(){
			var info = $(this).data("info");
			if(info) {
				var word = data_dict[info.text][info.selected];
				var text = $(this).text();
				var ndx = text.indexOf(word);
				if (word == text) return;
				if (ndx == -1) { 
					if(text.match(/.*?[ -~].*/)) 
						$(this).replaceWith(text);
					return;
				}
				var newspan = $("<span>"+word+"</span>");
				if (ndx > 0) {
					$(this).before(text.substring(0, ndx));
					$(this).after(newspan);
				}
				if (ndx + word.length < text.length) {
					$(this).before(newspan);
					newspan.after(text.substring(ndx + word.length));
				}
				$(this).remove();
				newspan.data("info", info);
			}
		});

		if(e.which == 8) $(".SriShell_div span").filter(function(){
			var info = $(this).data("info");
			return info && data_dict[info.text][info.selected]!=$(this).text();
		}).each(function(){
			var info = $(this).data("info");
			var data=data_dict[info.text];
			$("#id_menu2").empty();
			$("#id_menu2").show();
			for(var i=0;i<data.length;i++){
				$("#id_menu2").append("<div class='menu_item' id='id_item_"+i+"'><div class='menu_item_in'>"+data[i]+"</div></div>");
			}
			var rec=this.getBoundingClientRect();
			$("#id_menu2").css('left', rec.left);
			$("#id_menu2").css('top', rec.top);
			menu_node=this;
			$(".menu_item").click(menu_select);
			$(".menu_item:first").addClass("menu_item_hover");
			$(".menu_item").hover(function(){
				$(".menu_item_hover").removeClass("menu_item_hover");
				$(this).addClass("menu_item_hover");
			});
		});
		
		for(var node = this.firstChild;node;node = node.nextSibling) if(node.nodeType==3) {
			var i=node.data.search(/\w/);
			var j=node.data.search(/\W/);
			if (Math.min(i,j) >= 0) {
				node.splitText(Math.max(i,j));
				if (i==0) {
					if (node.data in data_dict)
						update_node(node);
					else {
						var img = $("<img src='/static/srishell/loading.gif'>");
						$(node).after(img);
						(function (node, img){
							$.getJSON("/srishell/ajax_words/", {input: node.data}, function(data){
								img.remove();
								data.push(node.data);
								data_dict[node.data] = data;
								update_node(node);
							});
						})(node, img);
					}
				}
			}
		}
	});
});
