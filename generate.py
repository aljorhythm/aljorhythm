

likes = ["Type checks", "Python", "Strong Duck typing",
         "NodeJS/Express", "Javascript/TypeScript"]

no_likes = ["Reflection", "VBA", "Magic", "AngularJS", "Springboot"]


def linkify(url):
    return "<a href='{}'>{}</a>".format(url["link"], url["html"])


reach_me = [
    {"html": "gmail", "link": "mailto:103879u@gmail.com"},
    {"html": "linkedin", "link": "https://www.linkedin.com/in/joel-lim-jing/"}
]

template = open('readme.template.md').read()
readme = template.format(opinions_yes="<br>".join(likes),
                         opinions_no="<br>".join(no_likes),
                         reach_me=" | ".join([linkify(url) for url in reach_me]))
open('readme.md', 'w').write(readme)
