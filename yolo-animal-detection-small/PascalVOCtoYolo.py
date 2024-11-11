import os
import xml.etree.ElementTree as ET

# Pascal VOC to YOLO conversion function
def convert_bbox(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# Path to your dataset
xml_folder = 'C:/Users/ken50/OneDrive/桌面/yolo-animal-detection-small/test'  # 這是存放 xml 文件的資料夾路徑
txt_folder = 'C:/Users/ken50/OneDrive/桌面/yolo-animal-detection-small/test'  # 這是存放轉換後的 txt 標籤的資料夾路徑

# Make sure the folder for txt files exists
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)

# Replace class names with your actual class names, same order as in your YAML file
classes = ["cat", "monkey", "dog"]  # 你的類別名稱

for file in os.listdir(xml_folder):
    if file.endswith(".xml"):
        # Parse XML file
        tree = ET.parse(os.path.join(xml_folder, file))
        root = tree.getroot()

        # Get image size
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        # Create a corresponding .txt file
        txt_file = os.path.join(txt_folder, file.replace('.xml', '.txt'))

        with open(txt_file, 'w') as out_file:
            # Iterate over all objects (bounding boxes) in the XML
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in classes:
                    continue
                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                     float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
                bbox = convert_bbox((w, h), b)
                out_file.write(f"{cls_id} {' '.join([str(a) for a in bbox])}\n")
        print(f"Converted {file} to YOLO format.")
