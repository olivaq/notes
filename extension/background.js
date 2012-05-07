url = 'http://localhost:8080/webpage/'
/*
chrome.extension.onRequest.addListener(
function(request, sender, sendResponse) {
	if("update" in request)
	{
		$.get(url + request.update, sendResponse);
	}

});
*/
function injectPageScript(tabid, info)
{
	chrome.tabs.get(tabid, function(tab)
	{
			if(info.status == 'loading')
			{
				chrome.tabs.executeScript(tabid, {'file':'inpage.js'});
			}
		});
}
chrome.tabs.onUpdated.addListener(injectPageScript)

