import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"
result = requests.get(url )
bs_obj = BeautifulSoup (result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class":"lf-item"})

hrefs = [div.find("a")['href'] for div in lf_items ]

print (hrefs)

# From now subpages


def get_bp_info (url):

    result = requests.get(url)
    bs_obj = BeautifulSoup (result.content, "html.parser")

    profile_name = bs_obj.find("div", {"class":"profile-name"})
    bpName = profile_name.find("h1").text

    cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
    locationAndWebsite = cover_buttons.findAll("span", {"class":"button-label"})

    print (len(locationAndWebsite))

    location = locationAndWebsite[0].text
    if len(locationAndWebsite)<2 :
        website = ""
    else :
        website = locationAndWebsite[1].find("a") ['href']

    bpInformation = { }
    bpInformation ['name'] = bpName
    bpInformation ['location'] = location
    bpInformation ['website'] = website

    return bpInformation


for i in range(0,4):
    bpInfo = get_bp_info(hrefs[i])
    print (bpInfo)




'''
def get_bp_info(url):

    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    profile_name = bs_obj.find("div", {"class":"profile-name"})

    h1_bp_name = profile_name.find("h1")
    bp_name = h1_bp_name.text

    cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})

    button_label = bs_obj.find("span", {"class":"button-label"})
    location = button_label.text

    lis = cover_buttons.findAll ("li")
    li_tag = lis[1]

    a_tag = li_tag.find("a")
    link = a_tag['href']

    dictionary1 = {}
    dictionary1 ['name'] = bp_name
    dictionary1 ['location'] = location
    dictionary1 ['link'] = link

    return dictionary1

url = "https://bp.eosgo.io/"
result = requests.get(url)
bs_obj = BeautifulSoup (result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class":"lf-item"})

hrefs = [div.find("a")['href'] for div in lf_items]

dic_result = get_bp_info(hrefs[0])
print (dic_result)

'''
