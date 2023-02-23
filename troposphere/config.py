# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.config import ONE_HOUR  # noqa: F401
from .validators.config import SIX_HOURS  # noqa: F401
from .validators.config import THREE_HOURS  # noqa: F401
from .validators.config import TWELVE_HOURS  # noqa: F401
from .validators.config import TWENTYFOUR_HOURS  # noqa: F401
from .validators.config import validate_source_details


class AggregationAuthorization(AWSObject):
    """
    `AggregationAuthorization <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html>`__
    """

    resource_type = "AWS::Config::AggregationAuthorization"

    props: PropsDictType = {
        "AuthorizedAccountId": (str, True),
        "AuthorizedAwsRegion": (str, True),
        "Tags": (Tags, False),
    }


class Scope(AWSProperty):
    """
    `Scope <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html>`__
    """

    props: PropsDictType = {
        "ComplianceResourceId": (str, False),
        "ComplianceResourceTypes": ([str], False),
        "TagKey": (str, False),
        "TagValue": (str, False),
    }


class CustomPolicyDetails(AWSProperty):
    """
    `CustomPolicyDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html>`__
    """

    props: PropsDictType = {
        "EnableDebugLogDelivery": (boolean, False),
        "PolicyRuntime": (str, False),
        "PolicyText": (str, False),
    }


class SourceDetails(AWSProperty):
    """
    `SourceDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html>`__
    """

    props: PropsDictType = {
        "EventSource": (str, True),
        "MaximumExecutionFrequency": (str, False),
        "MessageType": (str, True),
    }

    def validate(self):
        validate_source_details(self)


class Source(AWSProperty):
    """
    `Source <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html>`__
    """

    props: PropsDictType = {
        "CustomPolicyDetails": (CustomPolicyDetails, False),
        "Owner": (str, True),
        "SourceDetails": ([SourceDetails], False),
        "SourceIdentifier": (str, False),
    }


class ConfigRule(AWSObject):
    """
    `ConfigRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html>`__
    """

    resource_type = "AWS::Config::ConfigRule"

    props: PropsDictType = {
        "ConfigRuleName": (str, False),
        "Description": (str, False),
        "InputParameters": (dict, False),
        "MaximumExecutionFrequency": (str, False),
        "Scope": (Scope, False),
        "Source": (Source, True),
    }


class AccountAggregationSources(AWSProperty):
    """
    `AccountAggregationSources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html>`__
    """

    props: PropsDictType = {
        "AccountIds": ([str], True),
        "AllAwsRegions": (boolean, False),
        "AwsRegions": ([str], False),
    }


class OrganizationAggregationSource(AWSProperty):
    """
    `OrganizationAggregationSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html>`__
    """

    props: PropsDictType = {
        "AllAwsRegions": (boolean, False),
        "AwsRegions": ([str], False),
        "RoleArn": (str, True),
    }


class ConfigurationAggregator(AWSObject):
    """
    `ConfigurationAggregator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html>`__
    """

    resource_type = "AWS::Config::ConfigurationAggregator"

    props: PropsDictType = {
        "AccountAggregationSources": ([AccountAggregationSources], False),
        "ConfigurationAggregatorName": (str, False),
        "OrganizationAggregationSource": (OrganizationAggregationSource, False),
        "Tags": (Tags, False),
    }


class RecordingGroup(AWSProperty):
    """
    `RecordingGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html>`__
    """

    props: PropsDictType = {
        "AllSupported": (boolean, False),
        "IncludeGlobalResourceTypes": (boolean, False),
        "ResourceTypes": ([str], False),
    }


class ConfigurationRecorder(AWSObject):
    """
    `ConfigurationRecorder <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html>`__
    """

    resource_type = "AWS::Config::ConfigurationRecorder"

    props: PropsDictType = {
        "Name": (str, False),
        "RecordingGroup": (RecordingGroup, False),
        "RoleARN": (str, True),
    }


class ConformancePackInputParameter(AWSProperty):
    """
    `ConformancePackInputParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html>`__
    """

    props: PropsDictType = {
        "ParameterName": (str, True),
        "ParameterValue": (str, True),
    }


class TemplateSSMDocumentDetails(AWSProperty):
    """
    `TemplateSSMDocumentDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html>`__
    """

    props: PropsDictType = {
        "DocumentName": (str, False),
        "DocumentVersion": (str, False),
    }


class ConformancePack(AWSObject):
    """
    `ConformancePack <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html>`__
    """

    resource_type = "AWS::Config::ConformancePack"

    props: PropsDictType = {
        "ConformancePackInputParameters": ([ConformancePackInputParameter], False),
        "ConformancePackName": (str, True),
        "DeliveryS3Bucket": (str, False),
        "DeliveryS3KeyPrefix": (str, False),
        "TemplateBody": (str, False),
        "TemplateS3Uri": (str, False),
        "TemplateSSMDocumentDetails": (TemplateSSMDocumentDetails, False),
    }


class ConfigSnapshotDeliveryProperties(AWSProperty):
    """
    `ConfigSnapshotDeliveryProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html>`__
    """

    props: PropsDictType = {
        "DeliveryFrequency": (str, False),
    }


class DeliveryChannel(AWSObject):
    """
    `DeliveryChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html>`__
    """

    resource_type = "AWS::Config::DeliveryChannel"

    props: PropsDictType = {
        "ConfigSnapshotDeliveryProperties": (ConfigSnapshotDeliveryProperties, False),
        "Name": (str, False),
        "S3BucketName": (str, True),
        "S3KeyPrefix": (str, False),
        "S3KmsKeyArn": (str, False),
        "SnsTopicARN": (str, False),
    }


class OrganizationCustomPolicyRuleMetadata(AWSProperty):
    """
    `OrganizationCustomPolicyRuleMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html>`__
    """

    props: PropsDictType = {
        "DebugLogDeliveryAccounts": ([str], False),
        "Description": (str, False),
        "InputParameters": (str, False),
        "MaximumExecutionFrequency": (str, False),
        "OrganizationConfigRuleTriggerTypes": ([str], False),
        "PolicyText": (str, True),
        "ResourceIdScope": (str, False),
        "ResourceTypesScope": ([str], False),
        "Runtime": (str, True),
        "TagKeyScope": (str, False),
        "TagValueScope": (str, False),
    }


class OrganizationCustomRuleMetadata(AWSProperty):
    """
    `OrganizationCustomRuleMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "InputParameters": (str, False),
        "LambdaFunctionArn": (str, True),
        "MaximumExecutionFrequency": (str, False),
        "OrganizationConfigRuleTriggerTypes": ([str], True),
        "ResourceIdScope": (str, False),
        "ResourceTypesScope": ([str], False),
        "TagKeyScope": (str, False),
        "TagValueScope": (str, False),
    }


class OrganizationManagedRuleMetadata(AWSProperty):
    """
    `OrganizationManagedRuleMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "InputParameters": (str, False),
        "MaximumExecutionFrequency": (str, False),
        "ResourceIdScope": (str, False),
        "ResourceTypesScope": ([str], False),
        "RuleIdentifier": (str, True),
        "TagKeyScope": (str, False),
        "TagValueScope": (str, False),
    }


class OrganizationConfigRule(AWSObject):
    """
    `OrganizationConfigRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html>`__
    """

    resource_type = "AWS::Config::OrganizationConfigRule"

    props: PropsDictType = {
        "ExcludedAccounts": ([str], False),
        "OrganizationConfigRuleName": (str, True),
        "OrganizationCustomPolicyRuleMetadata": (
            OrganizationCustomPolicyRuleMetadata,
            False,
        ),
        "OrganizationCustomRuleMetadata": (OrganizationCustomRuleMetadata, False),
        "OrganizationManagedRuleMetadata": (OrganizationManagedRuleMetadata, False),
    }


class OrganizationConformancePack(AWSObject):
    """
    `OrganizationConformancePack <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html>`__
    """

    resource_type = "AWS::Config::OrganizationConformancePack"

    props: PropsDictType = {
        "ConformancePackInputParameters": ([ConformancePackInputParameter], False),
        "DeliveryS3Bucket": (str, False),
        "DeliveryS3KeyPrefix": (str, False),
        "ExcludedAccounts": ([str], False),
        "OrganizationConformancePackName": (str, True),
        "TemplateBody": (str, False),
        "TemplateS3Uri": (str, False),
    }


class SsmControls(AWSProperty):
    """
    `SsmControls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html>`__
    """

    props: PropsDictType = {
        "ConcurrentExecutionRatePercentage": (integer, False),
        "ErrorPercentage": (integer, False),
    }


class ExecutionControls(AWSProperty):
    """
    `ExecutionControls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html>`__
    """

    props: PropsDictType = {
        "SsmControls": (SsmControls, False),
    }


class RemediationConfiguration(AWSObject):
    """
    `RemediationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html>`__
    """

    resource_type = "AWS::Config::RemediationConfiguration"

    props: PropsDictType = {
        "Automatic": (boolean, False),
        "ConfigRuleName": (str, True),
        "ExecutionControls": (ExecutionControls, False),
        "MaximumAutomaticAttempts": (integer, False),
        "Parameters": (dict, False),
        "ResourceType": (str, False),
        "RetryAttemptSeconds": (integer, False),
        "TargetId": (str, True),
        "TargetType": (str, True),
        "TargetVersion": (str, False),
    }


class StoredQuery(AWSObject):
    """
    `StoredQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html>`__
    """

    resource_type = "AWS::Config::StoredQuery"

    props: PropsDictType = {
        "QueryDescription": (str, False),
        "QueryExpression": (str, True),
        "QueryName": (str, True),
        "Tags": (Tags, False),
    }


class ResourceValue(AWSProperty):
    """
    `ResourceValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html>`__
    """

    props: PropsDictType = {
        "Value": (str, False),
    }


class StaticValue(AWSProperty):
    """
    `StaticValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html>`__
    """

    props: PropsDictType = {
        "Values": ([str], False),
    }


class RemediationParameterValue(AWSProperty):
    """
    `RemediationParameterValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html>`__
    """

    props: PropsDictType = {
        "ResourceValue": (ResourceValue, False),
        "StaticValue": (StaticValue, False),
    }
