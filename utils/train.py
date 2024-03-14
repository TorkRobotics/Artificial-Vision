from ultralytics import YOLO

def run():
    model = YOLO('yolov8m.pt')
    
    data_dir = input("Enter data.yaml route: ")
    print('Training model from data: {0}'.format(data_dir))
    results = model.train(data=data_dir, epochs=100, imgsz=640, device=0)