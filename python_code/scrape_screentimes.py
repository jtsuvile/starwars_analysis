from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = "https://www.screentimecentral.com/star-wars-characters/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
all_screentimes_html = soup.find_all( class_ = "font_8 wixui-rich-text__text" ) 
df = pd.DataFrame()
for section in all_screentimes_html:
    if "EPISODE" in section.text and "%" in section.text:
        episode_str = section.text
        episode_str_list = episode_str.split('\n')
        episode_str_list = [x for x in episode_str_list if x != '']
        episode_df = pd.DataFrame({'appearances':episode_str_list[1:]})
        episode_df[['character','sep_1','minutes','sep_2','proportion']] = episode_df['appearances'].str.split(r"(/| - )", expand=True, regex=True)
        episode_df = episode_df[['character','minutes','proportion']]
        episode_df['film'] = episode_str_list[0]
        df = pd.concat([df, episode_df])

df.to_csv('')
