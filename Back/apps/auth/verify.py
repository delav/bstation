# coding: utf-8
import random
from PIL import ImageDraw, Image, ImageFont
from django.http import HttpResponse
from io import BytesIO
from django.conf import settings 


class CreateVerifyCode(object):

    @staticmethod
    def verify_code(request):
        bg_color = (255, 255, 255)
        width = 100
        height = 30
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, height))
            fill = (random.randrange(0, width), 255, random.randrange(0, height))
            draw.point(xy, fill=fill)
        # 随机干扰线条数
        n_line = (1, 3)
        line_num = random.randint(*n_line)
        for i in range(line_num):
            begin = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0, width), random.randint(0, height))
            draw.line([begin, end], fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
        strings = '0123456789abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0'
        # 随验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += strings[random.randrange(0, len(strings))]
        # 字体类型和大小
        font = ImageFont.truetype(settings.BASE_DIR+'/apps/auth/arial.ttf', size=25)
        # 绘制:参数分别为 位置、字体、字体类型、字体颜色
        draw.text((5, 2), rand_str[0], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
        draw.text((25, 2), rand_str[1], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
        draw.text((50, 2), rand_str[2], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
        draw.text((75, 2), rand_str[3], font=font, fill=(255, random.randrange(0, 255), random.randrange(0, 255)))
        # 释放画笔
        del draw
        # 存入session，用于做进一步验证
        request.session['code'] = rand_str
        request.session.set_expiry(settings.VERIFY_CODE_TIMEOUT)
        buf = BytesIO()
        # 将图片保存在内存中，文件类型为png
        img.save(buf, 'png')
        # 将内存中的图片数据返回给客户端，MIME类型为图片png
        return HttpResponse(buf.getvalue(), 'image/png')

