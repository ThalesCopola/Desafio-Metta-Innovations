import tkinter as tk       
from tkinter import ttk
from PIL import Image, ImageTk          
import cv2          
import json             
import matplotlib.pyplot as plt             
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils import ensure_dir_exists, save_json, draw_boxes          



class VideoApp(tk.Tk):             
    def __init__(self, video_path, history_path):          
        super().__init__()         
        self.title("Visualizador de Detecção")         
        self.geometry("900x600")            
        
        self.cap = cv2.VideoCapture(video_path)         
        self.history = self.load_history(history_path)        
        self.frame_id = 0               
        self.playing = False           

        
        
        self.video_label = ttk.Label(self)          
        self.video_label.pack()             
        
       
        self.count_label = ttk.Label(self, text="Pessoas: 0", font=("Arial", 14))         
        self.count_label.pack(pady=10)             
        
        
        self.play_button = ttk.Button(self, text="Play", command=self.toggle_play)         
        self.play_button.pack(pady=5)           
        
        
        self.fig, self.ax = plt.subplots(figsize=(10, 4))           
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)         
        self.canvas.get_tk_widget().pack()         

        self.plot_graph()           
        self.update_frame()             
        self.protocol("WM_DELETE_WINDOW", self.on_close)      


    def load_history(self, path):           
        with open(path, "r") as f:
            return json.load(f)
    
    def plot_graph(self):              
        ids = [h["id"] for h in self.history]
        counts = [h["count"] for h in self.history]
        self.ax.clear()                 
        self.ax.plot(ids, counts, label="Pessoas no Frame")
        self.ax.set_xlabel("Frame")
        self.ax.set_ylabel("Número de Pessoas")
        self.ax.set_title("Contagem de Pessoas por Frame")
        self.ax.legend()
        self.ax.grid(True)

        
        self.ax.set_xlim(0, max(ids) if ids else 1)     
        max_count = max(counts) if counts else 1
        self.ax.set_ylim(0, max_count + 1)

        self.canvas.draw()          

    def update_frame(self):             
        if self.playing:
            ret, frame = self.cap.read()
            if not ret:             
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                self.frame_id = 0
                ret, frame = self.cap.read()
            if ret:                 
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)          
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)            
                
                
                count = self.history[self.frame_id]["count"]            
                self.count_label.config(text=f"Pessoas: {count}")
                self.frame_id += 1
        
        self.after(30, self.update_frame)       
    
    def toggle_play(self):          
        self.playing = not self.playing    
        self.play_button.config(text="Pause" if self.playing else "Play")              

    def on_close(self):             
        self.playing = False
        self.destroy()

if __name__ == "__main__":                  
    app = VideoApp("output_results/video_out.mp4", "output_results/history.json")
    app.mainloop()          