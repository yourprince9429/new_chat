from url import *
import tornado.web
import os
from app.conf.config import *

from url_admin import *

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "views"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)
handlers = []


##根据web.ini设定相关参数
def application_setting_handle():
    _config = WebConfig()
    setting["template_path"] = _config.cf.get("web", "template_path")
    setting["static_path"] = _config.cf.get("web", "static_path")
    # --这里要加入静态文件的直接访问。
    handlers.append((r"/data/(.*)", tornado.web.StaticFileHandler, {"path": "data"}))  # 这是data静态文件，用自定义静态文件的路由。
    handlers.append((r"/images/(.*)", tornado.web.StaticFileHandler, {"path": "images"}))  # 这是images静态文件，用自定义静态文件的路由。
    handlers.append((r"/upload/(.*)", tornado.web.StaticFileHandler, {"path": "upload"}))  # 这是上传的静态文件，用自定义静态文件的路由。
    handlers.extend(url)  # pc端页面。
    handlers.extend(url_admin)  # 后台相关页面，


application_setting_handle()
application = tornado.web.Application(
    handlers=handlers,
    **setting
)
