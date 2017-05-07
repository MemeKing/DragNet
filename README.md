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
$ apt-get install python
$ apt-get install python-pip
$ apt-get install nmap
$ pip install python-nmap
```

#### Windows setup
Install everything according to their individual instructions.

#### Questions
>Is this legal?

i dunno lol. This script doesn't try to compromise anything but the legality and morality of port scanning is still an ongoing debate. Take a look at [Nmap's official article on the subject](https://nmap.org/book/legal-issues.html) for more information.

>Why is this taking so long to run?

The speed of this script is random. You might get a hit right away or it might take several minutes.

![glorious nmap](http://nmap.org/images/nmap-logo-256x256.png)