from django.shortcuts import render

# Create your views here.
import cv2
from django.http import JsonResponse

def detect_faces(request):

    print(request.method)
    if request.method == 'POST':
        print(request)
        image = request.FILES.get('image')
        if image:
            # Read the image file
            img = cv2.imread(image.temporary_file_path())

            # Load the pre-trained face detection classifier
            face_cascade = cv2.CascadeClassifier('path_to_haar_cascade_xml')

            # Convert the image to grayscale for face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Perform face detection
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Prepare the response with bounding box coordinates of detected faces
            response = []
            for (x, y, w, h) in faces:
                response.append({'x': x, 'y': y, 'width': w, 'height': h})

            return JsonResponse({'faces': response})

        return JsonResponse({'error': 'No image provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method provided'}, status=405)
