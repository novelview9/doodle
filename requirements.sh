pip install -r requirements.txt

for i in $(ls -d */);
do
  requirements_file_path=${i%%/}/requirements.txt
  echo $requirements_file_path
  if [ -f $requirements_file_path ]
  then
    exec pip install -r $requirements_file_path
  fi
done
