var url_backend = 'http://localhost:8000'
var domain = 'https://www.fiverr.com'
var mainCategory = 'programming-tech'
var category = 'chatbots'

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function httpGetOneUrlDetail() {

	let res = await axios.get(url_backend + '/detail')
	console.log(res.data)
	let data = res.data;
	if (data['id']) {
		await httpGetDetail(data['id'], data['url'])
	} else {
		console.log('No need update detail')
	}
}

async function httpGetDetail(id, url) {

	let res = await axios.get(url)
	let data = {
		"data": res.data,
		"id": id
	};
	let dataStr = JSON.stringify(data);

	let resUpdate = await axios.post(url_backend + '/update-detail', dataStr)
	console.log(resUpdate.data)
}

async function requestDataDetail(num) {
	for (let i = 0; i < num; i++) {
		console.log(i)
		await httpGetOneUrlDetail();
	}
}