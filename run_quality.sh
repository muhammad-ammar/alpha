mkdir -p reports

diff-quality --violations=pep8 --html-report reports/diff_quality_pep8.html

bash ./post_worker.sh
