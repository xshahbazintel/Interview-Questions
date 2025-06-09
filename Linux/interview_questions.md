What is Kernel? Explain its functions
kernel is a component that allows interaction between hardware and software components of os in linux. kernel is the first component that loads when system boots its also referred as low level system software
its functions include memory, process, device, storage and user managements.

What is LILO?
LILO means linux loader, which is a boot loader for linux based systems. Its main purpose is to load kernel into memory and trasfer control to it.

Guide me through the Linux boot process, i.e, from when you press the power button to when the Linux login prompt appears?

BIOS(Basic Input output initializes the hardware) which is stored in ROM  and it runs POST(Power On Self Test) 
which tests hardware,screen other devices connected this is performed for all os
the BIOS is loacted in ROM of motherboard 
once post is passed now bios will start booting process and search for Master Boot Record (MBR)
MBR is 512 bytes located on first set of hard disk of bootable device

MBR: Master Boot Record (MBR) may be found on the bootable disk's first sector. Usually found in dev/hda or dev/sda. It contains GRUB-related information (Grand Unified Bootloader). So, in a nutshell, the MBR loads and runs the GRUB boot loader.

GRUB: The default kernel image given in the grub configuration file is loaded by GRUB. /boot/grub/grub.conf is the location of the grub configuration file. It consists mostly of the kernel and the initrd image (initial ram disc - a method of loading a temporary root file system into memory). In a nutshell, GRUB loads and runs kernel and initrd images.

Kernel: The root file system is mounted, and the /sbin/init program is run. The process id of init is 1 since it is the first program to be executed by the kernel. To double-check, run ps -ef | grep init.

Init: Init determines the Linux run level by looking at the /etc/inittab file. In Linux, the following run levels are available:

what is softlink and hardlink?
softlink is a symbolic link that points to another file or directory
it has a different inode number than original file 
you can use softlink for directories
if the original is deleted or renamed the link will be broken

ln -s <source file path/directory> <target filepath/directory>


A hard link creates another reference to an existing inode (file) on the filesystem. Both the original file and the hard link share the same inode.

they cant be used for directories
ln <source> <target>


What is a File system in Linux? Explain different file system types in Linux?

A file system is a way of storing and organizing files on a disk/partition.
it provides a way for managing file and directories, also defines how data is stored, managed and accessed.
commonfile systems are ext4, ext3, ext2, xfs, ntfs, fat32

Write a Bash script that checks if a given process is running and prints a message accordingly.
#!/bin/bash

# Check if the process name is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <process_name>"
  exit 1
fi

# Store the process name
process_name="$1"

# Check if the process is running using pgrep
if pgrep -x "$process_name" > /dev/null; then
  echo "The process '$process_name' is running."
else
  echo "The process '$process_name' is not running."
fi

-z "string"	String has zero length
-n "string"	String has non-zero length


What is Zombie Process? Can Zombie Processes cause any issues or performance problems on a Linux system?

Hide Answer
A Zombie Process is a type of process that has completed its execution but still has an entry in the process table. In other words, it's a process that has terminated, but its parent process has not yet received its status. This usually happens when the parent process fails to invoke the wait system call after its child has completed execution. As a result, the operating system cannot remove the entry from the process table, and the terminated child process remains in a zombie state as a dormant process. Zombie processes occupy system resources and can lead to performance degradation if not taken care of in time.

Zombie Processes, by themselves, do not cause performance problems or issues on a Linux system. However, if a large number of zombies accumulate and are not reaped by their parent processes, they can consume entries in the process table, potentially leading to resource exhaustion.

Write a script that takes a directory path as an argument and lists all the files in that directory.

#!/bin/bash

# Check if a directory path is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

# Store the directory path
directory_path="$1"

# Check if the directory exists
if [ ! -d "$directory_path" ]; then
  echo "Error: '$directory_path' is not a valid directory."
  exit 1
fi

# List all files in the directory (excluding subdirectories)
echo "Listing all files in '$directory_path':"
find "$directory_path" -maxdepth 1 -type f


How would you create an ext4 file system?

Hide Answer
To create an ext4 file system, you can use the mkfs.ext4 or mke4fs command to format a partition with the ext4 file system type. Here's an example command to format a new partition with the ext4 file system using the mkfs.ext4 command:

sudo mkfs.ext4 /dev/sdX1

Replace sdX1 with the appropriate device name and partition number. Please note that this will erase all the data on the partition.



How do you find the top 10 largest files and directories on your Linux system?

sudo find / -type f -exec du -h {} + | sort -rh | head -n 10 #list top 10 file sizes in all directories

sudo du -h --max-depth=1 / | sort -rh | head -n 10 #lists top 10 directories

sudo du -ah / | sort -rh | head -n 10 #lists top 10 files and directories 

How do you set up a crontab to run a script every 15 minutes?

crontab -e #edits crontab

*/15 * * * * /path/to/your/script.sh

chmod +x /path/to/your/script.sh  #give permissions to execute script

crontab -l  #lists all crontab jobs 


How to search for the string "error" in files of a directory recursively?

grep -r "error" /path-to-directory
grep -r --include="*.log" "error" /path/to/directory/  #search for error in a directory recursively which ends with .log



find /path/to/directory/ -type f -exec grep -iH "error" {} \;
find /path/to/directory/ -type f -name "*.txt" -exec grep -H "error" {} \;


find all files in a directory which are older than 7 days?

find /path/to/directory -type f -mtime +7
find /path/to/directory -type f -name "*.log" -mtime +7  #file name that ends with .log

find all files created in last 7minutes?

find /path/to/directory -type f -mmin -7 


find all files recursively in a directory that ends with .html and replace string 123 with 456 in those files

find /directory_path -type f -name "*.html" -exec sed -i 's/123/456/g' {} \ ;

find all files plder than 7 days in a directories and remove them

find /path/to/directory -type f -mtime +7 -exec rm -f {} \;

What is the difference between a process and a thread in Linux? 
Processes are independent programs with their own memory space and resources, meaning each process is isolated from other processes. 
Thus, they offer a high level of security.
Threads, on the other hand, are units of execution that exist within a process. All threads within a process share the same resources. Multiple threads can be executed simultaneously, 
making them useful for tasks requiring cooperation and concurrency. 

how do you run a custom script when user logins to system automatically in linux
use 
~/.bash_profile
nano ~/.profile for non bash shells
or you can create a service and run 


what are the default permissions on a directory you create as a user 
When you create a directory as a user in Linux, the default permissions for the directory are determined by the system's umask value. The umask specifies the default permission settings for newly created files and directories.
defualt are 755, 


what is $@ and $?
$@: all arguments passed to a script
$?: exit status of last executed command


how do you troubleshoot ssh issues in linux?
there should be .ssh in user home directory with authorized_keys 
incorrect/corrupted key in authorized keys
incorrect permisions at folder or file level
file 600
folder 700 
check if sshd service is running 
run in verbose mode


how do you check which folder in partition has large size?
do df -h this will list all partitions with sizes, find largest partition
du -sh * find largest folder and find largest file 
truncate or delete it

i know i have a file in folder but i dont know path find it?
eg: find / -name httpd.conf

how do you check cpu and memory usage>
memory run: free -m
cpu: top or htop command
ps aux --sort=-%mem #sort with memory usage not realtime

how do you check all open listening ports in linux?
netstat -tulpn

-t tcp ports
-u udp ports
-l listening
-p process ids
-n numerical IP addresses and port numbers

how do you troubleshoot connection failed error between client and server
you have a nginx server running on linux machine how do you optimize performance
i have mounted a disk on linux now i have increased size of disk, what steps should i follow on machine now 