import {getEnvName} from '../utils/cdk-utils';

describe("CDK Utils", () => {
  test("Test get PR name without change ID", () => {
    const prEnv = 'pr';

    const envName = getEnvName(prEnv);
    expect(envName).toBe(prEnv);
  });

  test("Test get PR name", () => {
    const prEnv = 'pr3';

    const envName = getEnvName(prEnv);
    expect(envName).toBe('pr');
  });

  test("Test get qal name", () => {
    const qalEnv = 'qal';

    const envName = getEnvName(qalEnv);
    expect(envName).toBe(qalEnv);
  });

  test("Test get prod name", () => {
    const prodEnv = 'prod';

    const envName = getEnvName(prodEnv);
    expect(envName).toBe(prodEnv);
  });

  test("Test get prd name", () => {
    const prdEnv = 'prd';

    const envName = getEnvName(prdEnv);
    expect(envName).toBe(prdEnv);
  });
});