#!/bin/bash

echo 'propagate parent data analysis config file into each directory to be analyzed'

for fname in $VIDEO_SRC*
do
	# strip the directory and extension from the filename
	id="${fname##*/}" # includes extension
	id="${id%.*}"

	# copy parameters for the video into each video /src folder
	cp -r "$CONFIG_SRC/config_parent.py" "$DESTINATION$id/data/"

	# rename config file to same name as the hdf5 file
	# mv filename_original filename_new
	cd "$DESTINATION$id/data/"
	val=$(ls -1 | grep '.hdf5$' |wc -l)
	if [ "$val" -eq "1" ]; then
		new_id=$(ls -1 | grep '.hdf5$')
		new_id="${new_id##*/}"
		new_id="${new_id%.*}"
		new_id=${new_id:0:18}
		new_id="config_$new_id.py"
		mv $DESTINATION$id/data/config_parent.py $DESTINATION$id/data/$new_id
	else
		echo -e "\033[31m More than one hdf5 file in $id\033[0m"
	fi
done
