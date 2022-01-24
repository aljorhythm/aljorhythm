#example: python3 links_to_markdown.py ../gists/data.yt | pbcoby
# python3 scripts/links_to_markdown.py gists/data.yt | pbcopy
import sys
from urllib.parse import urlparse, parse_qs

filepath = sys.argv[1]

f = open(filepath, 'r')
content = f.read()

i = 0
lines = content.split("\n")

template = """
### {}
[![IMAGE ALT TEXT](http://img.youtube.com/vi/{}/0.jpg)]({} "{}")
"""
while i < len(lines):
    title = lines[i]

    i += 1
    url = lines[i]

    parsed_url = urlparse(url)
    query = parse_qs(parsed_url.query)
    video_id = query["v"][0]
    output_line = template.format(title, video_id, url, title)
    print(output_line)
    i += 2