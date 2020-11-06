# Second step
from mmdet.apis import init_detector, inference_detector, show_result_pyplot

config_file = '../configs/new_nn/yolo.py'
checkpoint_file = '../work_dirs/yolo_1/latest.pth'
filename = '../../video_for_training/validation.txt'
image_folder = '/home/duy/Documents/mmdetection/2bbox/'

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
array = []

for element in content:
    if str(element[-3:]) == 'png':
        array.append(image_folder + element[-16:])

model = init_detector(config_file, checkpoint_file, device='cuda:0')

i = 0
for frame in array:
    i += 1
    result = inference_detector(model, frame)
    show_result_pyplot(frame, model, frame, result)
