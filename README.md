
# Car-License-Plate-Recognition

License plate recognition technology is very useful in many fields. In parking lot management, this system automatically recognizes and records vehicle license plates, making management easier and less arduous. At automatic toll stations, this technology allows vehicles to pass through the station without stopping, reducing traffic congestion. In security and surveillance, license plates assist in tracking suspect vehicles, assisting in criminal investigations and searching for stolen vehicles...

<p align="center">
<a href="https://www.youtube.com/watch?v=ul1J0IiHU-k">
    <img width="600" src="https://github.com/user-attachments/assets/80a04961-84c5-428d-bf0e-d36d53031ef5" alt="Watch the video">
    </br>Watch on YouTube: Automatic number plate recognition with Python, Yolov8 and EasyOCR !
</a>
</p>

## Training Process and Data

A `Yolov8` pretrained model was used to detect vehicles.

A licensed plate detector was used to detect license plates. The model was trained with Yolov8 using [this dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

Dataset Split:

   | TRAIN SET (87%) |  VALID SET (8%) | TEST SET (4%) |
   |-----------------|-----------------|---------------|
   |   **21174** Images  |    **2048** Images  |  **1020** Images  |

Preprocessing:

- **Auto-Orient:** Applied
  
- **Resize:** Stretch to 640x640

<p align="left">
  <img src="https://github.com/user-attachments/assets/1dc809f1-9eed-4859-9186-0b6cd270fbee" width="400" height="250">
  <img src="https://github.com/user-attachments/assets/9aeb0bc8-8fb7-42bd-9cc4-71693db93936" width="400" height="250">
  <img src="https://github.com/user-attachments/assets/331f2628-e1fc-4703-9198-44b424f789e9" width="400" height="250">
  <img src="https://github.com/user-attachments/assets/af0e7ae0-63f8-444e-8028-64ed8b1b381d" width="400" height="250">
</p>

![image](https://github.com/user-attachments/assets/2ea74a29-5054-44d9-b537-8576677c2283)


## Implement license plate classification in Vietnam

**I have done the formatting with Vietnamese car license plates as follows:**

Divide license plates into two types and what they have in common is that they all have 8 characters formatted as follows:

In which, X(0,1,2,...9) is a number and Y(A,B,C,...Z) is a letter

- Type of plate 1: License plate is on one line

  XXY-XXX.XX

- Type of license plate 2: License plate is located on two lines

  XXY

  XXX.XX

## Results achieved when formatting Vietnamese license plates

**Results of car identification with Yolov8**

![image](https://github.com/user-attachments/assets/67acfcbc-3226-4015-8269-cb08ea99d3ea)


**Results of vehicle license plate recognition with Yolov8**

![image](https://github.com/user-attachments/assets/8301ae54-50da-4d87-a6dc-b61198b6f9fa)


**Handling one-line format license plates**

<p align="left">
  <img src="https://github.com/user-attachments/assets/4ede80a1-2b69-428c-9105-46941b801ada" width="250" height="200">
  <img src="https://github.com/user-attachments/assets/fae0d644-65b9-4c2e-8e8c-e0482b10feca" width="250" height="200">
  <img src="https://github.com/user-attachments/assets/98dd461f-67bb-4806-b8d3-3a54ac42b881" width="250" height="200">
</p>

**Handling two-line format license plates**

<p align="left">
  <img src="https://github.com/user-attachments/assets/bc0f9075-59f5-4612-9f95-5e2f48478984" width="250" height="200">
  <img src="https://github.com/user-attachments/assets/45ae0a83-9919-420e-897e-1f631028de19" width="250" height="200">
  <img src="https://github.com/user-attachments/assets/c2298c08-c59b-4492-9435-f8a4e67975d8" width="250" height="200">
</p>

**For license plates with a yellow background, the license plate cannot be processed until the final step only leaves a black color. This is really bad, it makes reading the license plate unsuccessful**

<p align="left">
  <img src="https://github.com/user-attachments/assets/1e4bc0ac-0e48-4dac-81db-dc9fcf29b788" width="250" height="200">
  <img src="https://github.com/user-attachments/assets/c1ab4cfe-0623-4442-a735-ca1e039b914d" width="250" height="200">
  <img src="https://github.com/user-attachments/assets/161b2a2b-b0b5-4613-bea7-6b70a4b0ad9e" width="250" height="200">
</p>

**In low light or too strong light, the license plate will appear as shown**

<p align="left">
  <img src="https://github.com/user-attachments/assets/e6f1385b-8977-4fce-a039-8df50e68ae04" width="250" height="200">
</p>




## Car-License-Plate-Recognition Installation Instructions

### Prerequisites
Before you begin, ensure you have the following software installed:

1. [Python version 3.12](https://www.python.org/)
   - Workload: `Python`
     
2. Library: ultralytics, pandas, opencv-python, numpy, scipy, easyocr, filterpy

3. Sort: The sort module needs to be downloaded from [this repository](https://github.com/abewley/sort)

4. Nếu bb_test hoặc bb_gt trống, trả về một mảng rỗng

```python
if bb_test.size == 0 or bb_gt.size == 0:
    return np.zeros((bb_test.shape[0], bb_gt.shape[0]))
```

### Step-by-Step Installation Guide

**Step 1.** Clone the Repository

   First, clone the repository containing the application source code.

   ```bash
   git clone github.com/anhhducnguyen/Car-License-Plate-Recognition
   ```

**Step 2.** Install the necessary libraries in `requirements.txt`

   ```
   pip install -r requirements.txt
   ```

**Step 3.** Download Yolov8 model at [yolov8n]() and license plate recognition model at [license plate detector](), then move it to the `models` folder in the project

**Step 4.** Download the video I used for testing at [sample video](), then transfer it to the project


**Step 5.** Run program `main.py`

 ```bash
 python main.py 
 ```

**Step 6.** Run program `add_missing_data.py`

 ```bash
 python add_missing_data.py 
 ```

**Step 7.** Run program `visualize.py`

 ```bash
 python visualize.py 
 ```


## <div align="left">Contact</div>

To report bugs and request features of software, please contact me for questions and discussion!

<br>
<div align="center">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="#"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
