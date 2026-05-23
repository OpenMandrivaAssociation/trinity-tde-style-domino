%bcond clang 1

# TDE variables
%define tde_pkg tde-style-domino
%define tde_prefix /opt/trinity


# Required for Mageia and PCLinuxOS: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Domino widget style and twin decoration for TDE
Group:		Graphical desktop/TDE
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/themes/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:  trinity-tdelibs-devel >= %{version}
BuildRequires:  trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# JPEG support
BuildRequires:  pkgconfig(libjpeg)

BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
Domino is a style with a soft look. It allows to fine adjust the shininess
of the widgets by customizable color gradients.


%files -f %{name}.lang
%defattr(-,root,root)
%{tde_prefix}/%{_lib}/trinity/plugins/styles/domino.la
%{tde_prefix}/%{_lib}/trinity/plugins/styles/domino.so
%{tde_prefix}/%{_lib}/trinity/tdestyle_domino_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_domino_config.so
%{tde_prefix}/%{_lib}/trinity/twin3_domino.la
%{tde_prefix}/%{_lib}/trinity/twin3_domino.so
%{tde_prefix}/%{_lib}/trinity/twin_domino_config.la
%{tde_prefix}/%{_lib}/trinity/twin_domino_config.so
%{tde_prefix}/share/apps/tdedisplay/color-schemes/Domino.kcsrc
%{tde_prefix}/share/apps/tdestyle/themes/domino.themerc
%{tde_prefix}/share/apps/twin/domino.desktop

