current_path=`pwd`

echo $current_path


reports_path=$current_path/reports

echo $reports_path

dest_path=$HOME/results/$TDDIUM_SESSION_ID/session/

echo $dest_path

ls $dest_path

cp reports_browser.html $dest_path

cp -rf $reports_path $dest_path 

echo '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

pep8_rpt=$current_path/reports/diff_quality_pep8.html

cp -rf $pep8_rpt $dest_path.diff_quality_pep8.html

echo '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'


echo '*************************************'

ls $dest_path


echo 'DONE'
