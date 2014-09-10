import os
import shutil

full_path = os.path.realpath(__file__)
source_path = full_path.replace("post_worker.py", "reports/diff_quality_pep8.html")

reports_path = full_path.replace("post_worker.py", "reports/")


print "full_path:", full_path
print "source dir:", source_path


session_path = os.path.join(
    os.environ['HOME'],
    'results',
    os.environ['TDDIUM_SESSION_ID'],
    'session')

file_dest = os.path.join(session_path, 'diff_quality_pep8.html')

print 'copying diff_quality_pep8.html to:', file_dest
shutil.copyfile(source_path, file_dest)

shutil.copytree(reports_path, session_path)

# finding if there is any screenshot or log file
#print 'attaching failed screenshots and logs (if any)'
#for (path, dirs, files) in os.walk('test_root/log'):
#    for filename in files:
#        if filename.find('png') != -1 or filename.find('log') != -1:
#            filepath = os.path.join(path, filename)
#            print 'copying file:', filepath
#            destpath = os.path.join(session_path, filename)
#            print 'destination:', destpath
#            shutil.copyfile(filepath, destpath)

print 'TDDIUM_SESSION_ID:', os.environ['TDDIUM_SESSION_ID']
