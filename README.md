# Streaming-Finance-Data-with-AWS-Lambda
sta9760 project3

```
For this project, Lambda functions was used to generate near real time finance data records for downstream processing and interactive querying. 

DataTransformer: Kinesis Firehose Delivery Stream transforms the record and streams it into an S3 bucket.
DataCollector: a simple URL call will grab stock price data and place it into the delivery defined in the DataTransformer. 
DataAnalyzer: query the S3 files generated by the DataTransformer using AWS Athena to gain insight into our streamed data

```
![](/pic/2.png)
![](/pic/1.png)
