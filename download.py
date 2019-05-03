#-*- encoding: utf-8 -*-
import json
import os 
import subprocess

inputpath = 'sample/hwp.json'
outputpath = 'sample/sah256.txt'

def downloadfile():
    '''
    sha256으로 해당 파일 다운로드
    입력: sha256목록이 있는 파일경로
    '''
    try:
        with open(outputpath, 'r') as f:
            lines = f.readlines()
            
            for line in lines:
                if line is None:
                    break
                    
                line = line.strip('\n')
                
                arguments = ['python', 'vxapi.py', 'overview_download_sample', line]
                with subprocess.Popen(arguments) as proc:
                    pass

    except Exception as e:
        print('[Error] subprocess')

downloadfile()