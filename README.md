# KhootClone

## สัปดาห์ที่ 2

โครงสร้างของโครงงานและการรับส่งข้อมูล (HttpRequest,HttpResponse)

### ผลลัพธ์การเรียนรู้

1. เข้าใจรูปแบบการส่งและรับข้อความระหว่างเครื่องผู้ใช้และเครื่องแม่ข่ายได้(client-server)

2. อธิบายองค์ประกอบของข้อมูลคำร้อง (request) ได้

3. อธิบายองค์ประกอบของข้อมูลส่งกลับ (response) ได้

4. สร้างโครงงานและเขียนคำสั่งรับส่งข้อมูลได้

5. ความรู้เบื้องต้นเกี่ยวกับการพัฒนาเว็บ

### เอกสารประกอบ

* Chapter 2 Request and response objects - https://docs.djangoproject.com/en/5.0/ref/request-response/

* HTTP Messages - https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages

* Tutorial - https://docs.djangoproject.com/en/5.0/intro/tutorial0kk1/ 


* Reportlab User Guide - https://docs.reportlab.com/reportlab/userguide/ch1_intro/ 

* Image Manipulation - https://realpython.com/image-processing-with-the-python-pillow-library/ 


### เอกสารปฏิบัติ

1. Json Response - https://docs.djangoproject.com/en/5.0/ref/request-response/#jsonresponse-objects

2. PDF Response - https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/

3. CSV Response - https://docs.djangoproject.com/en/5.0/howto/outputting-csv/

4. Image Response 

```python
from django.http import HttpResponse
from PIL import Image, ImageDraw   

def blur(req):  
    img = Image.new('RGB', (100,50))
    drawer = ImageDraw.Draw(img)
    drawer.text((10,10), '1145005 Web Dev', fill=(100,250,120))  
    del drawer
    response = HttpResponse(mimetype="image/png")  
    img.save(response, 'PNG')  
    return response
```
