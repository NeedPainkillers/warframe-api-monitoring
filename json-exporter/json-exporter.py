import requests
import time

if __name__ == '__main__':
  link = "https://api.warframestat.us/pc"
  f = requests.get(link)
  log = open("logs/wf.log", "w")
  log.write(f.text)
  log.close()

  while True: time.sleep(600)