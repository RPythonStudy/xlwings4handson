#!/bin/bash
# .env.example을 복사하여 .env 생성 후, 프로젝트 폴더명으로 변수값 자동 치환

set -e

CUR_DIR_NAME=$(basename "$PWD")
CUR_DIR_PATH="$PWD"

# .env.example 존재 확인
if [ ! -f .env.example ]; then
  echo "[ERROR] .env.example 파일이 없습니다."
  exit 1
fi

# .env 복사
cp -f .env.example .env

# PROJECT_NAME 치환
sed -i "s/^PROJECT_NAME=.*/PROJECT_NAME=${CUR_DIR_NAME}/" .env

# SERVICE_LOG_PATH, AUDIT_LOG_PATH 경로 치환
sed -i "s|/home/ben/projects/rpy-quarto-template/|${CUR_DIR_PATH}/|g" .env

echo "[INFO] .env 파일이 생성되고, 경로 및 프로젝트명이 현재 폴더명으로 자동 치환되었습니다."
