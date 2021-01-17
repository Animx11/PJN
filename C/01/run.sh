#!/bin/bash

grep -oP "[0-9]*" | sort -gr | uniq