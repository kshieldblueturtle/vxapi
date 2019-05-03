#-*- encoding: utf-8 -*-
import json
import os 
import subprocess

inputpath = 'sample/hwp.json'
outputpath = 'sample/sah256.txt'
threshold = 20

def downloadfile():
    '''
    sha256으로 해당 파일 다운로드
    입력: sha256목록이 있는 파일경로
    '''
    try:
        with open(outputpath, 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip('\n')
                
                arguments = ['python', 'vxapi.py', 'overview_download_sample', line]
                with subprocess.Popen(arguments) as proc:
                    pass

    except Exception as e:
        print('[Error] subprocess')

def GetSha256(json_data):
    '''
    Falcon 샌드박스 검색 결과(json)에서 sha256만 추출
    텍스트 파일로 저장
    '''
    with open(outputpath, 'w') as f:
        for item in json_data['result']:
            score = item['threat_score']

            # 스코어 점수가 null이 아니고 
            # threshold보다 큰 것만 추출
            if score is not None and score > threshold:
                f.write(item['sha256'] + '\n')

with open(inputpath, encoding='UTF16') as f:
    json_data = json.load(f)

#GetSha256(json_data)
downloadfile()