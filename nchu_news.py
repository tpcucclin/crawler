# %%
import requests
from bs4 import BeautifulSoup
import csv

# 目標 URL
url = "https://www2.nchu.edu.tw/news"

# 發送 GET 請求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 解析 HTML
soup = BeautifulSoup(response.text, "html.parser")

# 找到所有新聞項目
news_items = soup.select(".item-group ul li a")

data = []

for item in news_items:
    date = item.select_one(".date").text.strip()
    title = item.select_one("h2.title").text.strip()
    link = item["href"]
    if not link.startswith("http"):
        link = "https://www2.nchu.edu.tw" + link
    
    data.append([date, title, link])

# 儲存為 CSV
csv_filename = "nchu_news.csv"
with open(csv_filename, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["日期", "標題", "連結"])
    writer.writerows(data)

print(f"新聞已儲存至 {csv_filename}")
# %%
