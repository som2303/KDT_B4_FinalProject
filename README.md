# 네모네모 고등학교 졸업식  
## Description
네모네모 고등학교 졸업식은 사용자로부터 받은 이미지를 픽셀 캐릭터로 변환시켜주는 프로젝트입니다.  
각종 api와 딥러닝 모델을 통해 원본 사진에서 표정, 얼굴 비율, 얼굴과 머리 색상, 머리 스타일, 안경 유무 등을 파악하여 다양한 캐릭터를 만들 수 있습니다. 

## Member
이영준[@YJJonatanLee](https://github.com/YJJonatanLee)  
임동윤[@spade8](https://github.com/spade8)  
주소미[@som2303](https://github.com/som2303)  
김보섭[@platypus46](https://github.com/platypus46)  
## Example
![그림1](https://user-images.githubusercontent.com/37619294/220820041-a83cdf27-ad68-4ea0-a799-0e3d586fed2a.png)  

## Demonstration video
![1 5배속_](https://user-images.githubusercontent.com/37619294/220817790-fdc1037e-c3b8-45d7-86d7-f310f91f9e89.gif)


## Tools
 - <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
 - <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/>
 - <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
 - <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white"/>
 - <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>
 - <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
 - <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
 

## Models
| 기준 | 모델 | 분류 |
|--|--|--|
| 헤어 스타일 | EfficientNet | 11((웨이브)긴머리, (웨이브)단발머리, (웨이브)숏컷, 포니테일, 양갈래, 양갈래, 땋은머리, 대머리)  |
| 앞머리 스타일 | shufflenet v2 | 4(덮은 머리, 깐머리, 반깐머리, 가르마 머리) |
| 안경 | Mobilenet v2 | 2 |
| 표정 | Naver api(face recognition) | 5(기본, 슬픔, 기쁨, 무표정, 신남) |
| 얼굴 비율 | Naver api(face recognition) | 3 |
| 색상 | Naver api(face recognition) | 얼굴: 9, 헤어: 추출된 색상 |


<p align="center">
  <img src="https://user-images.githubusercontent.com/37619294/220816228-3a91ba96-d001-4f83-be31-bf319143c266.png" align="center" width="49%">
  <img src="https://user-images.githubusercontent.com/37619294/220816258-961b96b6-b56e-4ac6-9608-b31409b08671.png" align="center" width="49%">
  <figcaption align="center">
</p>


## Prototype

![캡처](https://user-images.githubusercontent.com/89053845/219292003-f3501e10-e1bc-4cf3-887a-6e79addb311d.PNG)

## [Files](https://github.com/YJJonatanLee/KDT_B4_FinalProject/wiki/Files)
[finalproject](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject)   
│  
├─ [b4](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4)    
│ ├─ migrations  
│ ├─ static  
│ │ └─ [b4](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4)  
│ │ │ ├─ [css](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4/css)  
│ │ │ ├─ [img](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4/img)  
│ │ │ │ ├─ [character](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4/img/character)  
│ │ │ │ │ ├─ face0  
│ │ │ │ │ ├─ face1  
│ │ │ │ │ └─ face2  
│ │ │ │ └─ [icon](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4/img/icon)  
│ │ │ ├─ [js](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4/js)     
│ │ │ └─ [models](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/b4/static/b4/models)     
│  
├─ media  
│ ├─ background   
│ │ └─ media  
│ │ │ └─ test     
│ ├─ converted  
│ │ └─ media  
│ │ │ └─ test  
│ ├─ origin  
│ ├─ origin_img  
│ └─ test     
└─ [templates](https://github.com/YJJonatanLee/KDT_B4_FinalProject/tree/main/finalproject/templates)   

## Usages
어떻게 사용하면 되는지에 대한 설명  
 
0. git clone

1. 가상환경 설치
```python
sudo pip install virtualenv
virtualenv venv
```

2. media 폴더 구축  


3. 네이버 api 관련 json 파일 설치
finalproject 하위 파일로 secrets.json파일을 작성해 주세요.
네이버 api는 [해당 사이트](https://developers.naver.com/docs/clova/api/CFR/API_Guide.md)를 확인해주세요.
```python
    {
        "Naver_id": "Client ID",
        "Naver_secret": "Client Secret"
    }
```

4. Django 가상환경 activate
```python
source venv/bin/activate
```

5. migrate 실행
```python
python manage.py migrate
python manage.py makemigrations
```

6. Django 서버 실행
```python
python manage.py runserver
```

## requirements
asgiref==3.6.0  
certifi==2022.12.7  
charset-normalizer==3.0.1  
Django==4.1.5  
django-cleanup==6.0.0  
django-social-share==2.3.0  
idna==3.4  
numpy==1.24.1  
opencv-python==4.7.0.68  
Pillow==9.4.0  
requests==2.28.2  
sqlparse==0.4.3  
torch==1.13.1  
torchvision==0.14.1  
typing_extensions==4.4.0  
urllib3==1.26.14
