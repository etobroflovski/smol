#!/bin/bash

counter=$1

until [ $counter -gt $2 ]
do
  ##echo Counter: $counter
 ./manga_dl.sh $3/$counter dl_$counter makecbz
  ((counter++))
done
