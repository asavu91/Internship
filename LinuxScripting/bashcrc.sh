#!/bin/bash

source="bashcrc.txt"
destination="bashcrc"


fields=("ARTIFACTORY_API_KEY" "ARTIFACTORY_USER" "ANDROID_HOME" "JAVA_HOME" "IVI_ADB_SERIAL")

for field in "${fields[@]}"; do
	value_bashcrc=$(grep "$field=" bashcrc | cut -d '=' -f 2)
	value_bashcrc_txt=$(grep "$field=" bashrc.txt | cut -d '=' -f 2)

	if [ -z "$value_bashcrc" ]; then

	sed -i "s/$field=$value_bashcrc_txt/$field=$value_bashcrc_txt/" bashcrc

echo "Replace complete"
	fi
done
