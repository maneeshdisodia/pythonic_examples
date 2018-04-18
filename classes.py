import urllib2
import json


# st = 100
# for s in range(1, 2000):
#     url = "http://67.205.153.219:8983/solr/indiadata/select?q=*:*" + "&start=" + str(
#         st) + "&rows=1000&wt=json&indent=true"
#     print(url)
#     response = urllib2.urlopen(str(url), timeout=20000)
#     if not response is None:
#         data = json.load(response)
#         docs = data['response']['docs']  # solr.search('info.location:*"noida"*',start=0,rows=100000)
#         totalcount = data['response']['numFound']
#         print(totalcount)
#         # print(r1)
#

def get_industry_data():
    url = "http://67.205.153.219:8983/solr/indiadata/select?q=*:*&start=100&rows=1000&wt=json&indent=true"
    result = {}
    response = urllib2.urlopen(url, timeout=2000000)
    if not response is None:
        res = json.load(response)
        print(res)
        return res
    else:
        return


rt =get_industry_data()
print(rt)
