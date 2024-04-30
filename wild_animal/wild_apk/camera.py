from imutils.video import VideoStream
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from wild_apk.database import*
import time
# from pushbullet import PushBullet
from twilio.rest import Client
account_ssid= 'ACdd3512333ec4948a214534e56cce6633'
auth_token = 'f3ea80431b4b92718e846defab36c0ab'
Client= Client(account_ssid, auth_token)

import threading
# from DBConnection import Db
# cap = cv2.VideoCapture('C:\\Users\\IDZ\\OneDrive\\Desktop\\Early Warning\\Warning_System\\animal.mp4')
def cam(id):
    # print("sdfghjkl;",aa)
    # path = aa.replace("\\", "\\\\") 
    
    # cap = cv2.VideoCapture(path)
    # cap = cv2. VideoCapture('C:\\RISS_PROJECTS\\Wild_Animal\\Web\\static\\animal.mp4')

    cap = cv2.VideoCapture(0)
    #get framerate of given video
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    second_completed = 0
    twillio_phno='+18583814080'
    recipent_no='+917558969793'

    #detection of video
    i=0
    while(True):
        #read every frame
        success, image_np = cap.read()
        if not success:
            print ('>>>>>  End of the video file...')
            break
        frame_count += 1
        #check if this frame is closed to time interval provided
        if frame_count == (2 * frame_rate):
            second_completed += 2
            print('>>>>>' + str(second_completed))
            frame_count = 0
            # cv2.imwrite("C:\\Users\\IDZ\\OneDrive\\Desktop\\Early Warning\\Warning_System\\pic.jpg",image_np)
            cv2.imwrite("C:\\Users\\abhij\\OneDrive\\Desktop\\wild_animal\\static\\pic2.png",image_np)

            # image_data = tf.gfile.FastGFile("C:\\Users\\IDZ\\OneDrive\\Desktop\\Early Warning\\Warning_System\\pic.jpg",
            image_data = tf.gfile.FastGFile("C:\\Users\\abhij\OneDrive\\Desktop\\wild_animal\\static\\pic2.png",
                                            'rb').read()

            # Loads label file, strips off carriage return
            label_lines = [line.rstrip() for line
                        in tf.gfile.GFile("logs/output_labels.txt")]

            # Unpersists graph from file
            with tf.gfile.FastGFile("logs/output_graph.pb", 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                _ = tf.import_graph_def(graph_def, name='')

            with tf.Session() as sess:
                # Feed the image_data as input to the graph and get first prediction
                softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

                predictions = sess.run(softmax_tensor, \
                                    {'DecodeJpeg/contents:0': image_data})

                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

                # for node_id in top_k:
                #     human_string = label_lines[node_id]
                #     score = predictions[0][node_id]
                #     print('%s (score = %.5f)' % (human_string, score))

                animal = label_lines[top_k[0]]
                print(animal, predictions[0][top_k[0]],"////////////////")
                # db = Db()
                # res = db.selectOne("select * from animals where animal_name='" + animal + "'")
                # print(res)
                # if res is not None:
                #     ani=res['animal_id']
                #     print("aaa",ani)
                #     db.insert("insert into alert values('','" + str(ani) + "',now())")
                
                ab=['elephant','tiger','lion','cheetah',' hyenas','crocodile','rhinoceros','leopard','hippopotamus']
                insert_interval = 60    
                
                for i in ab:
                    if animal==i:
                        image_name ="media/"+f"image_{animal}.png"
                        cv2.imwrite(image_name,image_np)
            
                        print(image_name,".......////////////q/////////")
                        print("detected")
                        
                        
                        qry = "insert into wild_apk_alert values(null,'%s',curdate(),'%s',curtime(),'%s')" % (animal, "/" + image_name, id)
                        insert(qry)
                        # pb = PushBullet('o.Hf01vuJf3GqNvqFUrZGc9uPRBXzzJXnm')
                        # push = pb.push_note("WG Alert","Wild animal detected near your area")
                        message_body = 'Wild Guard Alert; '+animal+ ' detected near your area'


                        message= Client.messages.create(body=message_body,from_=twillio_phno,to=recipent_no)
                        print ('Alert message Sented. sid:', message.sid)

                        
                        def schedule_function(interval):
                            while True:
                                cap()
                                time.sleep(interval)
                                interval_minutes = 1
                                interval_seconds = interval_minutes * 60
                                thread = threading.Thread(target=schedule_function, args=(interval_seconds,))
                                thread.daemon = True  # This will make the thread exit when the main program finishes
                                thread.start()
                                try:
                                    while True:
                                        time.sleep(1)
                                except KeyboardInterrupt:
                                    print("Main program terminated.")
        cv2.imshow("Frame", image_np)
        key = cv2.waitKey(1) & 0xFF
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # if key == ord('x') or cv2.getWindowProperty("Frame",cv2.WND_PROP_VISIBLE) < 1:
        #     break
    print("persons identified")

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

