class LogicError(Exception):
    '''逻辑异常类'''
    code = 0

    def __str__(self):
        return self.__class__.__name__


def generate_logic_error(name: str, code: int) -> LogicError:
    '''创建逻辑异常的子类'''
    base_cls = (LogicError,)
    return type(name, base_cls, {'code': code})


OK = generate_logic_error('OK', 0)
VcodeError = generate_logic_error('VcodeError', 1000)
VcodeExist = generate_logic_error('VcodeExist', 1001)
LoginRequire = generate_logic_error('LoginRequire', 1002)
UserNotExist = generate_logic_error('UserNotExist', 1003)
ProfileError = generate_logic_error('ProfileError', 1004)
