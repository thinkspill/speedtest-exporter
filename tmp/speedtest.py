import subprocess
import json
import datetime
import time

def to_mb(bytes_per_sec):
    bits = bytes_per_sec * 8
    mbs = round(bits / (10 ** 6), 2)
    return str(mbs) + " MB/s"

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

def run():
  while True:
    current_dt = datetime.datetime.now()
    print(current_dt.strftime("%H:%M:%S - Starting speedtest"))
    cmd = ["speedtest", "--format=json-pretty", "--progress=no", "--accept-license", "--accept-gdpr"]
    output = subprocess.check_output(cmd)
    if is_json(output):
      data = json.loads(output)
      ping = int(float(data['ping']['latency']))
      download = to_mb(data['download']['bandwidth'])
      upload = to_mb(data['upload']['bandwidth'])
      print("Ping: " + str(ping))
      print("Download: " + download)
      print("Upload: " + upload)
      print('----------------------------------')
      time.sleep(60)

if __name__ == '__main__':
  run()