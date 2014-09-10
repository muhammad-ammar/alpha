current_path=`pwd`

echo $current_path

reports_path=$current_path/reports

echo $reports_path

dest_path=$HOME/results/$TDDIUM_SESSION_ID/session/

echo $dest_path

cp -rf $reports_path $dest_path 

