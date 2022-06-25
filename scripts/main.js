var url_backend = 'http://localhost:8000'
var domain = 'https://www.fiverr.com'
var mainCategory = 'programming-tech'
var category = 'chatbots'

function httpGetAsync(url, category, page, callback) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() { 
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			let data = {
				"data": xmlHttp.responseText,
				"category": category,
				"page": page
			};
			let dataStr = JSON.stringify(data);

			callback(url_backend, dataStr, console.log);
		}
	}
	xmlHttp.open("GET", url, true);
	xmlHttp.send();
}

function httpPostAsync(url, data, callback) {
	let xhr = new XMLHttpRequest();
	xhr.open("POST", url);

	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");

	xhr.onload = () => {
		callback(xhr.responseText);
	}

	xhr.send(data);
}

function requestData(url, category, page) {
	httpGetAsync(url, category, page, httpPostAsync)
}


for (let i = 1; i < 21; i++) {
	var url = domain + '/categories/' + mainCategory + '/' + category + '?page=' + i
	requestData(url, mainCategory + '/' + category, i)
}