// @generated
// This file was automatically generated and should not be edited.

import * as cdk from "aws-cdk-lib";
import * as jsgurucdk from "@jsguru-cdk/core";
import { Construct } from "constructs";
import { IntuLambdaFn, IntuLambdaFnProps } from "@jsguru-cdk/core";
import { aws_ec2 as ec2 } from "aws-cdk-lib";
import { getEnvName } from "../utils/cdk-utils";

export interface VendedConstructsProps extends cdk.StackProps {
  readonly assetId: string;
  readonly appEnv: string;
  readonly imageTag: string;

  // additional resource props
  readonly lambdaProps?: Partial<IntuLambdaFnProps>;
}

/**
 * VendedConstructs is a CDK Construct which contains all resources vended by
 * the Serverless/CloudStack Paved Roads.
 *
 * !! This file is NOT intended to be manually modified !!
 *
 * If you want to use/modify the vended resources in your CDK stack, access them
 * through the public properties below, in your lib/cdk-stack.ts.

 * For more information please visit the Serverless/CloudStack Capability docs.
 */
export class VendedConstructs extends Construct {
  // public properties
  public readonly lambdaFns: Record<string, IntuLambdaFn>; // map of functionName -> IntuLambdaFn
  public readonly vpc: ec2.IVpc;
  public readonly alternateSubnets: ec2.SubnetSelection;
  public readonly dataSubnets: ec2.SubnetSelection;
  public readonly egressSubnets: ec2.SubnetSelection;
  public readonly ingressSubnets: ec2.SubnetSelection;
  public readonly privateSubnets: ec2.SubnetSelection;

  constructor(scope: Construct, id: string, props: VendedConstructsProps) {
    super(scope, id);
    const envContext = scope.node.tryGetContext(getEnvName(props.appEnv)) || {};
    const account = cdk.Stack.of(this).account;
    const accountContext = envContext[account] || envContext;
    const region = cdk.Stack.of(this).region;
    const regionContext = accountContext[region] || {};

    // vpc supersedes all others when added. the rest can flow in dependsOn order
    const vpcLookup = jsgurucdk.IntuVpc.fromLookup(this, "Vpc", {
      appEnv: props.appEnv,
    })

    this.vpc = vpcLookup.vpc;
    this.alternateSubnets = vpcLookup.alternateSubnets;
    this.dataSubnets = vpcLookup.dataSubnets;
    this.egressSubnets = vpcLookup.egressSubnets;
    this.ingressSubnets = vpcLookup.ingressSubnets;
    this.privateSubnets = vpcLookup.privateSubnets;

    // additional constructs
    const lambdaNames = (scope.node.tryGetContext("vendedLambdaNames") ?? []) as string[]
    const lambdaDefaultProps = {
      assetId: props.assetId,
      gitOrg: scope.node.tryGetContext('gitOrg'),
      gitRepo: scope.node.tryGetContext('gitRepo'),
      imageTag: props.imageTag,
      memorySize: 512,
      description: `Vended lambda function for ${props.assetId}`,
      vpcSubnets: this.privateSubnets,
      vpc: this.vpc,
      appEnv: props.appEnv,
      environment: regionContext['envVars'] || {}, 
    }
    this.lambdaFns = lambdaNames.reduce(
      (acc: Record<string, IntuLambdaFn>, lambdaName: string) => {
        return {
          ...acc,
          [lambdaName]: new IntuLambdaFn(
          this,
          `${lambdaName}Lambda`,
          {
            functionName: lambdaName,
            ...lambdaDefaultProps, 
            ...props.lambdaProps
          }
        )
        };
      }, {}
    );

  }
}
