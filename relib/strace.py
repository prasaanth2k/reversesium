import subprocess
import shlex
from rich import print

MEMORY = "brk,mmap,munmap,mprotect,mremap,msync,mlock,mlockall,munlock,munlockall,madvise,mmap2"
FILEACCESS = "open,read,write,close,lseek,stat,fstat,lstat,openat,newfstatat,readlink,readlinkat,mkdir,rmdir,unlink,unlinkat,rename,renameat,truncate,ftruncate,chmod,fchmod,chown,fchown,lchown,access,faccessat,getcwd,chdir,fchdir"
NETWORK = "socket,connect,accept,send,recv,sendto,recvfrom,sendmsg,recvmsg,bind,listen,shutdown,getsockname,getpeername,socketpair,setsockopt,getsockopt,ioctl"
PROCESS = "fork,vfork,execve,waitid,waitpid,exit,kill,getpid,getppid,getuid,geteuid,getgid,getegid,setuid,setgid,setpgid,setsid,setreuid,setresuid,setresgid,ptrace,clone,execveat,prctl"
INTERPROCESSCOMMUNICATION = "pipe,pipe2,shmget,shmat,shmctl,semget,semop,semctl,msgget,msgsnd,msgrcv,msgctl,ipc"
TIMEMANAGEMENT = "time,gettimeofday,settimeofday,clock_gettime,clock_settime,clock_getres,nanosleep,alarm,setitimer,getitimer"
SYSTEMINFORMATION = "uname,sysinfo,sethostname,sethostname,setdomainname"
SIGNALS = "kill,tkill,tgkill,pause,rt_sigaction,rt_sigprocmask,rt_sigpending,rt_sigqueueinfo,rt_tgsigqueueinfo,rt_sigtimedwait,rt_sigsuspend,rt_sigreturn,sigaltstack,signalfd,signalfd4,eventfd,eventfd2,restart_syscall"
RESOURCEMANAGEMENT = "getrlimit,setrlimit,getrusage,prlimit64,sched_setparam,sched_getparam,sched_setscheduler,sched_getscheduler,sched_yield,sched_get_priority_max,sched_get_priority_min,sched_rr_get_interval,nice"
THREADINGMANAGEMENT = "clone,futex,set_tid_address,tgkill"
DEVICEMANAGEMENT = "ioctl,mknod,mknodat,fchmodat,fchownat,read,write"
EVENTMANAGEMENT = "epoll_create,epoll_ctl,epoll_wait,poll,select"
OTHERS = "reboot,kexec_load,syslog,acct,capget,capset,personality,sysfs"

class STRACE:
    def tracer(self,cmd):
        categorylist = [MEMORY,FILEACCESS,NETWORK,PROCESS,INTERPROCESSCOMMUNICATION,TIMEMANAGEMENT,SYSTEMINFORMATION,SIGNALS,RESOURCEMANAGEMENT,THREADINGMANAGEMENT,DEVICEMANAGEMENT,EVENTMANAGEMENT,OTHERS]
        for category in categorylist:
            cmd_list = shlex.split(cmd)
            stracecommand = ["strace", "-n", "-e", f"trace={category}"] + cmd_list
            output = subprocess.run(stracecommand, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
            if category == MEMORY:
                print(f"[bold white]-------------|MEMORY|------------[/bold white]")
                print(f"[bold white]{output.stderr}[/bold white]")
            elif category == FILEACCESS:
                print(f"[bold purple]-------------|fileaccess|------------[/bold purple]")
                print(f"[bold purple]{output.stderr}[/bold purple]")
            elif category == NETWORK:
                print(f"[bold green]-------------|network|------------[/bold green]")
                print(f"[bold green]{output.stderr}[/bold green]")
            elif category == PROCESS:
                print(f"[bold cayn]-------------|process|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == INTERPROCESSCOMMUNICATION:
                print(f"[bold cayn]-------------|IPC|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == TIMEMANAGEMENT:
                print(f"[bold cayn]-------------|TIME|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == SYSTEMINFORMATION:
                print(f"[bold cayn]-------------|SYSINFO|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == SIGNALS:
                print(f"[bold cayn]-------------|SIGNALS|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == RESOURCEMANAGEMENT:
                print(f"[bold cayn]-------------|RESOURCE|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == THREADINGMANAGEMENT:
                print(f"[bold cayn]-------------|Thread|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == DEVICEMANAGEMENT:
                print(f"[bold cayn]-------------|Device|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == EVENTMANAGEMENT:
                print(f"[bold cayn]-------------|Event|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")
            elif category == OTHERS:
                print(f"[bold cayn]-------------|reboot,kexec_load,syslog,acct,capget,capset,personality,sysfs|------------[/bold cayn]")
                print(f"[bold cayn]{output.stderr}[/bold cayn]")


    def filtered_tracer(self, cmd, category):
        cmd_list = shlex.split(cmd)
        stracecommand = ["strace","-n","-e", f"trace={category}"] + cmd_list
        output = subprocess.run(stracecommand, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        if category == MEMORY:
            print(f"[bold white]-------------|MEMORY|------------[/bold white]")
            print(f"[bold white]{output.stderr}[/bold white]")
        elif category == FILEACCESS:
            print(f"[bold purple]-------------|fileaccess|------------[/bold purple]")
            print(f"[bold purple]{output.stderr}[/bold purple]")
        elif category == NETWORK:
            print(f"[bold green]-------------|network|------------[/bold green]")
            print(f"[bold green]{output.stderr}[/bold green]")
        elif category == PROCESS:
            print(f"[bold cayn]-------------|process|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == INTERPROCESSCOMMUNICATION:
            print(f"[bold cayn]-------------|IPC|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == TIMEMANAGEMENT:
            print(f"[bold cayn]-------------|TIME|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == SYSTEMINFORMATION:
            print(f"[bold cayn]-------------|SYSINFO|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == SIGNALS:
            print(f"[bold cayn]-------------|SIGNALS|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == RESOURCEMANAGEMENT:
            print(f"[bold cayn]-------------|RESOURCE|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == THREADINGMANAGEMENT:
            print(f"[bold cayn]-------------|Thread|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == DEVICEMANAGEMENT:
            print(f"[bold cayn]-------------|Device|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == EVENTMANAGEMENT:
            print(f"[bold cayn]-------------|Event|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
        elif category == OTHERS:
            print(f"[bold cayn]-------------|reboot,kexec_load,syslog,acct,capget,capset,personality,sysfs|------------[/bold cayn]")
            print(f"[bold cayn]{output.stderr}[/bold cayn]")
