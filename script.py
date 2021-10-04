import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pandas as pd

# subfunction to check of file at url exists
def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok


# enter date and time of first and last images to download. must be in format: YYYY/mm/dd/HHMM
first = '2021/10/02/1200'
last = '2021/10/02/1230'

# create list of date and time strings between first and last image (images taken every 10min)
dates = pd.Series(pd.date_range(start=first, end=last, freq="10min"))
datestrings = dates.dt.strftime('%Y/%m/%d/%H%M')

# stuff to make it retry if connection times out. foto-webcam.eu will refuse the connection
# eventually if many images are downloaded or script is run too often.

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# download all images in list.
for d in datestrings:
    url = "https://www.foto-webcam.eu/webcam/simonyhuette/"+d+"_hu.jpg"
    img_name = url[-22:].replace('/', '_')
    if exists(url):
        img_data = requests.get(url).content
        with open(img_name, 'wb') as handler:
            handler.write(img_data)


