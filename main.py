import time
import os

import requests
from threading import Timer

class TenvisTH661:

  def __init__(self, ip, username, password):
    self.ip = ip
    self.username = username
    self.password = password

  def pan_left(self, time=1.0):
    return self.move('left', time)

  def pan_right(self, time=1.0):
    return self.move('right', time)

  def tilt_up(self, time=1.0):
    return self.move('up', time)

  def tilt_down(self, time=1.0):
    return self.move('down', time)

  def move(self, dir, time=1.0):
    r = self.request_for(dir)
    if r.status_code == 200:
      Timer(time, self.stop).start()
    return True

  def stop(self):
    r = self.request_for('stop')
    return r

  def still(self, path=None):
    if path == None:
      timestr = time.strftime("%Y%m%d-%H%M%S")
      path = f"{timestr}.jpg"

    r = requests.get(f"http://{self.username}:{self.password}@{self.ip}/tmpfs/auto.jpg", stream=True)
    if r.status_code == 200:
      with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
          f.write(chunk)

  def request_for(self, action):
    return requests.get(self.url_for(action))

  def url_for(self, action):
    url = f"http://{self.username}:{self.password}@{self.ip}/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act={action}"
    print(url)
    return url

if __name__ == '__main__':
  ip = os.environ.get('IPCAM_IP')
  usn = os.environ.get('IPCAM_USN')
  pwd = os.environ.get('IPCAM_PWD')
  if ip == None or usn == None or pwd == None:
    print('All of the variables IPCAM_IP, IPCAM_USN and IPCAM_PWD are required.')
    exit(1)
  ipcam = TenvisTH661(ip, usn, pwd)
  ipcam.tilt_down(2.0)
  ipcam.still()
