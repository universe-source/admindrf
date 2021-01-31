"""
SimpleUI的自定义配置信息
"""
import time


SIMPLEUI_CONFIG = {
    # 是否保留系统默认的菜单, 默认不保留
    'system_keep': False,
    # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'menu_display': ['Simpleui', '测试', '权限认证', '动态菜单测试'],
    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'dynamic': True,    
    # menus字段: name-菜单名, icon-图标, url-链接地址, models-子菜单
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '组',
                    'icon': 'fas fa-user-friends',
                    'url': '/auth/group/',
                }
            ]
        },
        {
            'name': '网站测试',
            'icon': 'fa fa-search',
            'models': [{
                'name': time.time(),
                'url': 'http://baidu.com',
                'icon': 'far fa-surprise'
            }, {
                'name': 'xxxx',
                'url': 'http://baidu.com',
                'icon': 'far fa-surprise'
            }
            ]
        },
        {
            'name': '动态菜单测试',
            'icon': 'fas fa-search',
            'models': [
                {
                    'name': '百度',
                    'icon': 'far fa-surprise',
                    'url': 'https://www.baidu.com/',
                },
                {
                    'name': '百度问答',
                    'icon': 'far fa-surprise',
                    'url': 'https://zhidao.baidu.com/'
                }
            ]
        }
    ]
}

# 首页配置
#  SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
#  SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页链接
SIMPLEUI_INDEX = 'https://unusebamboo.top'
