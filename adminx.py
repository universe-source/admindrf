# coding:utf8
"""
站点全局配置
"""
import xadmin
from xadmin import views

#  from .book.models import Book, BookLabel


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    """ 设置部件:
        url: https://docs.djangoproject.com/zh-hans/3.1/ref/forms/widgets/
        说明: Django 对 HTML 输入元素的表示, 处理 HTML 渲染.
            a. 表单字段处理输入验证的逻辑, 直接在模板中使用;
            b. 小组件处理 HTML 表单输入元素在网页上的渲染和原始提交数据的提取
        实际上, 在表单中指定一个字段时, Django 会使用一个默认的部件来显示数据类型.(Field)
    """
    widgets = [
        [
            {
                "type": "html",
                "title": "Test Widget",
                "content": "<h3> Welcome to Xadmin!</h3>"
            },
            {
                "type": "chart",
                "model": "app.accessrecord",
                "chart": "user_count",
                "params": {"_p_date__gte": "2013-01-08", "p": 1, "_p_date__lt": "2013-01-29"}
            },
            {
                "type": "list",
                "model": "app.host",
                "params": {"o": "-guarantee_date"}
            },
        ],
    ]


@xadmin.sites.register(views.website.BaseAdminView)
class BaseSetting(object):
    """ xadmin的基本配置 """
    enable_themes = True      # 开启主题切换功能
    use_bootswatch = True     # 支持切换主题


@xadmin.sites.register(views.CommAdminView)
class GlobalSettings(object):
    """ xadmin的全局配置 """
    site_title = "drf后台管理系统"   # 设置站点标题
    site_footer = "unusebamboo"     # 设置站点的页脚
    menu_style = "accordion"    # 设置菜单折叠，在左侧，默认的
    # 设置搜索栏可选models(表名)
    #  global_search_models = [Book, BookLabel]
    # models的全局图标
    #  global_models_icon = {
    #      Book: "glyphicon glyphicon-user",
    #      BookLabel: "fa fa-cloud"
    #  }


class MaintainInline(object):
    #  model = MaintainLog
    extra = 1
    style = "accordion"
