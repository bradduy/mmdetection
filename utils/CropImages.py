# First step
import cv2

filename = '../../video_for_training/validation.txt'
with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
array = []
listImage = []
# print(content)
for element in content:
    check = element[-2:]
    # print(check)
    if str(check) == ' 0':
        array.append(element)
    if str(element[-4:]) == '.png':
        listImage.append(element)
# print(listImage)
# print(array)
for i in range(len(listImage)):

    path = '/home/duy/Documents/video_for_training/images/' + listImage[i][-16:]
    pathSave = '/home/duy/Documents/mmdetection/2bbox/'

    img = cv2.imread(path)
    bbox = array[i].split(' ')
    bbox[0] = round(float(bbox[0]))
    bbox[1] = round(float(bbox[1]))
    bbox[2] = round(float(bbox[2]))
    bbox[3] = round(float(bbox[3]))
    y1 = int(bbox[0]) + int(bbox[2])
    y2 = int(bbox[1]) + int(bbox[3])

    image = cv2.rectangle(img, (bbox[0], bbox[1]), (y1, y2), (0, 0, 255), thickness=5)

    cv2.imwrite(pathSave + listImage[i][-16:], image)
    i += 1
    if i % 30 == 0:
        print('-------------------->', i)
    cv2.waitKey(0)

