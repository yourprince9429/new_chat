import tornado.web
import os.path
import tornado.ioloop
import mako.lookup
import tornado.httpserver
import mako.template

import app.common.commons


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        template_path = self.get_template_path()
        self.lookup = mako.lookup.TemplateLookup(directories=[template_path], input_encoding='utf-8',
                                                 output_encoding='utf-8')
        # self._config = Config()
        # self.lookup = mako.lookup.TemplateLookup(directories=[template_path])

    # def get_conf(self,field,key):
    #    return self._config.get(field,key)
    def render_string(self, template_path, **kwargs):

        try:
            _debug = self.get_argument("debug", "false")
            template = self.lookup.get_template(template_path)
            namespace = self.get_template_namespace()
            namespace.update(kwargs)

            # siteConfig=WebConfig()
            env_kwargs = dict(
                handler=self,
                request=self.request,
                locale=self.locale,
                _=self.locale.translate,  # 国际化i18n的支持
                static_url=self.static_url,
                xsrf_form_html=self.xsrf_form_html,
                reverse_url=self.application.reverse_url,
                jsDebug=_debug,
                # get_conf = self.get_conf,
                # 加一个我们的相关设定下去。
                # conf=siteConfig

            )
            env_kwargs.update(kwargs)
            return template.render(**env_kwargs)
        except Exception as e:
            print("服务端错误")
            print(e)
            pass
