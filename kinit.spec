%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kinit
Version:	5.48.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Process launcher to speed up launching KDE applications
URL: http://kde.org/
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
Requires(post): libcap-utils

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
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%post
%{_sbindir}/setcap "CAP_SYS_RESOURCE=+ep" %{_libdir}/libexec/kf5/start_kdeinit ||:

%files -f %{name}%{major}.lang
%{_bindir}/*
%{_libdir}/libexec/kf5/*
%{_datadir}/dbus-1/interfaces/*
%{_libdir}/libkdeinit5_klauncher.so
%{_mandir}/man8/*
%lang(ca) %{_mandir}/ca/man8/*
%lang(de) %{_mandir}/de/man8/*
%lang(es) %{_mandir}/es/man8/*
%lang(it) %{_mandir}/it/man8/*
%lang(nl) %{_mandir}/nl/man8/*
%lang(pt) %{_mandir}/pt/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
%lang(sv) %{_mandir}/sv/man8/*
%lang(uk) %{_mandir}/uk/man8/*

%files devel
%{_libdir}/cmake/KF5Init
