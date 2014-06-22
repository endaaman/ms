#-*- encoding: utf-8 -*-

from django.db import models
from candidate.models import Candidate
import os
from PIL import Image
from cStringIO import StringIO
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from ms import settings

def change_ext_to_pilformat(ext):
    EXT_TO_PILFORMAT = {
        'jpeg': 'JPEG',
        'jpg': 'JPEG',
        'png': 'PNG',
        'bmp': 'BMP',
    }
    p = EXT_TO_PILFORMAT.get(ext, None)
    if None:
        raise Exception('unregistered extension. you can use jpeg, jpg, png and bmp')
    return p


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

def upload_to(instance, filename):
    root, ext = os.path.splitext(filename)
    ext = ext.lower()
    return os.path.join('photos', '%d' % instance.candidate.entry_number, '%s%s' % (instance.name, ext))


def generate_upload_to(thumb=False):
    prefix = '-thumb' if thumb else ''

    def closure(instance, filename):
        root, ext = os.path.splitext(filename)
        ext = ext.lower()
        return os.path.join('photos', '%d' % instance.candidate.entry_number, '%s%s%s' % (instance.name, prefix, ext))

    return closure

class Photo(models.Model):
    candidate = models.ForeignKey('candidate.Candidate', verbose_name='候補者')
    name = models.CharField(max_length=50, verbose_name='名前', help_text='<名前>.<拡張子>でサーバーに保存されます。遠田の管理用でもあるので、英名で、長ぎず、最低限どの画像なのかわかるようなものにしてください。')
    image = models.ImageField(null=True, upload_to=generate_upload_to(), storage=OverwriteStorage(), verbose_name='画像', help_text='自動的に長辺が1920pxに収まるようにリサイズされます。')
    thumb = models.ImageField(null=True, blank=True, upload_to=generate_upload_to(True), storage=OverwriteStorage(), verbose_name='サムネイル', help_text='自動的に生成されるのでファイルを指定しないでください。')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='タイトル', help_text='写真のタイトルです。今のところ仕様されていません')
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='説明', help_text='写真の説明文です。今のところ使用されていません。')
    index = models.IntegerField(default=0, blank=True, null=True, verbose_name='表示順位', help_text='数値が低いものが前になります。')

    class Meta:
        # order_with_respect_to = 'candidate'
        ordering = ['candidate', 'index']

    def __unicode__( self):
        return 'No.%d %s - %s' % (self.candidate.entry_number, self.candidate.name, self.name,)

    def admin_image_view(self):
        return u'<img src="%s" height="100" />' % self.thumb.url
    admin_image_view.short_description = 'Image'
    admin_image_view.allow_tags = True

    def get_ext(self):
        e = os.path.splitext(str(self.image))[1].lower()[1:]
        return e


    def generate_thumb(self, thumb_size):
        self.image.seek(0)
        buf = StringIO(self.image.read())
        buf.seek(0)
        thumb_img = Image.open(buf)


        w = thumb_img.size[0]
        h = thumb_img.size[1]
        y = w > h
        l, s = y and (w, h) or (h, w)
        # 短い方に合わせる
        thumb_size_long = thumb_size * l / s

        thumb_img = thumb_img.resize(y and (thumb_size_long, thumb_size) or (thumb_size, thumb_size_long), Image.ANTIALIAS)

        cords = 4*[0]
        # left, top, right, bottom
        offset1 = (thumb_size_long - thumb_size) / 2
        offset2 = thumb_size_long - offset1
        if y:
            #0:left,2:right
            cords[0] , cords[2] = offset1, offset2
            cords[3] = thumb_size
        else:
            #1:top,3:bottom
            cords[1] , cords[3] = offset1, offset2
            cords[2] = thumb_size

        thumb_img = thumb_img.crop(cords)


        # img -resize-> thumb_img -StringIO-> fp -Cast<ContentFile>-> tmp_file
        fp = StringIO()
        thumb_img.save(fp, format=change_ext_to_pilformat(self.get_ext()))
        fp.seek(0)
        tmp_file = ContentFile(fp.read())
        root, ext = os.path.splitext(str(self.image))
        self.thumb.save('%s-thumb%s'%(root, ext), tmp_file, save=False)
        fp.close()

    def resize_image(self, new_size):
        self.image.seek(0)
        buf = StringIO(self.image.read())
        buf.seek(0)
        img = Image.open(buf)

        if img.size[0] > new_size or img.size[1] > new_size:
            img.thumbnail((new_size, new_size), Image.ANTIALIAS)

            fp = StringIO()
            img.save(fp, format=change_ext_to_pilformat(self.get_ext()))
            fp.seek(0)
            tmp_file = ContentFile(fp.read())
            self.image.save(str(self.image), tmp_file, save=False)
            fp.close()



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.resize_image(1920)
        self.generate_thumb(600)
        r = super(Photo, self).save(force_insert, force_update, using, update_fields)
        return r

    def delete(self, *args, **kwargs):

        img_storage, img_path = self.image.storage, self.image.path
        thumb_storage, thumb_path = self.thumb.storage, self.thumb.path
        super(Photo, self).delete(*args, **kwargs)
        img_storage.delete(img_path)
        thumb_storage.delete(thumb_path)

