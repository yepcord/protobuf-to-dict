#!/bin/bash

protoc -I=. --python_out=. ./sample.proto
