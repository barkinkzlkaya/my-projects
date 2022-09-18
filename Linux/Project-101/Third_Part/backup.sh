#!/bin/bash

# Check if we are root privilage or not
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
# Which files are we going to back up. Please make sure to exist /home/ec2-user/data file
files="/home/ec2-user/data, /etc, /boot, /usr"

# Where do we backup to. Please crete this file before execute this script
dest="/mnt/backup"

# Create archive filename based on time
time=$(date +"%Y_%m_%d_%I_%M_%p")
hostname=$(hostname -s)
archive_file="${hostname}-${time}.tgz"

# Print start status message.
echo "Backing up ${backup_files} to ${dest}/${archive_file}"
date
echo

# Backup the files using tar.
tar czf ${dest}/${archive_file} ${backup_files} # &> /dev/null (Bunu script birkaç kez calistirilip eklenebilir)

# Print end status message.
echo
echo "Backup finished"
date

# Long listing of files in $dest to check file sizes.
ls -lh $dest
# To set this script for executing in every 5 minutes, we'll create cronjob

# crontab -e
# */5 * * * * sudo /home/ec2-user/backup.sh