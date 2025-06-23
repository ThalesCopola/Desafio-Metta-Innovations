import os          
import sys          
import json         
import cv2          
from ultralytics import YOLO            
from utils import ensure_dir_exists, save_json, draw_boxes        



class PersonDetector:       
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)       
    
    def detect_people(self, frame):    
        results = self.model(frame)[0]  
        people_boxes = [box for box in results.boxes if int(box.cls) == 0]  
        return people_boxes


class VideoProcessor:       
    def __init__(self, video_path, alert_limit, output_dir="output_results"):
        self.video_path = video_path
        self.alert_limit = alert_limit
        self.output_dir = output_dir
        ensure_dir_exists(self.output_dir)  
        
        self.cap = cv2.VideoCapture(self.video_path)        
        if not self.cap.isOpened():
            raise IOError(f"Não abriu o vídeo: {self.video_path}")
        
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))        
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        
        
        self.out = cv2.VideoWriter(         
            os.path.join(self.output_dir, "video_out.mp4"),
            cv2.VideoWriter_fourcc(*'mp4v'),
            self.fps,
            (self.width, self.height)
        )
        
        self.detector = PersonDetector()       
        self.history = []  
        self.alerts = []   
    
    def process(self):              
        frame_id = 0
        while True:
            ret, frame = self.cap.read()        
            if not ret:
                break  
            
            people_boxes = self.detector.detect_people(frame)   
            draw_boxes(frame, people_boxes)  
            
            count = len(people_boxes)       
            self.history.append({"id": frame_id, "count": count})
            
            
            if count >= self.alert_limit:          
                self.alerts.append({"id": frame_id, "count": count})
            
            self.out.write(frame)   
            frame_id += 1
        
        self.cap.release()
        self.out.release()
    
    def save_results(self):         
        
        save_json(self.history, os.path.join(self.output_dir, "history.json"))
        save_json(self.alerts, os.path.join(self.output_dir, "alerts.json"))
        
        print(f"Resultados salvos na pasta '{self.output_dir}'.")


def main(video_path, alert_limit):      
    processor = VideoProcessor(video_path, alert_limit)
    processor.process()
    processor.save_results()


if __name__ == "__main__":          
    if len(sys.argv) < 3:
        print("Use: python detector.py <video> <limite>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))