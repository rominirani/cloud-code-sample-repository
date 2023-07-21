const functions = require('@google-cloud/functions-framework');
const GcmSynthetics = require('@google-cloud/synthetics-sdk-mocha');

/*
 * This is the server template that is required to run a synthetic monitor in
 * Google Cloud Functions.
 */

functions.http('SyntheticMochaSuite', GcmSynthetics.runMochaHandler({
  spec: `${__dirname}/mocha_tests.spec.js`
}));
