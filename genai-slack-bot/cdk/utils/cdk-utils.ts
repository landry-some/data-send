export function getEnvName(envName: string): string {
  const prRegex = new RegExp('^pr\\d+');
  if (prRegex.test(envName)) {
    return 'pr';
  } else {
    return envName;
  }
};