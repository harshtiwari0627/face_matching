import face_recognition

b1 = face_recognition.load_image_file("A.jpg")  # Edit the image location inplace of $$
c1 = face_recognition.face_encodings(b1)[0]

b = face_recognition.load_image_file("B.jpg")  # Edit the image location inplace of $$
c = face_recognition.face_encodings(b)[0]

matches = face_recognition.compare_faces([c], c1)
