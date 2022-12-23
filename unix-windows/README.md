# MicroPython on Unix and Windows

From [MicroPython downloads](https://micropython.org/download/), one can choose from many different ports, features, vendors, and MCUs. However, if you want a micropython that runs on **Linux** or **Windows** PCs, you need to build one for yourself.

Under *windows*, there is a micropython.exe file that can be downloaded and used to run MicroPython on a Windows PC. 

There are two versions of MicroPython in the *unix* directory: one compiled with gcc-9.4.0 (unix/GCC940) and one compiled with gcc-11.3.0 (unix/GCC1130). 

The Windows version includes fewer features than the Unix version; for example, the Unix version includes *_threads* and *usocket* while the Windows version does not. Of course, *machine.Pin* and similar functions are not supported in these versions. 

There is also a "Linux raspberrypi 4.19.97-v7l+" version in the *raspberrypi* directory. 

These versions, however, support *worker* and *pipe* as *frozen modules*.
To use, simply import the module, for example,

```from worker import task, MT```
