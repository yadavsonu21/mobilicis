import boto3

# Initialize the Boto3 client for CloudWatch
cloudwatch = boto3.client('cloudwatch')

# Set the alarm threshold and duration
alarm_threshold = 80.0
alarm_duration = 5

# Get the ID of the EC2 instance
instance_id = 'INSTANCE_ID'

# Create the alarm
response = cloudwatch.put_metric_alarm(
    AlarmName='CPUUsageAlarm',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=alarm_duration,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=alarm_threshold,
    ActionsEnabled=True,
    AlarmActions=['arn:aws:sns:us-east-1:ACCOUNT_NUMBER:ALERT_TOPIC'],
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ],
)

print(response)
