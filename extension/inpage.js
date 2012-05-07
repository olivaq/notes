/*function()
{*/
/*
	var lolid = 'loliololodl';
	
	chrome.extension.sendRequest({update:window.location.href}, function(response)
	{
		var div = document.createElement('DIV');
		div.className = 'update';
		div.innerHTML = response;
		
		document.getElementById(lolid).appendChild(div);
	});

	function initmynotes()
	{
		var div = document.createElement('DIV');
		div.id = lolid;
		div.style.position = "fixed";
		div.style.right = "10px";
		div.style.top = "10px";
		div.innerHTML = "<h1 style=\"float:left;-webkit-transform-origin:100%;-webkit-transform:rotate(-90deg);\">Notes</h1>";
		document.body.appendChild(div);
	}
	
	initmynotes();*/
//}();

chrome.extension.sendRequest({update:window.location.href}, function(response)
{
	var div = document.createElement('DIV');
	div.className = 'update';
	div.innerHTML = response;
	
	document.getElementById(lolid).appendChild(div);
});

var l = document.createElement('iframe');
l.style.position = "fixed";
l.style.right = "10px";
l.style.top = "10px";
l.src = 'http://localhost:8080/webpage/' + window.location.href;
l.style.border = 'none';
document.body.appendChild(l);
