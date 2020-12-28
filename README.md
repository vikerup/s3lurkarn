# s3lurkarn

## Gettings started

s3lurkarn guesses public available s3 bucket based on a supplied keyword.

s3lurkarn was built mainly due to the fact similar projects was missing concurrency while also had uninspiring names. s3lurkarn fixes both these problems.

### Usage

```
./s3lurkarn.py testing
Public http://testing-web.s3.amazonaws.com
Public http://testing-production.s3.amazonaws.com
Public http://web-testing.s3.amazonaws.com
Public http://testing-web.s3.amazonaws.com
Public http://store.testing.s3.amazonaws.com
Public http://testing_aws.s3.amazonaws.com
Public http://testing_testing.s3.amazonaws.com
Public http://testing_dev.s3.amazonaws.com
Public http://static_testing.s3.amazonaws.com
```

### Beware

AWS will block your IP
