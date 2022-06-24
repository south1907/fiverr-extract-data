function httpGetAsync(url, callback) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() { 
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
			var url_backend = 'http://localhost:8000'

			let data = {
				"data": xmlHttp.responseText
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

function requestData(url) {
	httpGetAsync(url, httpPostAsync)
}

requestData('https://www.fiverr.com/')