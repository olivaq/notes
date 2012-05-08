function getNotes(url, parent_id)
{
    var query = {url:url};
    
    if(parent_id != undefined)
        query.parent_id = parent_id;
    
    return $.ajax(getNoteServer(), {data:query, async:false}).responseText;
}

function postNote(url, note, reply_to)
{
    var data = {url:url, note:note};
    
    if(reply_to != undefined)
        data.reply_to = reply_to;
    
    $.post(getNoteServer(), data);
}
