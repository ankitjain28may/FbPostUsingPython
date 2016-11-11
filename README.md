# FbPostUsingPython
>It is a small script to post status on your FB wall using python..!

#Installation
1- Install python 3.5 from [Python.org](https://www.python.org)

2- `sudo apt-get install python3-pip` (For Ubuntu Users)

3- `python setup.py` or `python3 setup.py`

  This will install all these packages

  * `pip install bs4`

  * `pip install selenium`

After the installation, open terminal at the root folder--

Run `python fb.py` or `python3 fb.py` to post status from terminal or cmd.

Note:- Use Mozilla Firefox V40.0 to make this script work for you.

##Some Useful Installation Tips ( Ubuntu )

If you have already installed python 2.7 install python 3 as well but it may be the problem that the packages installed with respect to python 2.7 and shows error for the python 3 packages,

So you need to install virtual Environment for the python 3 to install python3 packages.

```
    virtualenv -p /usr/bin/python3 py3env
    source py3env/bin/activate
    pip install package-name
```

After setting virtual environment install packages listed above and Enjoy.

#License

Copyright (c) 2016 Ankit Jain - Released under the Apache License

P.S For more python scripts Go To -> [pythonResources](https://github.com/ankitjain28may/pythonResources)
