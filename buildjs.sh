#!/bin/bash

set -e

cd visstr
npm install
npm run build
cp ./lib/vis_str.umd.js ../lib/visstr/