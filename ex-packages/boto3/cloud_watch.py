import boto3
import datetime
from IPython import embed

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

start_time = datetime.datetime.today() - datetime.timedelta(days=1)
end_time   = datetime.datetime.today()

statistics = cloudwatch.get_metric_statistics(
    Namespace='AWS/Billing',
    MetricName='EstimatedCharges',
    Dimensions=[
        {
            'Name': 'Currency',
            'Value': 'USD'
        }
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=3600*24,
    Statistics=['Maximum']
)


print(statistics['Datapoints'][0]['Maximum'])

embed()
