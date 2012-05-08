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

function getLocation()
{
    return window.location.href.split("#")[0];
}

function makeLinks(parent, id)
{
    var link = document.createElement('A');
    
    link.onclick = function(e){e.preventDefault();addReply(id);};
    
    link.innerHTML = "Add reply";
    link.href = "#";
    
    parent.appendChild(link);
}

function addReply(id)
{
    var note = prompt("Enter note")
    
    postNote(getLocation(), note, id)
}

function makePost()
{
    var note = prompt("Enter note")
    
    postNote(getLocation(), note);
}

function makeNote(json)
{
    var div = document.createElement('DIV');
    
    div.innerHTML = json.note;
    
    makeLinks(div, json.id);
    for(var i in json.replies)
        div.appendChild( makeNote(json.replies[i]) );
    
    return div;
}

//chrome.extension.sendRequest({update:window.location.href}, function(response)

function handleResponse(response)
{
    response = eval(response);
    
    for(var i in response)
    {
        document.body.appendChild( makeNote(response[i]) );
    }
}
