#!/bin/bash

grep 'serdar' ./event_history.csv | grep 'TerminateInstances' | egrep -o '\bi-0\w*' | sort | uniq > result.txt