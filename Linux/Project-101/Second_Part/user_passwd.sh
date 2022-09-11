#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

read -p "Enter the username (login): " USER_NAME
read -p "Enter the real name (first and last name): " COMMENT
read -p "Enter the password: " PASSWORD
useradd -c "${COMMENT}" -m ${USER_NAME}
if [ $? -eq 0 ]; then
    echo "User account created."
else
    echo "User account not created."
    exit 1
fi
echo ${PASSWORD} | passwd --stdin ${USER_NAME}
if [ $? -eq 0 ]; then
    echo "Password set for user ${USER_NAME}."
else
    echo "Password not set for user ${USER_NAME}."
    exit 2
fi
passwd -e ${USER_NAME}
echo "Username: ${USER_NAME}"
echo "Host: ${HOSTNAME}"
exit 0