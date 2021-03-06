import csv
from requests_html import HTML, HTMLSession

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render() # html.render() to get dynamic content

match = html.find('#footer', first=True)
print(match.html)


# session = HTMLSession()
# r = session.get('https://coreyms.com/')

# for link in r.html.absolute_links:
#     print(link)

# csv_file = open('cms_scrape.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video'])


# articles = r.html.find('article')

# for article in articles:
#     headline = article.find('.entry-title-link', first=True).text
#     print(headline)

#     summary = article.find('.entry-content p', first=True).text
#     print(summary)

#     try:
#         vid_src = article.find('iframe', first=True).attrs['src']
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         # print(vid_id)

#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except AttributeError:
#         yt_link = None

#     print(yt_link)
#     print()

#     csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()