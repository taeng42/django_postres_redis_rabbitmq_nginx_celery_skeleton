FROM ubuntu:20.04

# apt repository 를 카카오로 변경
RUN sed -i 's@archive.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-dev
RUN apt install -y libpq-dev

RUN apt install -y net-tools
RUN apt install -y dnsutils

## ↓↓↓↓ FOR DEVELOPE ↓↓↓↓ ##
RUN apt install -y iputils-ping
RUN apt install -y vim
RUN apt install -y wget
## ↑↑↑↑  WILL BE ERASE ↑↑↑↑ ##


RUN apt update
# 파이썬 출력 버퍼 제거
#ENV PYTHONUNBUFFERED 0

# 작업 디렉토리 설정
WORKDIR /home/akashic

# requirements.txt 설치
COPY pre_requirements.txt /home/akashic
COPY requirements.txt /home/akashic
RUN pip3 install --upgrade pip
RUN pip3 install -r pre_requirements.txt
RUN pip3 install -r requirements.txt


# postgres를 위한 대기 스크립트.
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
