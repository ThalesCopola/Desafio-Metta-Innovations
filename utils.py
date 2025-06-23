import os     
import json         
import cv2     

def ensure_dir_exists(path):            
    if not os.path.exists(path):
        os.makedirs(path)

def save_json(data, filepath):         
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def draw_boxes(frame, boxes, color=(0, 255, 0), thickness=2):          
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
        