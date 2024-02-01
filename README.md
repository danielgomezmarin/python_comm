# python_comm
Connect pure data and python via OSC

Connecting pure data and python 3.x has been a great need for the generative music community. Here I show how I use OSC messages to send information back and forth.

Pure data has the convenience of in depth audio and midi programming, straightforward GUI implementation plus onboard audio and MIDI inter connectivity (with audio hardware and virtual and midi interfaces). While python is a powerful software with state of the art modules for machine learning and general programming. The "py" object available for pure data only works for Python 2.7 but, although it was a very nice solution, every day less computers come with Python 2.7 and less people are willing to deal with he hassle of having an old version of Python. 

This simple  solution, composed of a python script and a pd patch, allows to send and receive floats and lists via OSC messages disregarding the Python version it is communicating with it. Although not a full replacement for py (can't load automatically scripts, inherits the laggedness of network communication, etc.) it is a workaround if you need to run Python 3.x scripts to process information from pure data and send it back.
