#!/bin/bash


if [ $# -ne 3 ]
then
	echo make_arff.sh path target_path basedir
 	exit
fi

path=$1
target_path=$2
BASEDIR=$3
#check data is lie 


#check sit or walk
echo "checking sit or walk..."
find $path -maxdepth 1 -type f   |  xargs -i python $BASEDIR/check_sit_or_walk.py {} | cat > $BASEDIR/files
cat $BASEDIR/files | awk -F/ '{print $0 , "imei"}' > $BASEDIR/log
python $BASEDIR/determine.py 0.5

if [ ! -d "$target_path" ]
then 
	mkdir -p $target_path
fi

mkdir $target_path/walk
mkdir $target_path/sit

while read file  state
do
        echo "make arff..."
	filename=`basename $file`
	python $BASEDIR/make_arff.py $file 1 $state > $target_path/$state/$filename.arff
done < $BASEDIR/out

#rm $BASEDIR/log
#rm $BASEDIR/out
#rm $BASEDIR/files




