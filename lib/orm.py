class ModelMixin:
    def to_dict(self, ignore_fileds=()):
        '''将一个 model 转换成一个 dict'''
        attr_dict = {}
        for field in self._meta.fields:                # 遍历所有字段
            name = field.attname                       # 取出字段名称
            if name not in ignore_fileds:              # 检查是否是需要忽略的字段
                attr_dict[name] = getattr(self, name)  # 获取字段对应的值
        return attr_dict
