#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():
    api_addr = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    res= requests.get(api_addr)
    print(res)

    if res.status_code ==200:
        html = res.text
        soup = BeautifulSoup(html,"xml")
        
        locations = soup.find_all('location')
        for location in locations :
            city = location.find("city").text
            data = location.find("data").find("tmEf").text
            weather = location.find("data").find("wf").text

            print(f"[ {data} ] {city} : {weather}")

if __name__ == "__main__":
    main()
