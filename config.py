import os


def exec_cmd(cmd):
    print("\n>>> " + cmd)
    #input("Press Enter")
    os.system(cmd)

removable = False
format_home = False
format_efi = True
swap_size = 16 # GB
efi = "/dev/sda5"
root = "/dev/sda6"
home = "/dev/sda6"

cpu = "intel"
# cpu = "amd"

hostname = "hal"
username = "partha"

services = [
    "acpid.service",
    "NetworkManager.service",
    "avahi-daemon.service",
    # "gdm.service",
    "bluetooth.service",
    "lightdm.service",
    "cups.service",
    "fstrim.timer",
    
    #"nvidia-suspend.service",
    #"nvidia-resume.service",
    #"nvidia-hibernate.service",
    #"ntpd.service",
]

packages = [
    # bootloader
    # ==========
    "grub",
    "efibootmgr",
    "os-prober",

    # network manager
    # ===============
    "networkmanager",
    # "network-manager-applet",

    # console programs
    # ================
    "bash-completion",
    #"ranger",
    "p7zip",
    "xclip",

    # file sharing
    # ==================================
    "grsync",
    "wget",
    # "aria2",
    # "youtube-dl",
    "yt-dlp",
    "uget",
    # "filezilla",
    # "deluge",
    # "python-cairo",

    # xorg
    # ====
    "xorg",
    # "xorg-xinit",
    # "xorg-server",
    # "xorg-xbacklight",

    # window managers
    # ===============
    # BSPWM
    # =====
    # "bspwm",
    # "sxhkd",
    # "feh",
    # "lightdm",
    # "lightdm-gtk-greeter",
    # "xclip",
    # "rxvt-unicode",
    # "pcmanfm",
    # "xarchiver",
    # "kupfer",

    # desktop environments
    # ====================
    # GNOME
    # =====
    # "gnome",
    # "gnome-extra",
    # XFCE
    # ====
    "xfce4",
    "xfce4-goodies",
    "xarchiver",
    "caja",
    "network-manager-applet",
    "lightdm",
    "lightdm-gtk-greeter",
    # MATE
    # ====
    # "mate",
    # "mate-extra",
    # "lightdm",
    # "lightdm-gtk-greeter",
    # KDE
    # ===
    # "plasma",
    # "kde-applications",
    # "sddm",
    # "packagekit-qt5",


    # video drivers
    # =============
    # "xf86-video-amdgpu",
    
    # "nvidia-dkms", 
    # "nvidia-utils", 
    # "nvidia-settings", 
    # "nvidia-prime",

    "mesa",
    "lib32-mesa",
    "vulkan-intel",
    "lib32-vulkan-intel",
    "xf86-video-intel",
    
    # sound server
    # ============
    "pulseaudio",
    "pulseaudio-alsa",
    # "pulseaudio-bluetooth",
    # "alsa-utils",
    # "alsa-plugins",

    # file systems
    # ============
    "dosfstools",
    "mtools",
    "mtpfs",
    "ntfs-3g",
    "gvfs",

    # text editors
    # ============
    # "nano",
    # "neovim",
    "emacs",
    # "code",
    # "atom",

    # web browsers
    # ============
    # "w3m",
    "firefox",
    # "vivaldi",
    # "chromium",

    # audio/video players
    # ===================
    "mplayer",
    "vlc",

    # fonts
    # =====
    "fontconfig",
    "noto-fonts-emoji",
    # "ttf-dejavu",
    # "ttf-inconsolata", "ttf-fira-mono", "ttf-fira-code", "ttf-dejavu",
    # "ttf-roboto", "noto-fonts", "ttf-ubuntu-font-family", "gnu-free-fonts",
    # "adobe-source-code-pro-fonts", "ttf-linux-libertine",

    # graphics tools
    # ==============
    "inkscape",
    "gimp",
    "blender",
    "krita",
    "obs-studio",

    # doc tools
    # =========
    "texlive-basic",
    "texlive-latex",
    "texlive-latexrecommended",
    "texlive-latexextra",
    "texlive-binextra",
    "texlive-fontsrecommended",
    "texlive-fontsextra",
    "texlive-xetex",
    "texlive-luatex",
    "texlive-bibtexextra",
    
    "pandoc",
    "calibre",
    "libreoffice-fresh", "libreoffice-extension-writer2latex",
    # "zathura", "zathura-pdf-poppler", "zathura-djvu", "zathura-ps",
    # "okular",
    "evince",
    "xournalpp",

    # misc
    # ====
    # "nodejs",
    # "npm",
    # "python-pynvim",
    # "redshift",
    "catfish",
    "synapse",
    "python-virtualenv",
    "keepassxc",
    "gparted",
    "neofetch",
    "baobab",
    
    "acpid",
    "bluez",
    "bluez-utils",
    "cups",
    "asusctl",
    "archlinux-keyring",
    "arch-install-scripts",
    "ntp",
]

aur = [
    "google-chrome",
    "dropbox",
    "write_stylus",
    "spotify",
    "zoom",
    "miniconda3",
    "visual-studio-code-bin",
    "jabref",
    "mint-themes",
    "mint-y-icons",
    "texmacs-qt",
    "cpupower-gui",
    #"anki",
    # "x2goclient",
]
