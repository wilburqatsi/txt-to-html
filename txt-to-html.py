import re

with open("1988.txt", "r", encoding="GB2312", errors="replace") as f:
    lines = f.readlines()

title = "1988：我想和这个世界谈谈"

head = f"""<!DOCTYPE html>
<html>
<head>
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body{{
        max-width: 1000px;
        margin: auto;
        color: #ffffff;
        font-family: Helvetica, Tahoma, Arial, “STXihei”, “华文细黑”, “Microsoft YaHei”, “微软雅黑”, sans-serif;
        font-size: 2.5em;
        background-color: #000000;
    }}
    #contents a{{
        display: block;
        text-decoration: none;
    }}
    #contents a:visited{{
        color: cyan;
    }}
  </style>
</head>\n"""

contents = []

chapter = re.compile("第\d*节")


text = ""
for line in lines:
    match = chapter.match(line)
    if match is not None:
        text += f"<h2 id='{line.rstrip()}'>" + line.rstrip() + "</h2>\n"
        contents.append(match.group())
    else:
        text += "<p>" + line.rstrip() + "</p>\n"

table_of_contents = "<div id='contents'>" + "<h2>Table of Contents</h2>"
for chapter in contents:
    table_of_contents += f"<a href='#{chapter}'>{chapter}</a>\n"
table_of_contents += "</div>\n"

body = "<body>\n" + f"<h1>{title}</h1>\n"
body += table_of_contents
body += text
body += "</body>\n"

foot = "</html>"

with open(f"{title}.html".strip(" "), "w") as w:
    w.write(head + body + foot)
