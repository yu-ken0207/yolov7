# 刪除舊的影像檔案
exec rm -f /home/ken/Desktop/program/yolov7/image.png

# 使用 ffmpeg 擷取影像
exec ffmpeg -f v4l2 -i /dev/video2 -vf fps=20 -update 1 image.png 2>&1

# 暫停 5 秒
exec sleep 5

# 使用 YOLOv7 進行物件偵測
exec ~/anaconda3/envs/yolov7/bin/python detect.py --weights /home/ken/Desktop/program/yolov7/runs/train/exp17/weights/best.pt --conf 0.25 --img-size 640 --source /home/ken/Desktop/program/yolov7/image.png
