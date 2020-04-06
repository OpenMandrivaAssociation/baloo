# filter bad requires on private lib
%define __noautoreq 'devel\\(libKF5BalooEngine.*'
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Baloo is a framework for searching and managing metadata
Name:		baloo
Version:	5.69.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/baloo-%{version}.tar.xz
Patch0:		baloo-5.67.0-default-off.patch
Patch1:		baloo-5.13.0-pkgconfig.patch
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	lmdb-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
# (tpg) https://issues.openmandriva.org/show_bug.cgi?id=865
Requires:	qt5-database-plugin-sqlite
Requires:	kfilemetadata
%rename	%{name}5

%description
Baloo is a framework for searching and managing metadata.

%files -f baloo_file5.lang -f baloo_file_extractor5.lang -f balooctl5.lang -f baloomonitorplugin.lang -f baloosearch5.lang -f balooshow5.lang -f kio5_baloosearch.lang -f kio5_tags.lang -f kio5_timeline.lang -f baloodb5.lang -f balooengine5.lang
%{_datadir}/qlogging-categories5/baloo.categories
%{_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_bindir}/baloo_file
%{_bindir}/baloo_file_extractor
%{_bindir}/balooctl
%{_bindir}/baloosearch
%{_bindir}/balooshow
%{_datadir}/dbus-1/interfaces/org.kde.BalooWatcherApplication.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.fileindexer.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.main.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.scheduler.xml
%{_libdir}/qt5/plugins/kf5/kded/baloosearchmodule.so
%{_libdir}/qt5/plugins/kf5/kio/baloosearch.so
%{_libdir}/qt5/plugins/kf5/kio/tags.so
%{_libdir}/qt5/plugins/kf5/kio/timeline.so
%{_datadir}/kservices5/baloosearch.protocol
%{_datadir}/kservices5/tags.protocol
%{_datadir}/kservices5/timeline.protocol
%{_libdir}/qt5/qml/org/kde/baloo

#----------------------------------------------------------------------------

%define baloo_major 5
%define libbaloo %mklibname KF5Baloo %{baloo_major}

%package -n %{libbaloo}
Summary:	Baloo Core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname KF5BalooCore 1}
Obsoletes:	%{mklibname KF5BalooFiles 1}
Obsoletes:	%{mklibname KF5BalooNaturalQueryParser 1}
Obsoletes:	%{mklibname KF5Baloo 1} < 5.13.0

%description -n %{libbaloo}
Baloo Core library

The core library of the Baloo file indexing service.

%files -n %{libbaloo}
%{_libdir}/libKF5Baloo.so.%{baloo_major}
%{_libdir}/libKF5Baloo.so.%{version}

#----------------------------------------------------------------------------

%define balooengine_major 5
%define libbalooengine %mklibname KF5BalooEngine %{balooengine_major}

%package -n %{libbalooengine}
Summary:	Plasma searching and managing metadata shared library
Group:		System/Libraries

%description -n %{libbalooengine}
Plasma searching and managing metadata shared library.

%files -n %{libbalooengine}
%{_libdir}/libKF5BalooEngine.so.%{balooengine_major}
%{_libdir}/libKF5BalooEngine.so.%{version}

#----------------------------------------------------------------------------

%define devbaloo %mklibname baloo5 -d

%package -n %{devbaloo}
Summary:	Development files for Baloo
Group:		Development/KDE and Qt
Requires:	%{libbaloo} = %{EVRD}
Requires:	%{libbalooengine} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloo}
This package contains header files needed if you wish to build applications
based on Baloo.

%files -n %{devbaloo}
%{_includedir}/KF5/Baloo/
%{_includedir}/KF5/baloo_version.h
%{_libdir}/qt5/mkspecs/modules/qt_Baloo.pri
%{_libdir}/*.so
%{_libdir}/cmake/KF5Baloo
%{_libdir}/pkgconfig/Baloo.pc

#--------------------------------------------------------------------
%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devbaloo} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
#--------------------------------------------------------------------

%prep
%autosetup -p1 -n baloo-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# FIXME workaround for gdb hang while trying to extract debuginfo
# from baloo_file_extractor with gdb 8.3.1-3 on x86_64 and znver1
strip --strip-unneeded %{buildroot}%{_bindir}/baloo_file_extractor

%find_lang baloo_file5
%find_lang baloo_file_extractor5
%find_lang balooctl5
%find_lang baloodb5
%find_lang balooengine5
%find_lang baloomonitorplugin
%find_lang baloosearch5
%find_lang balooshow5
%find_lang kio5_baloosearch
%find_lang kio5_tags
%find_lang kio5_timeline
