#!/bin/sh

# Check for repository path.
if [ -z "$1" ]
then
	echo Specify 86Box repository path. ImageMagick is required.
	exit 1
fi

# Determine the ImageMagick executable.
magick=magick
$magick >/dev/null 2>&1 || magick=magick.exe

# Convert icons to PNG.
for i in "$1/src/win/icons/"*.ico
do
	$magick convert "$i" "usage/images/$(basename $i | sed -e 's/.ico$//').png"
done

# Remove unnecessary icons.
cd usage/images
rm -f 86Box-* *_empty* *_active* *_disabled* *-1.png *-2.png

# Get small and big icons.
for i in *-0.png
do
	mv "$i" "$(echo $i | sed -e 's/-0/_small/')"
done
for i in *-3.png
do
	mv "$i" "$(echo $i | sed -e 's/-3//')"
done
for i in *-4.png
do
	mv "$i" "$(echo $i | sed -e 's/-4//')"
done

# Create include.rst entries.
for i in *.png
do
	echo '.. |'$(echo $i | sed -e 's/.png//')'| image:: /usage/images/'$i
done
