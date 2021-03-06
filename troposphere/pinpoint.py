# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 8.0.0


from . import AWSObject
from . import AWSProperty
from .validators import boolean
from .validators import integer
from .validators import double


class ADMChannel(AWSObject):
    resource_type = "AWS::Pinpoint::ADMChannel"

    props = {
        'ApplicationId': (basestring, True),
        'ClientId': (basestring, True),
        'ClientSecret': (basestring, True),
        'Enabled': (boolean, False),
    }


class APNSChannel(AWSObject):
    resource_type = "AWS::Pinpoint::APNSChannel"

    props = {
        'ApplicationId': (basestring, True),
        'BundleId': (basestring, False),
        'Certificate': (basestring, False),
        'DefaultAuthenticationMethod': (basestring, False),
        'Enabled': (boolean, False),
        'PrivateKey': (basestring, False),
        'TeamId': (basestring, False),
        'TokenKey': (basestring, False),
        'TokenKeyId': (basestring, False),
    }


class APNSSandboxChannel(AWSObject):
    resource_type = "AWS::Pinpoint::APNSSandboxChannel"

    props = {
        'ApplicationId': (basestring, True),
        'BundleId': (basestring, False),
        'Certificate': (basestring, False),
        'DefaultAuthenticationMethod': (basestring, False),
        'Enabled': (boolean, False),
        'PrivateKey': (basestring, False),
        'TeamId': (basestring, False),
        'TokenKey': (basestring, False),
        'TokenKeyId': (basestring, False),
    }


class APNSVoipChannel(AWSObject):
    resource_type = "AWS::Pinpoint::APNSVoipChannel"

    props = {
        'ApplicationId': (basestring, True),
        'BundleId': (basestring, False),
        'Certificate': (basestring, False),
        'DefaultAuthenticationMethod': (basestring, False),
        'Enabled': (boolean, False),
        'PrivateKey': (basestring, False),
        'TeamId': (basestring, False),
        'TokenKey': (basestring, False),
        'TokenKeyId': (basestring, False),
    }


class APNSVoipSandboxChannel(AWSObject):
    resource_type = "AWS::Pinpoint::APNSVoipSandboxChannel"

    props = {
        'ApplicationId': (basestring, True),
        'BundleId': (basestring, False),
        'Certificate': (basestring, False),
        'DefaultAuthenticationMethod': (basestring, False),
        'Enabled': (boolean, False),
        'PrivateKey': (basestring, False),
        'TeamId': (basestring, False),
        'TokenKey': (basestring, False),
        'TokenKeyId': (basestring, False),
    }


class App(AWSObject):
    resource_type = "AWS::Pinpoint::App"

    props = {
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class CampaignHook(AWSProperty):
    props = {
        'LambdaFunctionName': (basestring, False),
        'Mode': (basestring, False),
        'WebUrl': (basestring, False),
    }


class Limits(AWSProperty):
    props = {
        'Daily': (integer, False),
        'MaximumDuration': (integer, False),
        'MessagesPerSecond': (integer, False),
        'Total': (integer, False),
    }


class QuietTime(AWSProperty):
    props = {
        'End': (basestring, True),
        'Start': (basestring, True),
    }


class ApplicationSettings(AWSObject):
    resource_type = "AWS::Pinpoint::ApplicationSettings"

    props = {
        'ApplicationId': (basestring, True),
        'CampaignHook': (CampaignHook, False),
        'CloudWatchMetricsEnabled': (boolean, False),
        'Limits': (Limits, False),
        'QuietTime': (QuietTime, False),
    }


class BaiduChannel(AWSObject):
    resource_type = "AWS::Pinpoint::BaiduChannel"

    props = {
        'ApiKey': (basestring, True),
        'ApplicationId': (basestring, True),
        'Enabled': (boolean, False),
        'SecretKey': (basestring, True),
    }


class CampaignEmailMessage(AWSProperty):
    props = {
        'Body': (basestring, False),
        'FromAddress': (basestring, False),
        'HtmlBody': (basestring, False),
        'Title': (basestring, False),
    }


class CampaignSmsMessage(AWSProperty):
    props = {
        'Body': (basestring, False),
        'MessageType': (basestring, False),
        'SenderId': (basestring, False),
    }


class Message(AWSProperty):
    props = {
        'Action': (basestring, False),
        'Body': (basestring, False),
        'ImageIconUrl': (basestring, False),
        'ImageSmallIconUrl': (basestring, False),
        'ImageUrl': (basestring, False),
        'JsonBody': (basestring, False),
        'MediaUrl': (basestring, False),
        'RawContent': (basestring, False),
        'SilentPush': (boolean, False),
        'TimeToLive': (integer, False),
        'Title': (basestring, False),
        'Url': (basestring, False),
    }


class MessageConfiguration(AWSProperty):
    props = {
        'ADMMessage': (Message, False),
        'APNSMessage': (Message, False),
        'BaiduMessage': (Message, False),
        'DefaultMessage': (Message, False),
        'EmailMessage': (CampaignEmailMessage, False),
        'GCMMessage': (Message, False),
        'SMSMessage': (CampaignSmsMessage, False),
    }


class SetDimension(AWSProperty):
    props = {
        'DimensionType': (basestring, False),
        'Values': ([basestring], False),
    }


class EventDimensions(AWSProperty):
    props = {
        'Attributes': (dict, False),
        'EventType': (SetDimension, False),
        'Metrics': (dict, False),
    }


class CampaignEventFilter(AWSProperty):
    props = {
        'Dimensions': (EventDimensions, False),
        'FilterType': (basestring, False),
    }


class Schedule(AWSProperty):
    props = {
        'EndTime': (basestring, False),
        'EventFilter': (CampaignEventFilter, False),
        'Frequency': (basestring, False),
        'IsLocalTime': (boolean, False),
        'QuietTime': (QuietTime, False),
        'StartTime': (basestring, False),
        'TimeZone': (basestring, False),
    }


class WriteTreatmentResource(AWSProperty):
    props = {
        'MessageConfiguration': (MessageConfiguration, False),
        'Schedule': (Schedule, False),
        'SizePercent': (integer, False),
        'TreatmentDescription': (basestring, False),
        'TreatmentName': (basestring, False),
    }


class Campaign(AWSObject):
    resource_type = "AWS::Pinpoint::Campaign"

    props = {
        'AdditionalTreatments': ([WriteTreatmentResource], False),
        'ApplicationId': (basestring, True),
        'CampaignHook': (CampaignHook, False),
        'Description': (basestring, False),
        'HoldoutPercent': (integer, False),
        'IsPaused': (boolean, False),
        'Limits': (Limits, False),
        'MessageConfiguration': (MessageConfiguration, True),
        'Name': (basestring, True),
        'Schedule': (Schedule, True),
        'SegmentId': (basestring, True),
        'SegmentVersion': (integer, False),
        'Tags': (dict, False),
        'TreatmentDescription': (basestring, False),
        'TreatmentName': (basestring, False),
    }


class EmailChannel(AWSObject):
    resource_type = "AWS::Pinpoint::EmailChannel"

    props = {
        'ApplicationId': (basestring, True),
        'ConfigurationSet': (basestring, False),
        'Enabled': (boolean, False),
        'FromAddress': (basestring, True),
        'Identity': (basestring, True),
        'RoleArn': (basestring, False),
    }


class EmailTemplate(AWSObject):
    resource_type = "AWS::Pinpoint::EmailTemplate"

    props = {
        'HtmlPart': (basestring, False),
        'Subject': (basestring, True),
        'Tags': (dict, False),
        'TemplateName': (basestring, True),
        'TextPart': (basestring, False),
    }


class EventStream(AWSObject):
    resource_type = "AWS::Pinpoint::EventStream"

    props = {
        'ApplicationId': (basestring, True),
        'DestinationStreamArn': (basestring, True),
        'RoleArn': (basestring, True),
    }


class GCMChannel(AWSObject):
    resource_type = "AWS::Pinpoint::GCMChannel"

    props = {
        'ApiKey': (basestring, True),
        'ApplicationId': (basestring, True),
        'Enabled': (boolean, False),
    }


class APNSPushNotificationTemplate(AWSProperty):
    props = {
        'Action': (basestring, False),
        'Body': (basestring, False),
        'MediaUrl': (basestring, False),
        'Sound': (basestring, False),
        'Title': (basestring, False),
        'Url': (basestring, False),
    }


class AndroidPushNotificationTemplate(AWSProperty):
    props = {
        'Action': (basestring, False),
        'Body': (basestring, False),
        'ImageIconUrl': (basestring, False),
        'ImageUrl': (basestring, False),
        'SmallImageIconUrl': (basestring, False),
        'Sound': (basestring, False),
        'Title': (basestring, False),
        'Url': (basestring, False),
    }


class DefaultPushNotificationTemplate(AWSProperty):
    props = {
        'Action': (basestring, False),
        'Body': (basestring, False),
        'Sound': (basestring, False),
        'Title': (basestring, False),
        'Url': (basestring, False),
    }


class PushTemplate(AWSObject):
    resource_type = "AWS::Pinpoint::PushTemplate"

    props = {
        'ADM': (AndroidPushNotificationTemplate, False),
        'APNS': (APNSPushNotificationTemplate, False),
        'Baidu': (AndroidPushNotificationTemplate, False),
        'Default': (DefaultPushNotificationTemplate, False),
        'GCM': (AndroidPushNotificationTemplate, False),
        'Tags': (dict, False),
        'TemplateName': (basestring, True),
    }


class SMSChannel(AWSObject):
    resource_type = "AWS::Pinpoint::SMSChannel"

    props = {
        'ApplicationId': (basestring, True),
        'Enabled': (boolean, False),
        'SenderId': (basestring, False),
        'ShortCode': (basestring, False),
    }


class Recency(AWSProperty):
    props = {
        'Duration': (basestring, True),
        'RecencyType': (basestring, True),
    }


class Behavior(AWSProperty):
    props = {
        'Recency': (Recency, False),
    }


class Demographic(AWSProperty):
    props = {
        'AppVersion': (SetDimension, False),
        'Channel': (SetDimension, False),
        'DeviceType': (SetDimension, False),
        'Make': (SetDimension, False),
        'Model': (SetDimension, False),
        'Platform': (SetDimension, False),
    }


class Coordinates(AWSProperty):
    props = {
        'Latitude': (double, True),
        'Longitude': (double, True),
    }


class GPSPoint(AWSProperty):
    props = {
        'Coordinates': (Coordinates, True),
        'RangeInKilometers': (double, True),
    }


class Location(AWSProperty):
    props = {
        'Country': (SetDimension, False),
        'GPSPoint': (GPSPoint, False),
    }


class SegmentDimensions(AWSProperty):
    props = {
        'Attributes': (dict, False),
        'Behavior': (Behavior, False),
        'Demographic': (Demographic, False),
        'Location': (Location, False),
        'Metrics': (dict, False),
        'UserAttributes': (dict, False),
    }


class SourceSegments(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Version': (integer, False),
    }


class Groups(AWSProperty):
    props = {
        'Dimensions': ([SegmentDimensions], False),
        'SourceSegments': ([SourceSegments], False),
        'SourceType': (basestring, False),
        'Type': (basestring, False),
    }


class SegmentGroups(AWSProperty):
    props = {
        'Groups': ([Groups], False),
        'Include': (basestring, False),
    }


class Segment(AWSObject):
    resource_type = "AWS::Pinpoint::Segment"

    props = {
        'ApplicationId': (basestring, True),
        'Dimensions': (SegmentDimensions, False),
        'Name': (basestring, True),
        'SegmentGroups': (SegmentGroups, False),
        'Tags': (dict, False),
    }


class SmsTemplate(AWSObject):
    resource_type = "AWS::Pinpoint::SmsTemplate"

    props = {
        'Body': (basestring, True),
        'Tags': (dict, False),
        'TemplateName': (basestring, True),
    }


class VoiceChannel(AWSObject):
    resource_type = "AWS::Pinpoint::VoiceChannel"

    props = {
        'ApplicationId': (basestring, True),
        'Enabled': (boolean, False),
    }
