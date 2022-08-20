# Week 1
One of the most common tasks done in programming is retrieving data from a [web API](https://en.wikipedia.org/wiki/Web_API). "API" stands for application programming interface. It is a way for two computer systems to interact without a user interface being involved. 

> It is important to note "API" also refers to many other things, so you have to derive from context whether it is an *web* API.

For data people, web APIs are often a source of data. We are usually asked to take these data from a different web APIs and programmatically move it somewhere else. When talking about web APIs there are there are several base concepts we need to understand.

## HTTP / HTTPS
HTTP and HTTPS stand for "hyper-text transfer protocol" and "hyper-text transfer protocol secure." They are primarily how systems throughout the internet talk to one another. When open a webpage it is using this transfer protocol to retrieve HTML (hyper text markup language) and JavaScript code to your local computer, where it is run within your browser.

In Chrome, open the https://en.wikipedia.org/wiki/Web_API from earlier. Now, right click anywhere and select "Inspect." Then click on the "Network" section of the development tools. Lastly, refresh the page.

![web-api](media/web_api_call.png)

Each one of the entries in the network section with the "Initiator" of "Web API" is your browser asking for data from the Wikipedia website via the web API.

One more note, all traffic should be going through HTTPS now. This ensures any data sent between your computer and where you are going on the internet is encrypted so no one between can understand it.

### HTTP Request Codes
In the world of tech there is a standard for everything. It allows programmers to build applications which work together with some level of confidence. HTTP and HTTPS are no exceptions.  

One of the neat things about these protocols is they have status codes which tell you the status of a request you made of another system.

Dropping fancy talk, let's say your Python code makes a request for the Web API article on Wikipedia. 

```python
import requests

result = requests.get("https://en.wikipedia.org/wiki/Web_API")
print(result.status_code)
```
This code will print out the status code for retrieving the webpage.

![web-request-result](media/status_code.png)