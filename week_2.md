# Week 2

## Summary
The goals for this week: 
1. Getting comfortable with general Python concepts
2. Basic understanding of web APIs.
3. Retrieving data from lichess.com's web API

### Resources
* [Lichess API documentation](https://lichess.org/api#section/Introduction/Endpoint)

### Videos to watch:
* [Understanding Syntax](https://www.youtube.com/watch?v=Y69OtFzeY-Y)
* [44. Functions in Python](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412540#overview)
* [45. Arguments and Parameters](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15218270#overview)
* [46. Functions and return values in Python](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412544#overview)
* [47. Default parameter values](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15218272#overview)
* [10. Python Strings](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412510#overview)
* [11. Python String Formatting](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15218114#overview)
* [29. For Loops](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9413286#overview)

### Videos to Rewatch if Needed
* [16. Lists](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412520#overview)
* [37. List Slicing](https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412532#overview)
* [24. Joining Lists](https://www.udemy.com/course/)
  
### Concepts Learned
* Python syntax
* Formatting and style guides
* Python functions


## Python Syntax
Most programming languages are particular about how they are written. For example, the `C++` language would get upset if removed any character from the following program.

```cpp
int main() {
    int n, sum = 0;
}
```

This sort of extreme sensitivity has led to jokes such as:

> Programming is like writing a novel, except when your writing a novel the whole thing doesn't catch on fire if you leave at the semicolon on page 315.

Fortunately, Python isn't quite as irritating. It does away with superfluous characters like all those semicolons at the end of each line. Instead, if relies on indentation to understand what you are trying to do.

For example,
```python
if something == True:
    # Stuff here will happen only if it is `something` is true.

    if something_else == True:
        # Stuff here will only happen if `something` -and- `something_else` are true
    
    # Stuff here will happen only if it is `something` is true.

# Stuff here will happen regardless if `something` or `something_else` are true.
```

This indentation, combined with the keywords and special characters make up the Python syntax.

Here's a robust video on the matter (pro tip, we often watch videos on 2x speed):

* [Understanding Syntax](https://www.youtube.com/watch?v=Y69OtFzeY-Y)


## Style Guides
Often, the most noticeable difference between an senior program and a junior is their code style--or, lack thereof.  In programming, it is often pretty easy to get a program to do the one thing you need it to. However, building a program with thousands of tasks all building on each other requires discipline and skill to construct.  One of the ways professional programmers manage this complexity is through code styling.

Code styling is different than syntax. For example,

```python
def get_player_history(player_id: int)
    player_record = records[player_id]
    return player_record["history"]

def x(a):
    return records[x]["history"]
```
Both of these functions are the same, they retrieve a player's history after retrieving it from `records` using the `player_id`. However, the second would be extremely hard to debug. And the adage goes, "Programming is 15 minutes writing code and 5 hours debugging it."

Having code which is easy to read for your future self and others will pay continuous dividends. "Good styled" code can be somewhat objective, however, several organizations have put together style guides which are extremely common and are derived from legitimate rules.

Take for example,
```python
bio = "This is the string which never ends, it goes on and on and on and on and on and on and on and on and on and on and on and on and on..."
```
Above is a string being assigned to the variable `bio`. Most likely, you must scroll to the right to read the entire text.  This means you probably need to stop typing, switch to your mouse, and scroll over. All wasted effort. As such, most style guides suggest you keep strings like this to ~80 characters as this commonly fits on screen without scrolling right. And depending on the language, there are usually tricks for breaking it up.

For example, here's how one way to split it up in Python.

```python
bio = "This is the string which never ends," + \ 
"it goes on and on and on and on and on and on and " + \
"on and on and on and on and on and on and on..."
```

A few style guides to be aware of:
* [Pep 8](https://peps.python.org/pep-0008/) -- the old school Python style guide.
* [black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) -- the young kid on the block, but on the verge of exceeding `pep 8` in adoption.

For the rest of the course, I will be requesting you style all of your code in `black` format. "Wow, Thomas, that's a bit much for crash course, dude." Maybe. But it is best you start now--it will make you stand out among others applicants if it is habit for you.

Also, `black` has a companion tool which will automatically format your code! 🎉

### Installing Black
1. Open your `cmd` or `zsh` terminals.
2. Type `pip install black`.
3. Find a Python file (`.py`) you would like to format
4. Type `black /path/to/file`

Or, if you want to format all of your files in your project go to the project main directory and type `black *`.

> Note, `black` can only format projects which will run. If there are syntax issues (code won't run) then `black` will give you an error when formatting them.

## Functions
Let's go back to our Lichess code from last week.

```python
from rich import print
import requests

LICHESS_ID = "Cross_online"
LICHESS_API_PATH = "https://lichess.org/api/"
ENDPOINT = "users/status"

RESOURCE_PATH = f"{LICHESS_API_PATH}{ENDPOINT}"
REQUEST_URL = f"{RESOURCE_PATH}?ids={LICHESS_ID}"

result = requests.get(REQUEST_URL)
data = result.json()

first_user = data[0]
user_name = first_user["name"]
print(user_name)
```

Quick reminder, the `LICHESS_ID` is passed to the Lichess web API andpoint `users/status` and you get information back about the user's status. But this code isn't great. For example, what if you wanted to pull two user statuses? It would look something like this:

```python
from rich import print
import requests

LICHESS_ID = "Cross_online"
LICHESS_ID_2 = "Bob"

LICHESS_API_PATH = "https://lichess.org/api/"
ENDPOINT = "users/status"

RESOURCE_PATH = f"{LICHESS_API_PATH}{ENDPOINT}"
REQUEST_URL = f"{RESOURCE_PATH}?ids={LICHESS_ID}"
REQUEST_URL_2 = f"{RESOURCE_PATH}?ids={LICHESS_ID_2}"

result = requests.get(REQUEST_URL)
data = result.json()

result2 = requests.get(REQUEST_URL)
data2 = result2.json()

first_user = data[0]
user_name = first_user["name"]
print(user_name)

first_user2 = data2[0]
user_name2 = first_user2["name"]
print(user_name2)
```
As you can see, this script repeats almost every line for `bombegranate`. This means we wrote twice as much code, which wasted a lot of time and now is twice the area where a bug may appear. This is an extremely common problem in programming, so much we have a mnemonic for it: "Don't Repeat Yourself."  Or "DRY."  And the opposite of "DRY" code we call "WET." Or, "Write Everything Twice." Yeah, I know, programmers think they are funnier than they are.

Let's try to "DRY" the code up a bit. One of the easiest ways to make code more reusable, therefore DRY, is by using functions and classes. For now, let's focus on just functions and rewrite the above code using a function.

```python
from rich import print
import requests

LICHESS_ID = "Cross_online"
LICHESS_API_PATH = "https://lichess.org/api/"

def get_user(user_id):
    url = f"{LICHESS_API_PATH}users/status?ids={user_id}"
    data = requests.get(url)
    return data


result = get_user(LICHESS_ID)
data = result.json()

first_user = data[0]
user_name = first_user["name"]
print(user_name)

result2 = get_user("bombegranate")
print(list(result2))
```

Here we have added the `get_user()` function and it takes on argument, `user_id`. This cleans the code up a bit, but it is still WET. We need to address the duplicated lines such as `first_user = data[0]`, this should be the same for every user we retrieve.

The interesting thing to note is the user status endpoint in Lichess takes a list of player ids, such as `cross_online,bombegranate`. 

> Challenge #1: Rewrite the code above so the `get_user` function takes a list of user ids. E.g., `["cross_online", "bombegranate"]` and returns the data retrieved from Lichess. 

> Note, the data sent back is stored in an `object`, more on those later, but know you will need to convert this to a list like so, `list(data)`.


## Lichess SDK
One of the reasons Python is extremely popular is the amount of libraries out there. If you have something you want to get done, most likely, someone has already written a library for you. These libraries are key to allow someone from a different profession to quickly get something done, whether it is marine biology or astrophysics.

Chess is no different. There are currently [275](https://pypi.org/search/?q=chess) libraries listed for chess in Python. And probably many more unlisted.

Let's take Lichess again. There are several libraries for it, but let's work with the most popular.  By the way, "libraries" can also be called "packages," "modules," "SDK" (software development kit), or "framework."  And though all those terms have technical differences, many programmers use the terms interchangeably. Ok, let's on with it.

We are going to install Lichess' official SDK:
* [berserk](https://berserk.readthedocs.io/en/master/installation.html)

You can do so by opening a terminal and typing:
```sh
pip install berserk
```
And let's run this script:

```py
import berserk
from rich import print

USERNAME = "cross_online"

client = berserk.Client()

# Get realtime status
print(client.users.get_realtime_statuses(USERNAME))

# Get public adata
print(client.users.get_public_data(USERNAME))
```
Nice, right!? Very little effort on our part and we got a user's realtime status and all their public data. _This_ is the power of Python; the power to get stuff done.


## Homework Assignment
Using the `beserk` SDK do the following:

1. Using the `berserk` SDK do the following:
   1. Export a list of all of `cross_online`'s games
   2. Set the `max` argument to 200.
   3. Set the `evals` argument to `True`
   4. Set the `moves` argument to `True`
   5. Set the `openings` argument to `True`
2. The result object will need to be converted to a `list` (e.g., `list(result)`).
3. Loop through the list and print out the white player's user name, the black player's user name, and the `moves`  from each of the games in the list.
4. (Bonus) write the `moves` to a file.

* [berserk documentation](https://berserk.readthedocs.io/en/master/usage.html)
