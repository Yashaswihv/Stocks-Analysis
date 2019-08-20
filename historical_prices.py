
import urllib.request.urlopen
import os
print(os.getcwd())
# Download file
url = ""
urllib.request.urlretrieve(url, 'dd')

import zipfile, urllib.request, shutil
url = 'https://www.nseindia.com/content/historical/EQUITIES/2017/JUN/cm05JUN2017bhav.csv.zip'
file_name = 'myzip.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()