#!/usr/bin/env bash
zip package.zip *.py
aws lambda update-function-code \
  --function-name voice_db \
  --zip-file fileb://package.zip
