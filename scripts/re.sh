echo -e "\e[35m"
echo "██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗███████╗██╗██╗   ██╗███╗   ███╗"
echo "██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║██║   ██║████╗ ████║"
echo "██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗  ███████╗██║██║   ██║██╔████╔██║"
echo "██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝  ╚════██║██║██║   ██║██║╚██╔╝██║"
echo "██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗███████║██║╚██████╔╝██║ ╚═╝ ██║"
echo "╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝"
echo -e "\e[0m"

USERNAME=$(whoami)
HOSTNAME=$(hostname)
OS=$(lsb_release -ds)
HOST_MODEL=$(cat /sys/devices/virtual/dmi/id/product_name)
KERNEL=$(uname -r)
UPTIME=$(uptime -p | sed 's/up //')
PACKAGES=$(dpkg --get-selections | wc -l)
SHELL=$(bash --version | head -n 1)
CPU=$(lscpu | grep "Model name:" | sed 's/Model name:\s*//')
GPU=$(lspci | grep -i vga | cut -d: -f3)
MEMORY=$(free -h | grep Mem | awk '{print $3 " / " $2}')
echo -e "\033[1;32m"
echo "OS: $OS"
echo "Host: $HOST_MODEL"
echo "Kernel: $KERNEL"
echo "Uptime: $UPTIME"
echo "Packages: $PACKAGES"
echo "Shell: $SHELL"
echo "Resolution: $RESOLUTION"
echo "CPU: $CPU"
echo "GPU: $GPU"
echo "Memory: $MEMORY"
echo -e "\033[0m"