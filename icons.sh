#!/bin/sh

# Check for repository path.
if [ -z "$1" ]
then
	echo Specify 86Box repository path. ImageMagick is required.
	exit 1
fi

# Determine the ImageMagick executable.
if convert -version 2>&1 | grep -q ImageMagick
then
	magick=
elif magick -version >/dev/null 2>&1
then
	magick=magick
else
	magick=$(ls /c/Program\ Files/ImageMagick-*/magick.exe)
	if ! "$magick" -version >/dev/null 2>&1
	then
		echo ImageMagick not found.
		exit 2
	fi
fi

# Convert icons to PNG.
for i in "$1/src/qt/icons/"*.ico
do
	"$magick" convert "$i" -set filename:size "%wx%h" "usage/images/$(basename $i | sed -e 's/.ico$//')-%[filename:size].png"
done

# Remove unnecessary icons.
cd usage/images
rm -f 86Box-* *active* *disabled* *mute*

# Get small and big icons.
for suffix in 8x8 256x256 128x128 64x64 32x32 16x16
do
	for i in *-$suffix.png
	do
		cp -a "$i" "$(echo $i | sed -e "s/-$suffix/_small/")"
		[ "$suffix" != "16x16" ] && mv "$i" "$(echo $i | sed -e "s/-$suffix//")"
	done
done
rm -f *-*[0-9]x[0-9]*.png
