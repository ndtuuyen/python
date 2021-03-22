

from urllib import request
import re
CONTRACT="0x2ec485c2da20d6dda3ba640dda5b9110a524998e"
f = open("eth.txt", "r")
ETH_ADDRESS = '0x5035cdd515c909924278815d14c63eea3b78e96d'
response = request.urlopen("https://api.ethplorer.io/getAddressInfo/"+ETH_ADDRESS+"?apiKey=EK-kM9C7-gaobdfU-9uLQW")
    #page_source = response.read().decode('utf-8')
page_source = response.read().decode('utf-8')
print(page_source)

