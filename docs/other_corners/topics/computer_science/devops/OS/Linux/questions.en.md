# Questions

## Resource Management

1.  How can we see the cpu usage?

    - how can we see the memory usage?

      You can use the vmstat, top, htop, or ps commands to view processes sorted by resource usage.  
      To display the top 5 processes by memory usage:

      ```bash
      ps aux --sort=-%mem | head -n 6
      ```

2.  What is load average?

    - How can you see it?

      To view system uptime and load averages:

      ```bash
      uptime
      ```

3.  What is swap and how to see it?

    - What are the best practices with swap?

      To check memory and swap usage:

      ```bash
      free -h
      ```

---

## File System

1.  What is a file system?

2.  How to create a new file system?

3.  How to see all the mount points?

4.  How to mount and unmount file systems?

5.  What is the fstab file?

6.  What is inode?

7.  What is the difference between a hard link and a soft (symbolic) link?

    A hard link is a direct reference to the file’s inode. Changes made to a file are reflected in all hard links because they share the same inode.  
     A soft link (symbolic link) points to the file path rather than the inode. If the original file is deleted, the soft link becomes broken (invalid).

    To create a hard link:

    ```bash
    ln file1 <hardlink_name>
    ```

    To create a soft link:

    ```bash
    ln -s /path/to/file <symlink_name>
    ```

---

## Processes

1.  How to see all the processes that are running?

2.  How to get the PID of a process?

3.  How to kill a process?

    - What is the signal?

4.  How can I see wat the environment variables a process started with?

5.  What is a service?
    - How to create one?

---

## Storage

1. How do you check the disk usage of directories and files?

   You can use the du command to check disk usage of directories and files, and df to check disk space usage of the filesystem.  
    To check the disk space usage of the filesystem:

   ```bash
   df -h
   ```

   To display the disk usage of a directory:

   ```bash
   du -h <directory_path>
   ```

2. What is LVM?

---

## Networking

1.  How to see all the ports and their status?

    The netstat, ss, and lsof commands can be used to list open ports and their associated processes.  
     Using netstat:

    ```bash
    netstat -tuln
    ```

    Using ss (a more modern alternative to netstat):

    ```bash
    ss -tuln
    ```

    Using lsof to list open files and network connections:

    ```bash
    sudo lsof -i -P -n
    ```

2.  How to find which process is using a specific port?

3.  What is netfilter?

---

## Scheduling Scripts

1.  How to run a script with a schedule?
    - is there another way in addition to cronjob?

---

## Searching

1.  How do you search for a string in a file or a directory?

    The grep command is used to search for specific strings in files.  
     To search for a string in a file:

    ```bash
    grep "search_string" <file_name>
    ```

    To search for a string recursively in a directory:

    ```bash
    grep -r "search_string" <directory_path>
    ```

---

## Other

1.  What is the linux folder structure?

2.  What is systemd?
