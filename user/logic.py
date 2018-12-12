import os

from django.conf import settings
from worker import call_by_worker
from lib.qncloud import upload_to_qiniu


def save_upload_file(user, upload_file):
    '''将上传的文件保存到本地'''
    filename = 'avatar_%s' % user.id
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(filepath, 'wb') as fp:
        for chunk in upload_file.chunks():
            fp.write(chunk)
    return filepath, filename


@call_by_worker
def upload_avatar_to_qiniu(user, filepath, filename):
    '''将用户头像上传到七牛云'''
    *_, avatar_url = upload_to_qiniu(filepath, filename)
    user.avatar = avatar_url
    user.save()
