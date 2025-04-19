from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import csv


def time_to_minutes(time_str):
    """Convert a duration of format mm:ss or hh:mm:ss into
    minutes expressed as a decimal."""
    time_str = time_str.strip()
    parts = time_str.split(':')
    parts = list(map(int, parts))

    if len(parts) == 3:
        hours, minutes, seconds = parts
    elif len(parts) == 2:
        hours = 0
        minutes, seconds = parts
    else:
        raise ValueError(f"Unexpected time format: {time_str}")

    total_minutes = hours * 60 + minutes + seconds / 60
    return round(total_minutes, 2)


url = "https://www.screentimecentral.com/star-wars-characters/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
all_screentimes_html = soup.find_all(class_="font_8 wixui-rich-text__text")
df = pd.DataFrame()
for section in all_screentimes_html:
    if "EPISODE" in section.text and "%" in section.text:
        episode_str = section.text
        episode_str_list = episode_str.split('\n')
        episode_str_list = [x for x in episode_str_list if x != '']
        episode_df = pd.DataFrame({'appearances': episode_str_list[1:]})
        episode_df[['character', 'sep_1', 'minutes', 'sep_2', 'proportion']] \
            = episode_df['appearances'].str\
            .split(r"(/| - )", expand=True, regex=True)
        episode_df = episode_df[['character', 'minutes', 'proportion']]
        episode_df['film'] = episode_str_list[0]
        df = pd.concat([df, episode_df])

# clean up the resulting data to make it easier to work with
# clean up % sign from the "proportion" column
df['proportion'] = df['proportion'].str.strip().str.replace('%', '')
# fix minutes representation from : to .
df['minutes'] = df['minutes'].apply(time_to_minutes)
# split name column to more informative columns
df[['episode', 'film_name', 'release_year']] = df['film'].str\
    .extract(r'EPISODE (\w+) - (.+) \((\d{4})\)')
df = df.drop(columns='film')

df.to_csv('/Users/juusu53/Documents/code/starwars_analysis/' +
          'starwars_analysis/seeds/raw_screentime.csv', index=False,
          quoting=csv.QUOTE_ALL)
