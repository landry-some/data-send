import * as cdk from "aws-cdk-lib";
import { Match, Template } from "aws-cdk-lib/assertions";
import { CdkStack } from "../lib/cdk-stack";

describe("sample CDK stack", () => {
  const imageTag = "1234";
  const gitOrg = "someOrg";
  const gitRepo = "someRepo";
  const appEnv = "test";
  const assetId = "1234";
  const cdkEnv = { env: { account: "12345", region: "us-west-2" } };

  const environmentVars = { env: 'local' };
  const lmaEnvironmentVars = { env: 'local' };
  const serverlessConfig = "test config";
  const vpcId = "test vpc id";
  const availabilityZones = ["us-east-1", "us-west-1"];
  const domainTLD = "test.domain.com";
  const regionCertArn = "test region cert arn";
  const hostedZoneId = "test host zone id";
  const serviceName = "test service"

  test("default stack contains default lambda", () => {
    const subnets = ["subnet-11111", "subnet-22222"];
    const app = new cdk.App({
      context: {
        test: {
          "us-west-2": {
            vpcId: "vpc-1234",
            availabilityZones: ["us-west-2a", "us-west-2b", "us-west-2c"],
            privateSubnetIds: subnets,
          },
        },
        vendedLambdaNames: ["chatbot"],
      },
    });
    const stack = new CdkStack(app, "TestApp", {
      appEnv,
      assetId,
      gitOrg,
      gitRepo,
      imageTag,
      environmentVars,
      lmaEnvironmentVars,
      serverlessConfig,
      vpcId,
      subnets,
      availabilityZones,
      domainTLD,
      regionCertArn,
      hostedZoneId,
      serviceName,
      ...cdkEnv,
    });
    const template = Template.fromStack(stack);
    template.hasResource("AWS::Lambda::Function", {
      Properties: {
        Environment: {
          Variables: {
            ENVIRONMENT: appEnv,
            VERSION: imageTag,
          },
        },
        PackageType: "Image",
        VpcConfig: Match.objectLike({
          SubnetIds: subnets,
        }),
      },
    });
  });
});
