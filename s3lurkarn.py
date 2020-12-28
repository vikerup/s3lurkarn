#!/usr/bin/env python3
import asyncio
import requests
import sys
from concurrent.futures import ThreadPoolExecutor
import pyfiglet

#ascii_banner = pyfiglet.figlet_format("S3LURKARN")


url = 'https://s3.amazonaws.com/'
name = sys.argv[1].strip()

connectors = ['-','_','']

url = url + name

def fetch(session, com):
    with session.get(com) as response:
        #url = "http://" + name + com + ".s3.amazonaws.com"
        if response.status_code == 200: 
            print("Public",com),
            #conn = client('s3')
            #for key in conn.list_objects(Bucket=bucket)['Contents']:print(key['Key'])
        
        #elif response.status_code == 404: print("None"),
        #elif response.status_code == 403: print("Secure",com),
        #elif response.status_code == 301: print("Redirect",url),
        #elif response.status_code == 400: print("BadName"),
        #return

async def get_data_asynchronous():
    common = [
            'test','dev','bucket',
            'files','upload','uploads',
            '123','000','1','2',
            'store','001','s3',
            'aws','prd','prod',
            'pub','public','production',
            'development','testing',
            'archive','backup','backups','bak','web',
            'devops','sec','secure',
            'hidden','secret','staging',
            'static','download',
            'admin','administrator','app',
            'assets','common','contract',
            'corp','corperate','directory',
            'docker','dynamo','dynamodb',
            'ec2','export','fileshare',
            'git','github','gitlab',
            'graphql','infra',
            'internal','internal-tools',
            'jira','kubernetes','ldap',
            'mysql','mariadb','packages',
            'postgres','private','share',
            'terrafrom','deploy',
            'www','keys','web'
            ]
    connector1 = ["http://" + name + "-" + comm + ".s3.amazonaws.com" for comm in common]
    connector2 = ["http://" + comm + "-" + name + ".s3.amazonaws.com" for comm in common]
    connector3 = ["http://" + name + "." + comm + ".s3.amazonaws.com" for comm in common]
    connector4 = ["http://" + comm + "." + name + ".s3.amazonaws.com" for comm in common]
    connector5 = ["http://" + name + "_" + comm + ".s3.amazonaws.com" for comm in common]
    connector6 = ["http://" + comm + "_" + name + ".s3.amazonaws.com" for comm in common]
    connector7 = ["http://" + name + ".s3.amazonaws.com"]
    common = connector1 + connector2 + connector3 + connector4 + connector5 + connector6 + connector7
    #common = common + connector1 + connector2 + connector3 + [name]
    #print(common)

    with ThreadPoolExecutor(max_workers=25) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                    loop.run_in_executor(
                        executor,
                        fetch,
                        *(session, com)
                    )
                    for com in common
            ]
            for response in await asyncio.gather(*tasks):
                pass
def main():
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_asynchronous())
    loop.run_until_complete(future)

main()
