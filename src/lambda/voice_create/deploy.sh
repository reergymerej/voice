#!/usr/bin/env bash
zip package.zip lambda_function.py
aws lambda update-function-code \
  --function-name voice_create \
  --zip-file fileb://package.zip
