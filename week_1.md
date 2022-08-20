# Week 1

## Summary
The goals for this week: 
1. Getting comfortable with Python concepts
2. Retrieving data from lichess.com's web API


### Resources
* [Lichess API documentation](https://lichess.org/api#section/Introduction/Endpoint)

### Videos to watch:
* [JSON Crash Course](https://youtu.be/GpOO5iKzOmY)
* [21. Python dictionaries](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412524#overview)
* [235. Code for this section](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206672)
* [236. Signing up to OpenExchangeRates](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206674#overview)
* [237. Getting all exchange rates from the API](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206678#overview)

### Questions to Answer
> Quiz #1: What does the status code "200" mean?
> Quiz #2: When making an update to a resource what verb(s) should be used?


## Crash Course in Pull Chess Data
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

Here is a list of status codes:

* [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

> Quiz #1: What does the status code "200" mean?

### Web API Verbs
Programmers love to have a pattern when writing code. This helps us ensure the code is understandable as it grows. That is, if you write 50 lines of code and leave for a day, come back, it is not too hard to get your head back into. But if you have 10,000 lines of code across 20 files, if you don't have a pattern across all of the code then you don't have a mental model to understand the code. Each line must be understood one-by-one. This makes it exceed a cognitive complexity threshold. You may also hear developers talk about a project's "complexity budget."

Web API requests follow a well defined pattern. It has two major parts. The action one wants to take, followed by the resource one wants to take the action on.

In English we would say, "Jimmy got the ball."  With web APIs we would say, "Jonathan got the Wikipedia page on 'Web API's."  These sentences express complete thoughts.

Now, let's compare it to a web API request.
```
GET https://en.wikipedia.org/wiki/Web_API
```
Or going back to the Python code:
```python
result = requests.get("https://en.wikipedia.org/wiki/Web_API")
```

The `"https://en.wikipedia.org/wiki/Web_API"` is the resource and `get` is what we want do with it. Of course, there are many other words besides `get`. But each of them will be an action word, or, verb.  As such, we refer to these commands as the "HTTP verbs."

Here is a fairly complete list. Please read through all of them.

* [HTTP Verbs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

If you go back to inspecting the network traffic on Wikipedia, you can click on a request entry and see more details about the request, including the request method (aka, verb).

![request-method](media/request_method.png)

> Quiz #2: When making an update to a resource what verb(s) should be used?

### HTML and JSON
Now we know a bit about how we can make requests of a web API, but we haven't talked about the data which an API sends back. There are thousands of different data formats which can be used, but luckily, the internet has agreed on two which are ubiquitous, `HTML` and `JSON`.

#### HTML
You are probably aware of HTML, but as I mentioned, it is hyper-text markup language. It looks something like this:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Come-at-me-bro! Inc.</title>
</head>

<body>
    <main>
        <h1>Come-at-me-bro! Come-at-me-bro!</h1>
    </main>
    <footer class="footer">&copy; Come-at-me-bro! Inc.</footer>
</body>

</html>
```
The above HTML code is a complete website.

> Exercise: Copy the above code, save it on your Desktop as `index.html`, right click on the file and select "Open with Chrome / Firefox / Safari"

Notice how the web browser knows exactly what to do with the file? Web browsers have built in HTML interpreters. HTML and its partner CSS (cascading style sheets) are a huge topic by themselves. If you enjoy them, then you would probably enjoy a career in web site design (front-end engineer).

### JSON
"JSON" (pronounced "Jason") is not actually a coding language. It is a data format. Rather reexplaining what others have done a better job at, watch this video:

* [JSON Crash Course](https://youtu.be/GpOO5iKzOmY)

Before we move on, it is important to know Python converts JSON objects into Python dictionaries usually. However, this is not always the case.  Let's look at some JSON.

```json
[
    {
        "name": "cross_online", 
        "id": "cross_online"
    }
]
```

Above is the data sent back when requesting results from the Lichess.com web API resource:

* [GET: Masters Database](https://lichess.org/api#tag/Opening-Explorer/operation/openingExplorerMaster)

These data can then be transformed and sent elsewhere, such as a database.  Or used for visualization.