import cv2, os 
haar_file = 'haarcascade_frontalface_default.xml'
  
#Will save data here
def add_data(name):
    #Create a folder in your local drive and give the path below
    datasets = 'datasets'  
  
    sub_data = name     
  
    path = os.path.join(datasets, sub_data) 
    if not os.path.isdir(path): 
        os.mkdir(path) 
  
    # img sample size
    (width, height) = (130, 100)     
  
    face_cascade = cv2.CascadeClassifier(haar_file) 
    webcam = cv2.VideoCapture(0)  
  
    # Will caputure upto 30 img
    count = 1
    while count < 30:  
        (_, im) = webcam.read() 
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
        for (x, y, w, h) in faces: 
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
            face = gray[y:y + h, x:x + w] 
            face_resize = cv2.resize(face, (width, height)) 
            cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
        count += 1
      
        cv2.imshow('OpenCV', im) 
        key=cv2.waitKey(10) 
        if key == 27: 
            break
        cv2.destroyAllWindows()