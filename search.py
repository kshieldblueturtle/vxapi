#-*- encoding: utf-8 -*-
import json
import os 
import subprocess

outputpath = 'sample/hwp.json'
threshold = 40

def search():
    '''
    타입으로 한글 파일만 찾기
    '''
    try:
        arguments = ['python', 'vxapi.py', 'search_terms', '--filetype', 'hwp']
        proc = subprocess.Popen(arguments, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout = proc.communicate()[0]
        
        return json.loads(stdout.decode('utf-8'))
            
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
            if score is not None and int(score) > 40:
                f.write(item['sha256'] + '\n')

# with open(inputpath, encoding='UTF16') as f:
#     json_data = json.load(f)

json_data = search()
GetSha256(json_data)