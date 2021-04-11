Name:           samarux-desktop-i3-skel
Version:        0.1
Release:        27
Summary:        samarux-desktop-i3 skeleton files for i3, polybar et al
License:        GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Packager: 	Enrique Gil (mahoul@gmail.com)
BuildArch:	noarch
BuildRequires:	rsync

%description
Skeleton files for the samarux-desktop-i3 (i3 + gnome-flashback + 
dunst + polybar + rofi)
Most of the files for this are minimal tweaked versions from files
from the awesome Regolith project (https://regolith-linux.org/)


%prep
#[ -d %{name} ] && rm -Rfv %{name}
#[ -d %{_topdir}/SOURCES ] && rsync -avP --exclude '.git' --delete %{_topdir}/SOURCES/ .
%autosetup

%install
%{__install} -D -m644 etc/skel/.config/i3/config %{buildroot}/etc/skel/.config/i3/config
%{__install} -D -m644 etc/skel/.config/dunst/dunstrc %{buildroot}/etc/skel/.config/dunst/dunstrc
%{__install} -D -m644 etc/skel/.config/rofi/Adapta-Nokto.rasi %{buildroot}/etc/skel/.config/rofi/Adapta-Nokto.rasi
%{__install} -D -m644 etc/skel/.config/rofi/Pop-Dark.rasi %{buildroot}/etc/skel/.config/rofi/Pop-Dark.rasi
%{__install} -D -m644 etc/skel/.config/rofi/clean.rasi %{buildroot}/etc/skel/.config/rofi/clean.rasi
%{__install} -D -m644 etc/skel/.config/rofi/colors.rasi %{buildroot}/etc/skel/.config/rofi/colors.rasi
%{__install} -D -m644 etc/skel/.config/rofi/config %{buildroot}/etc/skel/.config/rofi/config
%{__install} -D -m644 etc/skel/.config/rofi/gruvbox-common.inc.rasi %{buildroot}/etc/skel/.config/rofi/gruvbox-common.inc.rasi
%{__install} -D -m644 etc/skel/.config/rofi/gruvbox-dark.rasi %{buildroot}/etc/skel/.config/rofi/gruvbox-dark.rasi
%{__install} -D -m644 etc/skel/.config/rofi/powermenu.rasi %{buildroot}/etc/skel/.config/rofi/powermenu.rasi
%{__install} -D -m644 etc/skel/.config/rofi/rofi.rasi %{buildroot}/etc/skel/.config/rofi/rofi.rasi
%{__install} -D -m644 etc/skel/.config/picom/picom.conf		 %{buildroot}/etc/skel/.config/picom/picom.conf
%{__install} -D -m644 etc/skel/.config/polybar/config		 %{buildroot}/etc/skel/.config/polybar/config
%{__install} -D -m644 etc/skel/.config/autostart/volumeicon.desktop		 %{buildroot}/etc/skel/.config/autostart/volumeicon.desktop

%clean

%files
%defattr(-, root, root)
/etc/skel/.config/i3/config
/etc/skel/.config/dunst/dunstrc
/etc/skel/.config/rofi/Adapta-Nokto.rasi
/etc/skel/.config/rofi/Pop-Dark.rasi
/etc/skel/.config/rofi/clean.rasi
/etc/skel/.config/rofi/colors.rasi
/etc/skel/.config/rofi/config
/etc/skel/.config/rofi/gruvbox-common.inc.rasi
/etc/skel/.config/rofi/gruvbox-dark.rasi
/etc/skel/.config/rofi/powermenu.rasi
/etc/skel/.config/rofi/rofi.rasi
/etc/skel/.config/picom/picom.conf
/etc/skel/.config/polybar/config
/etc/skel/.config/autostart/volumeicon.desktop

%changelog
* Sun Apr 11 2021 Enrique Gil <mahoul@gmail.com> - 0.1-27
- Replaced prep section with autosetup

* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-26
- Renamed pkg to samarux-desktop-i3-skel

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-25
- Run samarux-looks.sh instead of kostix-look.sh

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-24
- Changed kostix-look.sh call from i3 to samarux-looks.sh

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-23
- Renamed package to samarux-desktop-skel and added galculator to scratchpad

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-22
- Disable volumeicon via skel autostart file

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-21
- Added volicon disabling desktop file in /etc/skel/.config/autostart

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-20
- Added volicon disabling desktop file in /etc/skel/.config/autostart

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-19
- Reset rofi theme to regolith one

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-18
- Fixed rofi launch bindsym entries

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-17
- Added set-bing-wallpaper.sh to i3 startup

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-16
- Added parcellite to i3 startup

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-15
- Launch mousepad in scratchpad instead of gedit

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-14
- Fixed system-fan-speed.sh script location

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-13
- Added samarux-look.sh script to i3 startup

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-12
- Added picom and polybar configs

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-11
- First package build

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-1
- Initial release.

