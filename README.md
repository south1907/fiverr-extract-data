# Fiverr Extract Data (Crawl data Fiverr)
Tool extract data from Fiverr use super way (Console)

## How to extract data from Fiverr
Fiverr is a big website of Works, Fiverr connects businesses with freelancers offering digital services in 500+ categories. Data of website have a big value, but crawl Fiverr is not easy

I try to some ways:
- Use Requests

<img width="1214" alt="image" src="https://user-images.githubusercontent.com/24355759/175592650-f00a6bfd-5a23-4f52-8db1-3578942ec8ce.png">

- Use Selenium: Website can detect it is not human

...

but not successful!

And I really can request API in Console of Website

```
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    	console.log(xhttp.responseText)
    }
};
xhttp.open("GET", 'https://www.fiverr.com/', true);
xhttp.send();

```

<img width="1047" alt="image" src="https://user-images.githubusercontent.com/24355759/175604315-dd6097d8-332f-4d98-ad66-b8031266a34f.png">

So, do it :V
