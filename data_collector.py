import json
import boto3
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

def lambda_handler(event, context):
    
    stocks = ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    data = yf.Tickers(stocks)
    hist = data.history(start="2020-05-14", end="2020-05-15",interval="1m",group_by = 'tickers')

    summ = []

    for stock in stocks:
        for index, value in hist[stock].iterrows():
            summ.append({'high':value['High'],'low':value['Low'],'ts':index.strftime('%Y-%m-%d %H:%M:%S'),'name':stock})
        
    # initialize boto3 client
    fh = boto3.client("firehose", "us-east-2")
    as_jsonstr = json.dumps(summ)

        # this actually pushed to our firehose datastream
        # we must "encode" in order to convert it into the
        # bytes datatype as all of AWS libs operate over
        # bytes not strings
    fh.put_record(
        DeliveryStreamName="test-delivery-stream", 
        Record={"Data": as_jsonstr.encode('utf-8')})

    # return
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }