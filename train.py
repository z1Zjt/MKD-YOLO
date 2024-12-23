import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('/data1/zz1jt/ultralytics-main/ultralytics/cfg/models/v8/yolov8n.yaml')  
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='/data1/zz1jt/ultralytics-main/dataset/', # The path of your own dataset
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=10,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                patience=50,
                project='runs/train',
                name='yolov8n',
                )
