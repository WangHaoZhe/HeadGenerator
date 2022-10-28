import headGenerator.add_picture
from django.shortcuts import render
import json

def receive_data(request):
    path = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
    return render(request, "index.html", {"new_img_path": json.dumps(path)})
