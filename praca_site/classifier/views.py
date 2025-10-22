from django.shortcuts import render
from .cnn_model.predict import predict_image
import os
from django.conf import settings

# Create your views here.

def classify_image(request):
    results = []  # lista wyników dla wszystkich obrazów
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp_uploads')
    os.makedirs(temp_dir, exist_ok=True)

    if request.method == 'POST' and request.FILES.getlist('images'):
        for image_file in request.FILES.getlist('images'):
            file_path = os.path.join(temp_dir, image_file.name)
            with open(file_path, 'wb') as f:
                for chunk in image_file.chunks():
                    f.write(chunk)
            result, confidence = predict_image(file_path)
            image_url = os.path.join(settings.MEDIA_URL, 'temp_uploads', image_file.name.replace('\\', '/'))

            results.append({
                'result': result,
                'confidence': confidence,
                'image_url': image_url
            })

    return render(request, 'classifier/classify.html', {'results': results})
