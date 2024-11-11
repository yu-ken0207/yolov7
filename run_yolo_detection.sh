#!/bin/bash

# 無窮迴圈執行
while true; do

    # 刪除舊的影像檔案
    rm -f /home/ken/Desktop/program/yolov7/image.png

    # 使用 ffmpeg 擷取影像
    ffmpeg -f v4l2 -i /dev/video0 -vf fps=20 -update 1 /home/ken/Desktop/program/yolov7/image.png

    # 暫停 5 秒
    # sleep 5

    # 使用 YOLOv7 進行物件偵測 設定輸出資料夾
    ~/anaconda3/envs/yolov7/bin/python detect.py --weights /home/ken/Desktop/program/yolov7/runs/train/exp17/weights/best.pt --conf 0.25 --img-size 640 --source /home/ken/Desktop/program/yolov7/image.png --project /home/ken/Desktop/program/yolov7/runs/detect --name result

    # Bash 自動開啟影像
    xdg-open /home/ken/Desktop/program/yolov7/runs/detect/result/image.png

done
