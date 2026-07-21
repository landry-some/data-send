import * as cdk from "aws-cdk-lib";
import { IntuApiGw, IntuLambdaFn } from "@jsguru-cdk/core";
import { VendedConstructs } from "./vended-constructs";

export interface CdkStackProps extends cdk.StackProps {
  readonly assetId: string;
  readonly gitOrg: string;
  readonly gitRepo: string;
  readonly imageTag: string;
  readonly appEnv: string;
  readonly environmentVars?: { [key: string]: string };
  readonly lmaEnvironmentVars?: { [key: string]: string };
  readonly serverlessConfig: string;
  readonly vpcId: string;
  readonly subnets: string[];
  readonly availabilityZones: string[];
  readonly domainTLD: string;
  readonly regionCertArn: string;
  readonly hostedZoneId: string;
  readonly serviceName: string;
}

/*
 * A CDK Stack for your infrastructure
 */
export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props: CdkStackProps) {
    super(scope, id, props);

    // keep these lines to support vended constructs from devportal

    const vended = new VendedConstructs(this, "VendedConstructs", {
      assetId: props.assetId,
      appEnv: props.appEnv,
      imageTag: props.imageTag,
    });

    // your custom infrastructure code goes here 👇

    new IntuApiGw(this, "api", {
      appEnv: props.appEnv,
      gitOrg: props.gitOrg,
      gitRepo: props.gitRepo,
      memorySize: 128,
      lmaEnvironmentVars: props.lmaEnvironmentVars,
      domainTLD: props.domainTLD,
      regionCertArn: props.regionCertArn,
      hostedZoneId: props.hostedZoneId,
      lambdaFunc: vended.lambdaFns['chatbot'],
      apiname: "chatbot",
    });

    const secretManager = new cdk.aws_secretsmanager.Secret(this, 'Secret', {
      secretName: `${props.serviceName}-${props.appEnv}`,
      secretObjectValue: {
        UIPATH_SHARED_KEY: cdk.SecretValue.unsafePlainText('CHANGE ME')
      }
    });
    secretManager.grantRead(vended.lambdaFns['chatbot']);
    vended.lambdaFns['chatbot'].addEnvironment('SECRETS_NAME', secretManager.secretName);

  }
}
