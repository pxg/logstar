/** Loop our requests and output them to the table */
function displayRequests(requests, top=true) {
    if(top == true){
        requests.reverse();
    }
    for (var i=0; i < requests.length; i++) {
        displayRequest(requests[i], top);
    }
}


/** Display a request as a row in the table */
function displayRequest(request, top) {
    var table = document.getElementById('requests')
    if(top == true){
        // insert after header
        row = 1;
    }else{
        // Insert at bottom
        row = table.rows.length;
    }
    var row = table.insertRow(row);
    addCell(row, truncate(request['url']), '/request/' + request['id'] + '/');
    addCell(row, request['time']);
    addCell(row, request['method']);
    addCell(row, getStatusCodeDisplay(request['response_status_code']));
    addCell(row, request['created_at']);
}

/** Get the emoji to display with the status code **/
function getStatusCodeDisplay(statusCode) {
    var statusFirstDigit = statusCode.toString()[0];
    if(statusFirstDigit == 4){
        return statusCode + ' 😢';
    }
    if(statusFirstDigit == 5){
        return statusCode + ' 😡';
    }
    return statusCode + ' 😀';
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


function pollApi() {
    var url = '/api/';
    if(aboveId != false) {
        url += 'above/' + aboveId + '/'
    }
    fetch(url, {
        method: 'get'
    }).then(function(response) {
        return response.json();
    }).then(function(json) {
        if(json.length > 0){
            aboveId = json[0]['id'];
            // Set intial below ID value
            if(belowId === false) {
                belowId = json[json.length - 1]['id'];
            }
        }
        displayRequests(json);
    });
}


function loadMoreApi() {
    var url = '/api/';
    url += 'below/' + belowId + '/'
    fetch(url, {
        method: 'get'
    }).then(function(response) {
        return response.json();
    }).then(function(json) {
        if(json.length > 0){
            belowId = json[json.length - 1]['id'];
        }
        displayRequests(json, false);
    });
}

// Nasty globals find better polling technique
var aboveId = false;
var belowId = false;

pollApi();
setInterval(function() { pollApi(); }, 5000);

var loadMoreButton = document.getElementById("more");
loadMoreButton.onclick = loadMoreApi;
