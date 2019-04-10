# coding:utf-8
import sys
import tornado.web
import os
from app.web.modules.testModule import index as TestIndex
from app.web.modules.PC import *

url = [
    # (r"/data/(.*)", tornado.web.StaticFileHandler,{"path":"data"})#这是data静态文件，用自定义静态文件的路由。
    (r"/test", TestIndex)
    # pc版页面，
    , (r"/index\.html", pc_index)

]
