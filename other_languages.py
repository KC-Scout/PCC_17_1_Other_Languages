import requests
import pygal

url = (
    "https://api.github.com/search/repositories?q="
"language:javascript&sort=stars"
)
r = requests.get(url)
request = r.json()

top_thirty_list = request['items']
top_ten = top_thirty_list[:10]

x_labels, stars = [], []
for item in top_thirty_list[:10]:
    x_labels.append(item['name'])
    stars.append(item['stargazers_count'])
    
chart = pygal.Bar()
chart.x_labels = x_labels
chart.add('', stars)
chart.render_to_file('javascript_top_ten.svg')


