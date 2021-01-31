"""
SimpleUI 配置
"""


SIMPLEUI_CONFIG = {
    # 1 是否需要保留系统默认的菜单, False-不保留
    'system_keep': False,
    # 2 开启排序和过滤功能(最好不要添加, 空值则什么都没有)
    #  'menu_display': ['权限认证',],
    # 3 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'dynamic': True,
    # 4 菜单项
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',  # 图标https://fontawesome.com/icons
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '组',
                    'icon': 'fa fa-user-friends',
                    'url': 'auth/group/'
                }
            ],
        },
        {
            'name': '搜索引擎和字典',
            'icon': 'fas fa-search',
            'models': [
                {
                    'name': 'Baidu',
                    'icon': 'far fa-surprise',
                    'url': 'https://www.baidu.com/',
                },
                {
                    'name': '有道翻译',
                    'icon': 'far fa-surprise',
                    'url': 'http://fanyi.youdao.com/'
                },
            ],
        }
    ]
}
