%define major %(echo %{version} |cut -d. -f1)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Name: kinit
Version:	5.116.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Process launcher to speed up launching KDE applications
URL: https://kde.org/
License: GPL
Group: System/Libraries
Patch0: fpie.patch
BuildRequires: libcap-utils
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libcap)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5DBusAddons)

%description
Process launcher to speed up launching KDE applications.

%package devel
Summary: Development files for KInit
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
CMake files applications can use to determine where KInit
is installed.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major} --all-name --with-man

%files -f %{name}%{major}.lang
%{_datadir}/qlogging-categories5/*.*categories
%{_bindir}/*
%{_libdir}/libexec/kf5/klauncher
%caps(cap_sys_resource+ep) %{_libdir}/libexec/kf5/start_kdeinit
%{_libdir}/libexec/kf5/start_kdeinit_wrapper
%{_datadir}/dbus-1/interfaces/*
%{_libdir}/libkdeinit5_klauncher.so
%doc %{_mandir}/man8/*

%files devel
%{_libdir}/cmake/KF5Init
