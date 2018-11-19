#!/bin/bash  
#====================================================
#
#          FILE: install.sh
# 
#         USAGE: ./install.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Brett Salemink (BS), admin@roguedesigns.us
#  ORGANIZATION: Rogue Designs
#       CREATED: 11/19/2018 00:05
#      REVISION:  ---
#====================================================
set -o nounset                              # Treat unset variables as an error

SOFTWAREINSTALL="python-pip"


function InstallerDeb ()
{
	sudo apt-get update -y && sudo apt-get upgrade -y
	sudo apt-get install $SOFTWAREINSTALL
}	# End Function

function InstallerArch ()
{
	sudo pacman -S $SOFTWAREINSTALL
}	# End Function

function InstallerGentoo ()
{
	sudo emerge $SOFTWAREINSTALL --autounmask-write
	sudo etc-update
	sudo emerge $SOFTWAREINSTALL
}	# End Function

function Proceed ()
{
	echo "This will install "$SOFTWAREINSTALL
	echo "Do you want to proceed? [Y/n]"
	read PROCEED

	case $PROCEED in
		"Y"|"y")
		WhichDistro
		;;
		"N"|"n")
		exit 0
		;;
		*)
		WhichDistro
		;;
	esac
}	# End Function

function WhichDistro ()
{
	echo "Which Distro are you installing to? [1.Debian-based 2.Arch-based 3.Gentoo-based 4.Exit]"
	read DISTRO
	case $DISTRO in
		1)
		InstallerDeb
		;;
		2)
		InstallerArch
		;;
		3)
		InstallerGentoo
		;;
		4)
		exit 0
		;;
		*)
		echo "You need to pick one of the 3 distros. Option [1,2,3]"
		WhichDistro
		;;
	esac
}	# End Function

function InstallApprise()
{
	sudo pip install apprise
}	# end function

function Main ()
{
	Proceed
	InstallApprise
}	# End Function

Main

#=== Exit ===
exit 0
