%define debug_package %{nil}

Name: kinit
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Process launcher to speed up launching KDE applications
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
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
BuildRequires: ninja

%description
Process launcher to speed up launching KDE applications

%package devel
Summary: Development files for KInit
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
CMake files applications can use to determine where KInit
is installed.

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/*
%{_libdir}/libexec/kf5/*
%{_datadir}/dbus-1/interfaces/*
%{_mandir}/man8/*
%{_libdir}/libkdeinit5_klauncher.so

%files devel
%{_libdir}/cmake/KF5Init
