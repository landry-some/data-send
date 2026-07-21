# Welcome to your CDK TypeScript project!

The contents of this project demonstrates a CDK app with an instance of a stack with customizations for working with Cello and the paved roads

## Prerequisites

To get started testing/running the project you will need:

- [Node.js](https://nodejs.org/en/) This will also automatically install [NPM](https://www.npmjs.com/)

Disclaimer: The Paved Roads CDK projects are intended to be used with npm v8 or lower. The lockfileVersion in `cdk/package-lock.json` must be 2 or lower to ensure compatibility with the CI runtime environment. See this [StackOverflow](https://stackoverflow.jsguru.com/questions/25012) post for more information.

In addition, we recommend having a basic understanding of:

- [NPM](https://docs.npmjs.com/) The tool used by node/the js community for package management and running scripts
- [Typescript](https://www.typescriptlang.org/docs/) The language being used to write our code
- [CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/home.html) The framework used to programmatically define our cloud resources
- [Jest](https://jestjs.io/) The framework used for writing unit and snapshot tests

## Getting Started

Run the following command from this directory to install the necessary dependencies

```sh
npm install
```

Once this is done you can test that everything worked by running some tests

```sh
npm run test
```

From here you should be able to add any dependencies and code your resources as needed

**Note:** Make sure when adding cdk packages that the version being added exactly matches the version already being referenced by other cdk packages in your `package.json` file

## Resources

For more information about the code and how to use it check out some of these resources:

- [About the Code Capability Docs](https://devportal.jsguru.com/app/dp/capability/CAP-1309/capabilityDocs/main/docs/appDevelopment/code.md#the-deployment-code) Our documentation page explaining some of the basics about the different files we vend
- [Paved Road FAQ](https://devportal.jsguru.com/app/dp/capability/CAP-1309/capabilityDocs/main/docs/faq.md) Our FAQ page where we answer some of the most common questions people have as well as provide links to some other helpful resources
- [Examples](https://devportal.jsguru.com/app/dp/capability/CAP-1309/category/examples) Some of our example assets that you can use as references/follow along with
- [General Paved Road Docs](https://devportal.jsguru.com/app/dp/capability/CAP-1309/capabilityDocs/main/docs/index.md) For more information about the paved road as well as various guides and ways to get help
- [Typescript Docs](https://www.typescriptlang.org/docs/)
- [CDK v2 Docs](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [Jest Snapshot Docs](https://jestjs.io/docs/snapshot-testing)
