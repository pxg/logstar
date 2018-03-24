function displayRequests(requests){
    var table = document.getElementById('requests')
    // TODO: check JS coding conventions for line below http://crockford.com/javascript/code.html
    for (var i = 0, len = requests.length; i < len; i++) {
        displayRequest(table, requests[i]);
    }
}


// TODO: test with a 404 in the database
function displayRequest(table, request){
    var row = table.insertRow();
    // TODO: add hyperlink to page with details for request
    addCell(row, request['url']);
    addCell(row, request['response_status_code']);
    addCell(row, request['method']);
    addCell(row, request['time']);
    addCell(row, request['created_at']);
}


function addCell(row, data){
    var cell  = row.insertCell();
    var text  = document.createTextNode(data);
    cell.appendChild(text);
}


fetch('/api/', {
    method: 'get'
}).then(function(response) {
    return response.json();
}).then(function(j) {
    displayRequests(j);
});
