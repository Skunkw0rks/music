#!/bin/bash
mongo --eval "DBQuery.shellBatchSize = 100;db.tracks.find().sort({_id:1}).limit(100).pretty().shellPrint();" viperial > $results
echo $results

