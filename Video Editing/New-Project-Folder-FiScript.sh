
set -euf -o pipefail
#----- INSERT YOUR PATHS HERE -----
LOCAL_MOUNT_POINT="/Volumes/SSD nvme USB-C"
TEMPLATE_PATH="/Users/JFtech/Desktop/YouTube/Template"
#----------------------------------
PROJECT_PATH=$PATH
name="$(basename -- "$PROJECT_PATH")"
if [ -e "$PROJECT_PATH"/"$name".fcpbundle ]; then
  echo "exist"
else
  echo "NOT exist"
  TEMPLATEPATH="$(printf '%q\n' "$TEMPLATE_PATH")"
  LOCALMOUNTPOINT="$(printf '%q\n' "$LOCAL_MOUNT_POINT")"
  #FOLDERPATH="$(printf '%q\n' "$PROJECT_PATH")"
  cp -a "$TEMPLATEPATH"/. "$PROJECT_PATH"
  mv "$PROJECT_PATH"/Template.fcpbundle "$PROJECT_PATH"/"$name".fcpbundle
  mv "$PROJECT_PATH"/Template.pages "$PROJECT_PATH"/"$name".pages
  if mount | grep "on $LOCALMOUNTPOINT" > /dev/null; then
    mv "$PROJECT_PATH" "$LOCAL_MOUNT_POINT"
    open "$LOCAL_MOUNT_POINT"
  fi
fi
