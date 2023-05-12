import cv2

#Вращение картинки
def rotation(img):
    (h, w) = img.shape[:2]
    center = (int(w / 2), int(h / 2))
    rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.6)
    rotated = cv2.warpAffine(img, rotation_matrix, (w, h))
    return rotated

#Функция вычисления хэша
def CalcImageHash(FileName):
    image = cv2.imread(FileName) #Прочитаем картинку
    resized = cv2.resize(image, (16,16), interpolation = cv2.INTER_AREA) #Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #Переведем в черно-белый формат
    avg=gray_image.mean() #Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) #Бинаризация по порогу
    
    #Рассчитаем хэш
    _hash=""
    for x in range(16):
        for y in range(16):
            val=threshold_image[x,y]
            if val==255:
                _hash=_hash+"1"
            else:
                _hash=_hash+"0"
            
    return _hash

def CalcImageHash1(image):
    resized = cv2.resize(image, (16,16), interpolation = cv2.INTER_AREA) #Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #Переведем в черно-белый формат
    avg=gray_image.mean() #Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) #Бинаризация по порогу
    
    #Рассчитаем хэш
    _hash=""
    for x in range(16):
        for y in range(16):
            val=threshold_image[x,y]
            if val==255:
                _hash=_hash+"1"
            else:
                _hash=_hash+"0"
            
    return _hash

def CompareHash(hash1,hash2):
    l=len(hash1)
    i=0
    count=0
    while i<l:
        if hash1[i]!=hash2[i]:
            count=count+1
        i=i+1
    return count

flag = 0
hash2=CalcImageHash(r"pictures/doc.jpg")
ls = list()
ima = cv2.imread(r"pictures/doc_copy.jpg")
for i in range(4):
    ls.append(ima)
    ima = rotation(ima)
for i in ls:
    if (CompareHash(CalcImageHash1(i), hash2)<80):
        flag = 1
if (flag == 0):
    print("Несовпадение")
else:
    print("Совпадение")
