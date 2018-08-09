#!/bin/bash

# run a test using standard target positions at CMAC for OBC 2018

# target positions taken from test on 5th August 2018
FLAGS="--flag=-35.362669,149.164242,barrell"
FLAGS="$FLAGS --flag=-35.362846,149.164272,barrell"
FLAGS="$FLAGS --flag=-35.363027,149.164295,barrell"

# note that we need to use params.json, not params_half.json
# for accurate georef
CAM_PARMS="../cuav/data/PiCamV2/params.json"

geosearch.py --camera-params=$CAM_PARMS --minscore=500 $FLAGS $*
