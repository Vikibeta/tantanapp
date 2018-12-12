from django.utils.deprecation import MiddlewareMixin

from common import errors
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    white_list = [
        '/api/user/vcode',
        '/api/user/login',
    ]

    def process_request(self, request):
        # 检查当前 path 是否在白名单内
        if request.path in self.white_list:
            return

        # 用户登录验证
        uid = request.session.get('uid')
        if uid is None:
            return render_json(None, errors.LoginRequire.code)
        else:
            try:
                user = User.objects.get(id=uid)
            except User.DoesNotExist:
                return render_json(None, errors.UserNotExist.code)
            else:
                # 将 user 对象添加到 request
                request.user = user


class LogicErrorMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        '''异常处理'''
        if isinstance(exception, errors.LogicError):
            return render_json(None, exception.code)  # 处理逻辑错误
