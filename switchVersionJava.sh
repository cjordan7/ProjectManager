#!/bin/bash
#!/usr/bin/env bash

path=$PWD

echo $PWD

cd ~

JAVA_COMMANDS_FILE=.bashJavaCommands
touch $JAVA_COMMANDS_FILE

> $JAVA_COMMANDS_FILE

if [ $1 -lt 8 ] || [ $1 -gt 12 ]
then
    echo "Unknown java version! Specify 8, 9, 10, 11 or 12!"
elif [ $1 -eq 8 ]
then
    echo export JAVA_HOME=`/usr/libexec/java_home -v 1.8` >> $JAVA_COMMANDS_FILE
    export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
else
    echo "export JAVA_HOME=`/usr/libexec/java_home -v $1`" >> $JAVA_COMMANDS_FILE
    #echo export JAVA_HOME=`/usr/libexec/java_home -v $1`
    export JAVA_HOME=`/usr/libexec/java_home -v $1`
fi

cd $path
#source ~/.bash_profile
#source ~/.bashrc
