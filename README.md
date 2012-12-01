AWSLI
====================

**Amazon Web Services Line Interpreter**

**Author:** Val Neekman [ info@neekware.com, @vneekman ]


Credit
=======
**Contributor(s):** 
    1. Sam Odivwri [sam.ese.odivwri@gmail.com]


Overview
========

A Line Interpreter for Amazon Web Services with tab completion.


How to install
==================
    Dependancies:
    1. $ sudo apt-get install mono-runtime (or equivalent on your distro.)
    
    1. easy_install python-awsli
    2. pip install python-awsli
    3. git clone http://github.com/un33k/python-awsli
        a. cd python-awsli
        b. run python setup.py
    4. wget https://github.com/un33k/python-awsli/zipball/master
        a. unzip the downloaded file
        b. cd into python-awsli-* directory
        c. run python setup.py

How to use
=================

``Usage:``

run cli.py

Welcome to AWSLI console!

`(cli)` help [tab]

>exit                 help                 node_list
>security_group_list  zone_list   

`(cli)` ? [tab]

>exit                help                node_list

`(cli)` help node[tab]_list

Usage: node_list.py [options]

Options:

  -h, --help            show this help message and exit
  
  -k KEY, --key=KEY     amazon web services access key id. aka:
  
                        aws_access_key_id
                        
  -s SECRET, --secret=SECRET
  
                        amazon web services secret access key. aka:
                        
                        aws_secret_access_key
                        
  -j, --json            print output as json when possible
  
  -r, --raw             print output raw - as is
  
`(cli)` 

``Note:``


Running the tests
=================

To run the tests against the current environment:

    python test.py

Changelog
=========

0.1
-----

* Initial release


License
=======

Copyright (c) 2012, Val Neekman

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



