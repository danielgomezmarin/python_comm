# python_comm
Connect pure data and python via OSC

Connecting pure data and python 3.x has been a great need for the generative music community. Here I show how I use OSC messages to send information back and forth.

Pure data has the convenience of in depth audio and midi programming, straightforward GUI implementation plus onboard audio and MIDI inter connectivity (with audio and midi hardware and virtual  interfaces), while python is a powerful software with state of the art modules for machine learning and general programming. The "py" object available for pure data only works for Python 2.7 but, although it was a very nice solution, every day less computers come with Python 2.7 and less people are willing to deal with he hassle of installing an old version of Python. 

This simple  solution, composed of a python script and two pd patches (an abstraction and a help patch), allows to send and receive floats and lists via OSC messages disregarding the Python version it is communicating with it. Although not a full replacement for py (can't automatically load scripts, inherits the laggedness of network communication, etc.) it is a workaround if you need to run Python 3.x scripts to process information from pure data and send it back.
