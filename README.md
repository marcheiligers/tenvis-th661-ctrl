# tenvis-th661-ctrl

Tenvis TH661 Control lib in Python. I'm writing this in the hope that I'll be able to control this IP camera from [Home Assistant](http://home-assistant.io/). Nope, I'm not a Python developer.

## Usage

``` python
ipcam = TenvisTH661(ip, usn, pwd)
ipcam.tilt_down(2.0)
ipcam.still()
```

## Available methods

- `tilt_up(seconds=1.0)`
- `tilt_down(seconds=1.0)`
- `pan_left(seconds=1.0)`
- `pan_right(seconds=1.0)`
- `still(filename=None) # filename will default to a timestamp`
