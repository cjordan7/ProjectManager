#!/bin/bash

JAVA_VERSION_8=`/usr/libexec/java_home -v 1.8`
JAVA_VERSION=`/usr/libexec/java_home -v $1`

case "$1" in
    "8")
        export JAVA_HOME=$JAVA_VERSION_8
        ;;
    "9")
        export JAVA_HOME=$JAVA_VERSION
        ;;
    "10")
        export JAVA_HOME=$JAVA_VERSION
        ;;
    "11")
        export JAVA_HOME=$JAVA_VERSION
        ;;
    "12")
        export JAVA_HOME=$JAVA_VERSION
        ;;
    *)
        echo "Unknown java version! Specify 8, 9, 10, 11 or 12!"
        ;;
