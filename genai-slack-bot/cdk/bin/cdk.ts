#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { CdkStack } from "../lib/cdk-stack";
import { readFileSync } from "fs";
import { getEnvName } from "../utils/cdk-utils";

const app = new cdk.App();

const appEnv = getEnvName(process.env.ENVIRONMENT || "qal");
const envContext = app.node.tryGetContext(getEnvName(appEnv));
const account = process.env.CDK_DEFAULT_ACCOUNT || "123";
const accountContext = envContext[account] || envContext;

const assetId = app.node.tryGetContext("assetId");
const gitOrg = app.node.tryGetContext("gitOrg");
const gitRepo = app.node.tryGetContext("gitRepo");
const description = app.node.tryGetContext("description");
const serviceName = app.node.tryGetContext("service_name");
const region = process.env.CDK_DEFAULT_REGION;

if (!gitOrg || !gitRepo || !assetId || !region) {
  throw new Error(`required CDK contexts not set`);
}

const imageTag = obtainImageTag();

const cdkEnv = {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
};

// Apply tags to all CDK resources
cdk.Tags.of(app).add("jsguru:asset_id", assetId);
cdk.Tags.of(app).add("jsguru:git_org", gitOrg);
cdk.Tags.of(app).add("jsguru:git_repo", gitRepo);
cdk.Tags.of(app).add("jsguru:managed_by", "serverless");
cdk.Tags.of(app).add("environment", appEnv);

const stackName = `${appEnv}-${assetId}`;

new CdkStack(app, stackName, {
  appEnv,
  assetId,
  gitOrg,
  gitRepo,
  imageTag,
  description,
  serviceName,
  environmentVars: accountContext[region]?.envVars,
  lmaEnvironmentVars: accountContext[region]?.lmaEnvVars,
  serverlessConfig: accountContext[region]?.serverlessConfig,
  vpcId: accountContext[region]?.vpcId,
  subnets: accountContext[region]?.subnets,
  availabilityZones: accountContext[region]?.availabilityZones,
  domainTLD: accountContext[region]?.domainTld,
  regionCertArn: accountContext[region]?.regionCertArn,
  hostedZoneId: accountContext[region]?.hostedZoneId,
  ...cdkEnv,
});

function obtainImageTag(): string {
  let tag = "";

  try {
    tag = readFileSync("./image_tag.txt", "utf-8");
  } catch (error) {
    throw new Error(`image_tag.txt must exist`);
  }

  if (!tag) {
    throw new Error(`image_tag.txt must contain an image tag`);
  }

  return tag.trim();
}
