#https://www.google.com/search?q=weather+today&oq=weather+&gs_lcrp=EgZjaHJvbWUqDQgEEAAYgwEYsQMYgAQyBwgAEAAYjwIyDQgBEAAYkgMYgAQYigUyDQgCEAAYkgMYgAQYigUyEggDEAAYQxiDARixAxiABBiKBTINCAQQABiDARixAxiABDINCAUQABiDARixAxiABDISCAYQABhDGIMBGLEDGIAEGIoFMgoIBxAAGLEDGIAEMgoICBAAGLEDGIAEMgoICRAAGLEDGIAE0gEKMTY5MjlqMWoxNagCCLACAQ&sourceid=chrome&ie=UTF-8
#user agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
#span id='wob_tm'
#span class='wob_t'
from requests_html import HTMLSession
import speech_to_text


def weather_find():
    s1= HTMLSession()
    query="patna"
    url = "https://www.google.com/search?q=weather+today&oq=weather+&gs_lcrp=EgZjaHJvbWUqDQgEEAAYgwEYsQMYgAQyBwgAEAAYjwIyDQgBEAAYkgMYgAQYigUyDQgCEAAYkgMYgAQYigUyEggDEAAYQxiDARixAxiABBiKBTINCAQQABiDARixAxiABDINCAUQABiDARixAxiABDISCAYQABhDGIMBGLEDGIAEGIoFMgoIBxAAGLEDGIAEMgoICBAAGLEDGIAEMgoICRAAGLEDGIAE0gEKMTY5MjlqMWoxNagCCLACAQ&sourceid=chrome&ie=UTF-8"
    url2="https://www.google.com/search?q+weather+{query}"
    r1 = s1.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})
    temp = r1.html.find('span#wob_tm',first = True).text
    unit= r1.html.find('div.vk_bk.wob-unit span.wob_t',first = True).text
    desc= r1.html.find('span#wob_dc',first = True).text
    return temp+" "+unit+" "+desc


# from requests_html import HTMLSession

# s1 = HTMLSession()
# query = "patna"
# url = f"https://www.google.com/search?q=weather+{query}"

# try:
#     r1 = s1.get(url, headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
#     })

#     # Extracting weather information
#     temp_element = r1.html.find('span#wob_tm', first=True)
#     unit_element = r1.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
#     desc_element = r1.html.find('span#wob_dc', first=True)

#     if temp_element and unit_element and desc_element:
#         temp = temp_element.text
#         unit = unit_element.text
#         desc = desc_element.text

#         print(f"Temperature: {temp} {unit}")
#         print(f"Description: {desc}")
#     else:
#         print("Weather information not found.")
# except Exception as e:
#     print(f"Error fetching weather: {e}")
