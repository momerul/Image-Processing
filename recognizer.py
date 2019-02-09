import cv2, numpy as np;
import os;
import firebase
import xlwrite;
from playsound import playsound

#import firebase_admin;
#import firebase.firebase_ini as fire;
import time
OPENCV_VIDEOIO_PRIORITY_MSMF = 0
start=time.time()
period=100
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');

id=0;

filename='filename';
dict = {
            'item1': 1
}
#font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id,conf=recognizer.predict(roi_gray)
        
        if(id==1):
            id= '1'
            name ='Jannat'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',1, name, id,'Yes');
                dict[str(id)]=str(id);
        
        if(id==2):
            id= '2'
            name='Asik Syed'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',2, name, id,'Yes');
                dict[str(id)]=str(id); 
                     
        if(id==3):
            id= '3'
            name='Mizan'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',3, name, id,'Yes');
                dict[str(id)]=str(id); 

        if(id==4):
            id= '4'
            name = 'Momerul'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 4, name, id, 'Yes');
                dict[str(id)] = str(id);
                
        if(id==5):
            id= '5'
            name = 'Iabur'
            if ((str(id)) not in dict):
                filename =xlwrite.output('attendance', 'class1', 5, name, id, 'Yes');
                dict[str(id)] = str(id);
                
                                   
        if(id==6):
            id= '6'
            name='Imtiaj '
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',6, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==7):
            id= '7'
            name='Chamak '
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',7, name, id,'Yes');
                dict[str(id)]=str(id);
         
                 
        if(id==8):
            id= '8'
            name='Labib'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',8, name, id,'Yes');
                dict[str(id)]=str(id);
                
                
        if(id==9):
            id= '9'
            name='Akib'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',9, name, id,'Yes');
                dict[str(id)]=str(id);
                
                
        if(id==10):
            id= '10'
            name='Muaz'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',10, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==11):
            id= '11'
            name='Joarddar'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',11, name, id,'Yes');
                dict[str(id)]=str(id);   
                
        if(id==12):
            id= '12'
            name='Robayed'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',12, name, id,'Yes');
                dict[str(id)]=str(id);
        
        if(id==13):
            id= '13'
            name='Mahmud'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',13, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==14):
            id= '14'
            name='Minhaz'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',14, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==15):
            id= '15'
            name='Anik'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',15, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==16):
            id= '16'
            name='Wasim'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',16, name, id,'Yes');
                dict[str(id)]=str(id);
                
                
        if(id==17):
            id= '17'
            name='Ferdous'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',17, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==18):
            id= '18'
            name='Fahim'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',18, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==19):
            id= '19'
            name='Partha'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',19, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==20):
            id= '20'
            name='Musfiq'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',20, name, id,'Yes');
                dict[str(id)]=str(id);
       
        if(id==21):
            id= '21'
            name='Tithir'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',21, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==22):
            id= '22'
            name='Ony'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',22, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==23):
            id= '23'
            name='Miad'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',23, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==24):
            id= '24'
            name='Sharmin'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',24, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==25):
            id= '25'
            name='Tanvir'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',25, name, id,'Yes');
                dict[str(id)]=str(id);
        
        if(id==26):
            id= '26'
            name='Hemayet'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',26, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==27):
            id= '27'
            name='Sayed'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',27, name, id,'Yes');
                dict[str(id)]=str(id);
        
        if(id==28):
            id= '28'
            name='Ananda'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',28, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==29):
            id= '29'
            name='Mosarraf'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',29, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==30):
            id= '30'
            name='Ornob'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',30, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==31):
            id= '31'
            name='Kamal'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',31, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==32):
            id= '32'
            name='Tapan'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',32, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==33):
            id= '33'
            name='Farhana'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',33, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==34):
            id= '34'
            name='Shanu'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',34,name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==35):
            id= '35'
            name='Himel'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',35,name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==36):
            id= '36'
            name='Taiyeba'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',35,name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==37):
            id= '37'
            name='Sinthia'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',37,name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==38):
            id= '38'
            name='Dipu'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',38,name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==39):
            id= '39'
            name='Farhana'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',39,name, id,'Yes');
                dict[str(id)]=str(id);
                    
        if(id==40):
            id= '40'
            name='Rimon'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',40, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==41):
            id= '41'
            name='Shahadat'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',41, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==42):
            id= '42'
            name='Somiah'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',42, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==43):
            id= '43'
            name='Nihal'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',43, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==44):
            id= '44'
            name='Arif'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',44, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==45):
            id= '45'
            name='Lizur'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',45, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==46):
            id= '46'
            name='Khadeja'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',46, name, id,'Yes');
                dict[str(id)]=str(id);
        
        if(id==47):
            id= '47'
            name='Sayket'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',47, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==48):
            id= '48'
            name='Amit Roy'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',48, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==49):
            id= '49'
            name='Fahim Talha'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',49, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==50):
            id= '50'
            name='Khabbab'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',50, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==51):
            id= '51'
            name='Ashik Mahmud'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',51,name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==52):
            id= '52'
            name='Olip'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',52, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==53):
            id= '53'
            name='Sohan'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',53, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==54):
            id= '54'
            name='Solaiman Rajon'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',54, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==55):
            id= '55'
            name='Akash'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',55, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==56):
            id= '56'
            name='Shitul'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',56, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==57):
            id= '57'
            name='Shotej'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',57, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==58):
            id= '58'
            name='Nusrat'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',58, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==59):
            id= '59'
            name='Heemel'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',59, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==60):
            id= '60'
            name='Taskeed Jabid'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',60, name, id,'Yes');
                dict[str(id)]=str(id);
                
        if(id==61):
            id= '61'
            name='Monir'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',61, name, id,'Yes');
                dict[str(id)]=str(id);
                
        #show frame recognizing you with your name + confidence
        #cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
        
        #show reconized frame mentioning your name
        cv2.putText(img,str(name),(x,y-10),font,0.55,(120,255,120),1)

    cv2.imshow('frame',img);
    

    #cv2.imshow('gray',gray);
    if time.time()>start+period:
        break;
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break;
print("Successfully Written")
playsound('thankyou.flv')

cap.release();
cv2.destroyAllWindows();
