## 커뮤니티마스터 BackEnd

커뮤니티 마스터 백엔드 프로젝트 입니다.

## 프로젝트 설정

1.  프로젝트 폴더 생성
2.  git 내려받기

        $ git clone https://github.com/cuma-master/cuma-BE.git

3.  Poetry 설치

        $ pip install poetry==1.8.5

4.  프로젝트 의존성 설치

        $ poetry install

5.  가상환경 진입

        $ poetry shell

6.  프로젝트 실행

        $ python run.py

7.  가상환경 종료

        $ exit

## swagger 접속 방법

url : http://localhost:5000/docs

## 주의점

- 컨벤션 지키기
- .env 파일 생성하기
- pycache 폴더 push 금지
- main branch 에서 작업 금지
