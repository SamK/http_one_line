# http_one_line

This is a small webserver that displays a message of your choice.

You can use it as a maintenance page when you upgrade servers and must put them offline.
You can also use this program as a simple page website.

## Installation

### Prerequisites

* Python
* CherryPy version 3. Available on Debian and Ubuntu by installing the `python-cherrypy3` package

### Download

The latest stable release can be found here: https://github.com/SamK/http_one_line

### Installation

1. Type the following commands:

    python setup.py build
    sudo python setup.py install

2. Test that the program has been installed by typing `http_one_line --help`

### Compatibility

* Tested under Python version 2.7 

## Usage

Note that you might need to use sudo if the port is below 1024.

How to get some help:

    # http_one_line --help

Create a web server with a simple maintenance message:

    # echo 'This server is under maintenance. Please come back later.' | http_one_line --code 503

How to show your .bashrc file to the world:

    # http_one_line < ~/.bashrc 

* Exit the server by typing CTRL+C

## Contributing

* Submit bugs if you find some.
* Try to respect pep8 rules in pull requests
* Submit pull requests and I will happily merge them *when I have free time*.
Note that I must understand your code.

## Author

Samuel Krieg. My email is in the source code somewhere.

## License

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.

License addendum:
----
You are encouraged to send a nice email to the author.

