#[ip82]顔検出プログラム
import cv2
import numpy as np

device = 0

def main():
  face_cascade = cv2.CascadeClassifier("./learned_models/haarcascades/haarcascade_frontalface_default.xml")
  eye_cascade = cv2.CascadeClassifier("./learned_models/haarcascades/haarcascade_eye.xml")

  cap = cv2.VideoCapture(device)

  fps = cap.get(cv2.CAP_PROP_FPS)
  print(fps,"fps")

  # プレイヤー初期位置
  player_x = 320

  # 落ち物
  enemy_x1 = np.random.randint(20, 620)
  enemy_y1 = 0
  enemy_x2 = np.random.randint(20, 620)
  enemy_y2 = 0
  enemy_x3 = np.random.randint(20, 620)
  enemy_y3 = 0
  enemy_x4 = np.random.randint(20, 620)
  enemy_y4 = 0
  enemy_x5 = np.random.randint(20, 620)
  enemy_y5 = 0
  
  # 落ちる速度
  enemy_speed1 = 3
  enemy_speed2 = 5
  enemy_speed3 = 7
  enemy_speed4 = 9
  enemy_speed5 = 11

  score=0;
  while cap.isOpened():
    ret, frame = cap.read()
    score = score + 1
    if not ret:
        print("映像を取得できませんでした。")
        break
    
    ######## 顔の検出 ########
    # カスケードを10%ずつ縮小しながら検出，最低何個の近傍矩形を検出すれば採用するか
    faces = face_cascade.detectMultiScale(frame, 1.1, 5)

    # facesの中にある顔と認識した領域を順に取り出す
    for (x, y, w, h) in faces:

        # 顔枠
        cv2 .rectangle(frame, (x, y), (x+w, y+h),(0, 0, 255), 2)

        # 顔の中心座標
        center_x = x + w // 2
        center_y = y + h // 2

        # プレイヤー位置更新
        player_x = center_x
        
        # 中心確認用
        cv2.circle(frame,(center_x, center_y),5,(0, 255, 0),-1)

    # プレイヤー描画
    player_y = 400

    cv2.rectangle(frame,(player_x - 20, player_y - 20),(player_x + 20, player_y + 20),(0, 255, 255),-1)

    # 障害物を落とす
    enemy_y1 = enemy_y1 + enemy_speed1
    enemy_y2 = enemy_y2 + enemy_speed2
    enemy_y3 = enemy_y3 + enemy_speed3
    enemy_y4 = enemy_y4 + enemy_speed4
    enemy_y5 = enemy_y5 + enemy_speed5
    
    # 障害物
    cv2.rectangle(frame,(enemy_x1 - 20, enemy_y1 - 20),(enemy_x1 + 20, enemy_y1 + 20),(0, 0, 255),-1)
    cv2.rectangle(frame,(enemy_x2 - 20, enemy_y2 - 20),(enemy_x2 + 20, enemy_y2 + 20),(0, 0, 255),-1)
    cv2.rectangle(frame,(enemy_x3 - 20, enemy_y3 - 20),(enemy_x3 + 20, enemy_y3 + 20),(0, 0, 255),-1)
    cv2.rectangle(frame,(enemy_x4 - 20, enemy_y4 - 20),(enemy_x4 + 20, enemy_y4 + 20),(0, 0, 255),-1)
    cv2.rectangle(frame,(enemy_x5 - 20, enemy_y5 - 20),(enemy_x5 + 20, enemy_y5 + 20),(0, 0, 255),-1)

    # 当たり判定
    if abs(player_x - enemy_x1) < 40 and abs(player_y - enemy_y1) < 40:
       cv2.putText(frame,"GAME OVER",(150, 200),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 0, 255),3)
       cv2.putText(frame,"Score : " + str(score),(170, 250),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),3)
       cv2.imshow("video", frame)
       cv2.waitKey(3000)
       break
    
    if abs(player_x - enemy_x2) < 40 and abs(player_y - enemy_y2) < 40:
       cv2.putText(frame,"GAME OVER",(150, 200),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 0, 255),3)
       cv2.putText(frame,"Score : " + str(score),(170, 250),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),3)
       cv2.imshow("video", frame)
       cv2.waitKey(3000)
       break
    
    if abs(player_x - enemy_x3) < 40 and abs(player_y - enemy_y3) < 40:
       cv2.putText(frame,"GAME OVER",(150, 200),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 0, 255),3)
       cv2.putText(frame,"Score : " + str(score),(170, 250),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),3)
       cv2.imshow("video", frame)
       cv2.waitKey(3000)
       break
    
    if abs(player_x - enemy_x4) < 40 and abs(player_y - enemy_y4) < 40:
       cv2.putText(frame,"GAME OVER",(150, 200),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 0, 255),3)
       cv2.putText(frame,"Score : " + str(score),(170, 250),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),3)
       cv2.imshow("video", frame)
       cv2.waitKey(3000)
       break
    
    if abs(player_x - enemy_x5) < 40 and abs(player_y - enemy_y5) < 40:
       cv2.putText(frame,"GAME OVER",(150, 200),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 0, 255),3)
       cv2.putText(frame,"Score : " + str(score),(170, 250),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),3)
       cv2.imshow("video", frame)
       cv2.waitKey(3000)
       break

    # 下まで行ったら戻す
    if enemy_y1 > 480:
       enemy_y1 = 0
       enemy_x1 = np.random.randint(20, 620)

    if enemy_y2 > 480:
       enemy_y2 = 0
       enemy_x2 = np.random.randint(20, 620)

    if enemy_y3 > 480:
       enemy_y3 = 0
       enemy_x3 = np.random.randint(20, 620)
    
    if enemy_y4 > 480:
       enemy_y4 = 0
       enemy_x4 = np.random.randint(20, 620)

    if enemy_y5 > 480:
       enemy_y5 = 0
       enemy_x5 = np.random.randint(20, 620)

   
    # スコア
    cv2.putText( frame,"Score : " + str(score),(10, 40),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)


    cv2.imshow("video", frame)


    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
      break


  cv2.destroyAllWindows()
  cap.release()

if __name__ == '__main__':
  main()
