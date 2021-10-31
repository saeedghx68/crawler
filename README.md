Crawler
=============
A web crawler that, visits HTML pages within the same domain for a given url.

Web crawler will output a file (csv|xml) , and for each page a list of assets (e.g. CSS, Images, Javascripts) and links between pages.

Run
-----------
clone the project and run with docker

generate xml file:
```
docker build -t crawler .  && touch /tmp/out.xml && docker run --name python_crawler -v /tmp/out.xml:/tmp/out.xml crawler python crawler.py -u http://test.com -t xml -o /tmp/out.xml
```
generate csv file:
```
docker build -t crawler .  && touch /tmp/out.csv && docker run --name python_crawler -v /tmp/out.csv:/tmp/out.csv crawler python crawler.py -u http://test.com -t csv -o /tmp/out.csv
```

after this, the application will output the result in desired path with entered output type(xml/csv).

**notes:**
1) Output can be set csv or xml
2) You can set any urls
3) You can change the output file

-----------
## Test and Build

to run test or build application, we have make commands so :
to run tests:

**To test application**
```
make test
```
**note** please install python3.10 before run **make** command

**Run app**
```
make all
```
This command will install `python3-pip` and `virtualenv`
After that run create `virtualenv` and active and then install requirements package, finaly run this command.
`python crawler.py -u $(url) -t $(format) -o $(output)`
for example you have to run:
`make all output=/tmp/a.xml url=http://test.com/ format=xml` 


How it work
-----------
when the program start, it will create number async call and return data and save to a file.

Why asyncio ?
------------
Python finally has an excellent asynchronous framework, asyncio. Lets take a look at all the problems of threading and see if we have solved them.
1) **CPU Context switching:** asyncio is asynchronous and uses an event loop; it allows you to have application controlled context switches while waiting for I/O. No CPU switching found here!
2) **Race Conditions:** Because asyncio only runs a single coroutine at a time and switches only at points you define, your code is safe from race conditions.
3) **Dead-Locks/Live-Locks:** Since you don’t have to worry about race conditions, you don’t have to use locks at all. This makes you pretty safe from dead-locks. You could still get into a dead-lock situation if you require two coroutines to wake each other, but that is so rare you would almost have to try to make it happen.
4) **Resource Starvation:** Because coroutines are all run on a single thread, and dont require extra sockets or memory, it would be a lot harder to run out of resources. Asyncio however does have an “executor pool” which is essentially a thread pool. If you were to run too many things in an executor pool, you could still run out of resources. However, using too many executors is an anti-pattern, and not something you would probably do very often.

