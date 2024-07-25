# Aptus Video Analytics Sample YOLOv8 Flask API

## Requirements

- Create a python virtual environment

```bash
$ python3 -m venv venv
```

- Activate the virtual environment

```bash
$ source venv/bin/activate
```

- Install all dependacies in the requirements file:

```bash
$ pip3 install -r requirements.txt
```

## Usage

- For serving the API with GPU:

```bash
$ python server.py --weights yolov8s.pt    # Object detection
```

- For serving the API with CPU:

```bash
$ python server.py --weights yolov8s.pt    --device cpu
```

By default the api will be available to interact in [0.0.0.0:8000](0.0.0.0:8000)

- To change the port to <PORT>:

```bash
$ python server.py --weights yolov8s.pt    --device cpu --port <PORT>
```

- To interact from a python client

```python
import requests

resp = requests.get("http://0.0.0.0:8000/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg&save_txt=T",
                    verify=False)
print(resp.content)

```

## API Response

- Model api resposne will be a json of the form:

```
b'{"results": [{"name": "person", "class": 0, "confidence": 0.9490957260131836, "box": {"x1": 239.0, "y1": 15.0, "x2": 1018.0, "y2": 1053.0}, "keypoints": {"x": [604.9951782226562, 653.2091064453125, 552.5707397460938, 697.6889038085938, 457.49749755859375, 786.6876831054688, 358.194091796875, 954.072998046875, 488.3907775878906, 684.831298828125, 802.8469848632812, 687.2332153320312, 412.4287414550781, 924.52685546875, 632.3346557617188, 811.2559814453125, 768.5433349609375], "y": [316.5501403808594, 260.7156066894531, 257.27691650390625, 291.1667175292969, 285.6615905761719, 566.11962890625, 596.4549560546875, 909.6119384765625, 965.7925415039062, 997.584716796875, 841.6057739257812, 1066.0, 1066.0, 850.1934204101562, 812.7511596679688, 954.5965576171875, 951.3284912109375], "visible": [0.9959749579429626, 0.9608340859413147, 0.9934138655662537, 0.4281827211380005, 0.9349473118782043, 0.9848191738128662, 0.9723504185676575, 0.8565006852149963, 0.8561225533485413, 0.9004713296890259, 0.9377612471580505, 0.10934382677078247, 0.08168646693229675, 0.008380762301385403, 0.008864155039191246, 0.0017155600944533944, 0.001865472993813455]}}]}'
```
