# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double
from .validators.logs import policytypes  # noqa: F401
from .validators.logs import (
    validate_loggroup_retention_in_days,
    validate_resource_policy,
)


class Destination(AWSObject):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html>`__
    """

    resource_type = "AWS::Logs::Destination"

    props: PropsDictType = {
        "DestinationName": (str, True),
        "DestinationPolicy": (str, False),
        "RoleArn": (str, True),
        "TargetArn": (str, True),
    }


class LogGroup(AWSObject):
    """
    `LogGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html>`__
    """

    resource_type = "AWS::Logs::LogGroup"

    props: PropsDictType = {
        "DataProtectionPolicy": (dict, False),
        "KmsKeyId": (str, False),
        "LogGroupName": (str, False),
        "RetentionInDays": (validate_loggroup_retention_in_days, False),
        "Tags": (Tags, False),
    }


class LogStream(AWSObject):
    """
    `LogStream <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html>`__
    """

    resource_type = "AWS::Logs::LogStream"

    props: PropsDictType = {
        "LogGroupName": (str, True),
        "LogStreamName": (str, False),
    }


class Dimension(AWSProperty):
    """
    `Dimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class MetricTransformation(AWSProperty):
    """
    `MetricTransformation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html>`__
    """

    props: PropsDictType = {
        "DefaultValue": (double, False),
        "Dimensions": ([Dimension], False),
        "MetricName": (str, True),
        "MetricNamespace": (str, True),
        "MetricValue": (str, True),
        "Unit": (str, False),
    }


class MetricFilter(AWSObject):
    """
    `MetricFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html>`__
    """

    resource_type = "AWS::Logs::MetricFilter"

    props: PropsDictType = {
        "FilterName": (str, False),
        "FilterPattern": (str, True),
        "LogGroupName": (str, True),
        "MetricTransformations": ([MetricTransformation], True),
    }


class QueryDefinition(AWSObject):
    """
    `QueryDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html>`__
    """

    resource_type = "AWS::Logs::QueryDefinition"

    props: PropsDictType = {
        "LogGroupNames": ([str], False),
        "Name": (str, True),
        "QueryString": (str, True),
    }


class ResourcePolicy(AWSObject):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html>`__
    """

    resource_type = "AWS::Logs::ResourcePolicy"

    props: PropsDictType = {
        "PolicyDocument": (validate_resource_policy, True),
        "PolicyName": (str, True),
    }


class SubscriptionFilter(AWSObject):
    """
    `SubscriptionFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html>`__
    """

    resource_type = "AWS::Logs::SubscriptionFilter"

    props: PropsDictType = {
        "DestinationArn": (str, True),
        "Distribution": (str, False),
        "FilterName": (str, False),
        "FilterPattern": (str, True),
        "LogGroupName": (str, True),
        "RoleArn": (str, False),
    }
