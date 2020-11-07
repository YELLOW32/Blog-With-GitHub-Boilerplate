# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "YELLOW32",
    "type": "local",
    "path": "../YELLOW32"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "YELLOW 32"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "YELLOW"
email = "2044127201@qq.com"
author_homepage = "https://www.github.com/YELLOW32"
description = "Everything you do,they are all yellow"
key_words = ['YELLOW32', 'YELLOW', '32', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "YELLOW32",
        "url": "https://github.com/YELLOW32",
        "brief": "🏄‍ Go My Own FUCKING Way."
    },
    {
        "name": "黄色計劃",
        "url": "https://www.github.com/YELLOW32",
        "brief": "YELLOW 32的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = 
    {
        "name": "GitHub",
        "url": "https://github.com/YELLOW32",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5602436052/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
