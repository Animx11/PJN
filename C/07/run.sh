#!/bin/bash

awk '{print NR " " $s}' | sort -rg