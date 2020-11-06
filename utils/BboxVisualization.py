# from d2l import torch as d2l

# d2l.set_figsize()
# img = d2l.plt.imread('../video_for_training/test/frame.png')
# d2l.plt.imshow(img)

# bbox = [3.23945215e+03,  9.44254028e+02,  3.34550537e+03, 1.16835718e+03]
#
# def bbox_to_rect(bbox, color):
#     """Convert bounding box to matplotlib format."""
#     # Convert the bounding box (top-left x, top-left y, bottom-right x,
#     # bottom-right y) format to matplotlib format: ((upper-left x,
#     # upper-left y), width, height)
#     return d2l.plt.Rectangle(
#         xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1],
#         fill=False, edgecolor=color, linewidth=2)
#
#
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# img = mpimg.imread('../video_for_training/test/frame.png')
# imgplot = plt.imshow(img)
# fig = d2l.plt.imshow(img)
# fig.axes.add_patch(bbox_to_rect(bbox, 'red'))
# plt.show()
arr = [0, 0.0641, 0.2582, 0.2947, 0.2322, 0.1296, 0.2058, 0.0348, 0.0535, 0.4430, 0.0658, 0.2146, 0.1270, 0.3263,
       0.2134, 0.2481, 0.0731, 0.1450, 0.0941, 0.1157, 0.2110, 0.1043, 0.2107, 0.1123, 0.1426, 0.2381, 0.1601,
       0.1889, 0.1766, 0.0852, 0.2744, 0.3022, 0.1295, 0.0740, 0.1452, 0.1369, 0.0934, 0.1076, 0.2531, 0.1939,
       0.1361, 0.1001, 0.2267, 0.1683, 0.0750, 0.1663, 0.2343, 0.2064, 0.3029, 0.0877, 0.2691, 0.1311, 0.2412,
       0.2042, 0.2179, 0.2201, 0.2345, 0.1734, 0.1576, 0.2059, 0.1219, 0.1345, 0.1175, 0.2434, 0.0679, 0.0895,
       0.1258, 0.1162, 0.1954, 0.2185, 0.1538, 0.1542, 0.1597, 0.1811, 0.2027, 0.1191, 0.0852, 0.0806, 0.0714,
       0.1391, 0.0650, 0.0862, 0.1991, 0.0900, 0.0806, 0.1193, 0.2268, 0.1540, 0.0535, 0.1548, 0.1854, 0.1008,
       0.1007, 0.0870, 0.0942, 0.0545, 0.1500, 0.1253, 0.1320, 0.1048, 0.2498]

import matplotlib.pyplot as plt
import json

fileName = './work_dirs/work_dirs/yolo_1/20201023_175746.log_write.json' # mAP = 0

# fileName = './work_dirs/work_dirs/yolo1/20201023_175746.log.json'
input_file = open(fileName)
json_array = json.load(input_file)

losses = []
loss_5th = []
i = 0
for index in range(len(json_array)):
    item = json_array[index]
    i += 1
    if item['mode'] != 'val':
        loss_5th.append(item['loss'])
        losses.append(loss_5th[-1])
        # if len(loss_5th) == 5:
            # losses.append(loss_5th[-1])
            # loss_5th = []

    print(i)

plt.plot(losses)
plt.title('Loss Chart')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()
