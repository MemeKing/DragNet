## Drag Net
This python script will find random web servers on the internet. It isn't a penetration testing tool, it's just meant to be interesting and maybe helpful if you're doing research.

### Usage
Run this script from the command line. It will display results in the console.
Scan() can be used standalone. It will return one random live IP that's running whatever port you give it.

### Installation
The following stuff is needing for this to work:
* [Python 2.x](https://www.python.org/)
* [Nmap Secrurity Scanner](https://nmap.org/)
* [python-nmap](https://bitbucket.org/xael/python-nmap)

#### Linux setup
```sh
$ apt-get install python nmap python-pip
$ pip install python-nmap
$ git clone https://github.com/MemeKing/DragNet
```

#### Windows setup
1. Download and extract the repo. 
2. Run the following in the command prompt.
```cmd
> python -m pip install python-nmap
``` 

#### Questions
>Is this legal?

i dunno lol. This script doesn't try to compromise anything but the legality and morality of port scanning is still an ongoing debate. Take a look at [Nmap's official article on the subject](https://nmap.org/book/legal-issues.html) for more information.

>Why is this taking so long to run?

The speed of this script is random. You might get a hit right away or it might take several minutes.

>Why are all my results going to "Invalid URL" and "404 not found" pages? I thought this only returned live servers?

Most of your results will be duds like this because the script can't tell the difference between a live IP with something actually behind it and a live IP that just responds. Sites like this usually still have something on them, but I'll leave the exploring to you.
![glorious nmap](http://nmap.org/images/nmap-logo-256x256.png) 