

likes = ["TDD", "DevOps", "Type checks", "Python", "Strong Duck typing",
         "NodeJS/Express", "Javascript/TypeScript"]

no_likes = ["Reflection", "VBA", "Magic", "AngularJS", "Springboot"]

resources = [{
    "Allen Holub": [
        {
            "blog": "https://holub.com/blog/",
            "twitter": "https://twitter.com/allenholub",
        }
    ],
    "GOTO": [
        {
            "youtube": "https://www.youtube.com/user/GotoConferences"
        }
    ]
}]

personal_manifesto_description = "Things I strive for"
personal_manifesto = [
    {
        "title": "Being rational"
    },
    {
        "title": "Call out BS, but be kind",
    },
    {
        "title": "No silver bullet"
    },
    {
        "title": "The existence of multiple subobtimal solutions does not mean there are no wrong answers"
    },
    {
        "title": "Read books",
        "remarks": "primary sourcing"
    },
    {
        "title": "Delayed Gratification"
    }
]

tech_manifesto = [
    {
        "name": "(Build, Lint and Test) or bust"
    }
]


def linkify_reach_me(url):
    return "<a href='{}'>{}</a>".format(url["link"], url["html"])


reach_me = [
    {"html": "gmail", "link": "mailto:103879u@gmail.com"},
    {"html": "linkedin", "link": "https://www.linkedin.com/in/joel-lim-jing/"},
    {"html": "medium", "link": "https://medium.com/@aljorhythm"}
]

template = open('readme.template.md').read()
readme = template.format(opinions_yes="<br>".join(likes),
                         opinions_no="<br>".join(no_likes),
                         reach_me=" | ".join([linkify_reach_me(url) for url in reach_me]))
open('readme.md', 'w').write(readme)
