import yaml
import xml.etree.ElementTree as xml_tree
import http.client

conn = http.client.HTTPSConnection("live-metal-prices.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "b55da08e82msh6947c9ac7782b19p1677bfjsn00e61c6e8ffd",
    'X-RapidAPI-Host': "live-metal-prices.p.rapidapi.com"
}

conn.request("GET", "/v1/latest/XAU_14K,XAU_18K,XAU_22K,XAU_24K/INR/GRAM", headers=headers)

res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))

with open('feed.yaml', 'r')as source:
    yaml_data = yaml.safe_load(source)

rss_element = xml_tree.Element('rss', {'version': '2.0'})