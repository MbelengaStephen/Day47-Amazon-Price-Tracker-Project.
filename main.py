import requests
from bs4 import BeautifulSoup
import smtplib
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
EMAIL = "peppersoup234@gmail.com"
MY_EMAIL = "mbelengamichael21@gmail.com"
PASSWORD = "mbelenga21"

url = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=pd_di_sccai_1/" \
      "130-6503134-1932226?pd_rd_w=JkNPj&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=3533133AZMPRVY1PKHK2&pd_rd_" \
      "r=e4b911e4-b68f-4df8-86d7-dbe7680dc677&pd_rd_wg=bxu7Z&pd_rd_i=B08PQ2KWHS&psc=1"
response = requests.get(url=url, headers=headers)
content = response.text
soup = BeautifulSoup(content, "html.parser")
title = soup.find(name="span", id="priceblock_dealprice").getText()
price_without_currency = title.split("$")[1]
price_as_float = float(price_without_currency)
current_price = price_as_float
BUY_PRICE = 200

if current_price < BUY_PRICE:
    message = f"{title} is now ${current_price}"

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}")