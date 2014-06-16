Summary:	Baloo is a framework for searching and managing metadata
Name:		baloo
Version:	4.13.2
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kfilemetadata-devel
BuildRequires:	xapian-devel
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(QJson)
# For kio_timeline.so and tags.protocol
Conflicts:	kdebase4-runtime < 1:4.13.0

%description
Baloo is a framework for searching and managing metadata.

%files
%{_sysconfdir}/dbus-1/system.d/org.kde.baloo.filewatch.conf
%{_kde_bindir}/akonadi_baloo_indexer
%{_kde_bindir}/baloo_file
%{_kde_bindir}/baloo_file_cleaner
%{_kde_bindir}/baloo_file_extractor
%{_kde_bindir}/balooctl
%{_kde_bindir}/baloosearch
%{_kde_bindir}/balooshow
%{_kde_datadir}/akonadi/agents/akonadibalooindexingagent.desktop
%{_kde_iconsdir}/hicolor/128x128/apps/baloo.png
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/kde4/akonadi/akonadi_baloo_searchplugin.so
%{_kde_libdir}/kde4/akonadi/akonadibaloosearchplugin.desktop
%{_kde_libdir}/kde4/libexec/kde_baloo_filewatch_raiselimit
%{_kde_services}/*.desktop
%{_kde_services}/*.protocol
%{_kde_servicetypes}/baloosearchstore.desktop
%{_datadir}/autostart/baloo_file.desktop
%{_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/dbus-1/system-services/org.kde.baloo.filewatch.service
%{_datadir}/polkit-1/actions/org.kde.baloo.filewatch.policy

#----------------------------------------------------------------------------

%define baloocore_major 4
%define libbaloocore %mklibname baloocore %{baloocore_major}

%package -n %{libbaloocore}
Summary:	Shared library for Baloo
Group:		System/Libraries
Requires:	baloo = %{EVRD}

%description -n %{libbaloocore}
Shared library for Baloo.

%files -n %{libbaloocore}
%{_kde_libdir}/libbaloocore.so.%{baloocore_major}*

#----------------------------------------------------------------------------

%define baloofiles_major 4
%define libbaloofiles %mklibname baloofiles %{baloofiles_major}

%package -n %{libbaloofiles}
Summary:	Shared library for Baloo
Group:		System/Libraries

%description -n %{libbaloofiles}
Shared library for Baloo.

%files -n %{libbaloofiles}
%{_kde_libdir}/libbaloofiles.so.%{baloofiles_major}*

#----------------------------------------------------------------------------

%define baloopim_major 4
%define libbaloopim %mklibname baloopim %{baloopim_major}

%package -n %{libbaloopim}
Summary:	Shared library for Baloo
Group:		System/Libraries

%description -n %{libbaloopim}
Shared library for Baloo.

%files -n %{libbaloopim}
%{_kde_libdir}/libbaloopim.so.%{baloopim_major}*

#----------------------------------------------------------------------------

%define balooxapian_major 4
%define libbalooxapian %mklibname balooxapian %{balooxapian_major}

%package -n %{libbalooxapian}
Summary:	Shared library for Baloo
Group:		System/Libraries

%description -n %{libbalooxapian}
Shared library for Baloo.

%files -n %{libbalooxapian}
%{_kde_libdir}/libbalooxapian.so.%{balooxapian_major}*

#----------------------------------------------------------------------------

%define devbaloo %mklibname baloo -d

%package -n %{devbaloo}
Summary:	Devel stuff for Baloo
Group:		Development/KDE and Qt
Requires:	%{libbalooxapian} = %{EVRD}
Requires:	%{libbaloopim} = %{EVRD}
Requires:	%{libbaloofiles} = %{EVRD}
Requires:	%{libbaloocore} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloo}
This package contains header files needed if you wish to build applications
based on Baloo.

%files -n %{devbaloo}
%{_kde_includedir}/baloo/
%{_kde_libdir}/*.so
%{_kde_libdir}/cmake/Baloo

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Mon Jun 16 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-2
- Add baloo to libbaloocore's Requires

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- Initial Rosa package
