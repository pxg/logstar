/** Loop our requests and output them to the table */
function displayRequests(requests) {
    var table = document.getElementById('requests')
    for (var i=0, len=requests.length; i < len; i++) {
        displayRequest(table, requests[i]);
    }
}


/** Display a request as a row in the table */
function displayRequest(table, request) {
    var row = table.insertRow();
    addCell(row, truncate(request['url']), '/request/' + request['id'] + '/');
    addCell(row, request['time']);
    addCell(row, request['method']);
    addCell(row, request['response_status_code']);
    addCell(row, request['created_at']);
}


/** Add a cell to the row */
function addCell(row, content, url=false) {
    var cell  = row.insertCell();
    if(url != false) {
        content = '<a href="' + url + '">' + content + '</a>';
    }
    cell.innerHTML = content
}


/** Truncate a string if it's over a set length */
function truncate(string, length=80) {
    if(string.length >= length) {
        return string.substring(0, length) + '...';
    }
    return string;
}


fetch('/api/', {
    method: 'get'
}).then(function(response) {
    return response.json();
}).then(function(json) {
    displayRequests(json);
});
