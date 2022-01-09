#!/bin/bash
curl -sI | grep "Content-Length" | cut -d' ' -f 2
