# AI-AirWriter
A real-time AI-powered hand gesture recognition system that allows users to write in the air using their fingers. Ideal for speech-impaired individuals to communicate easily during video calls.  

# AI AirWriter: Silent Communication for Video Calls ✍️🎥  

AI-powered real-time hand gesture recognition system that allows users to **write in the air using their fingers**. This project helps people who cannot talk communicate easily during video calls.  

---

Features  
 **Write in the Air** – Move your index finger to write on the screen.  
 **Lift to Stop Writing** – Writing stops when the finger is lifted.  
 **Real-time Hand Tracking** – Uses OpenCV and MediaPipe for accurate gesture recognition.  
 **Non-Verbal Communication** – Ideal for speech-impaired individuals.  
 **Clear & Reset** – Press **'C'** to clear the screen.  
 **Easy Exit** – Press **'Q'** to quit the app.  

---

Install Dependencies

 ->pip install opencv-python mediapipe numpy
Run application

->python air_writer.py

Key controls:

Key      	Action
C	     Clear the screen
Q	     Quit the application

How It Works:
Tracks Hand Gestures – Detects the index finger and thumb positions.
Writing Gesture – If the index finger touches the thumb, writing starts.
Lifting Finger – When the finger is lifted, writing stops.
Draws on a Virtual Canvas – The movements are stored and displayed in real-time.

Technologies Used
Python 
OpenCV 
MediaPipe 
NumPy 
