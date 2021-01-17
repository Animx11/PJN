#!/bin/bash

cut -d ";" -f 3  | grep -oP "[0-9]*" | sort -gr | head -1