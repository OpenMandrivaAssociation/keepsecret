%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Name:		keepsecret
Version:	26.08.1
Release:	1
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Password manager for Secret Service
URL:		https://apps.kde.org/keepsecret/
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KirigamiAppComponents)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	qml(org.kde.kirigamiaddons.formcard)
BuildRequires:	qml(org.kde.kirigami.actioncollection)

%description
KeepSecret is a password manager that talks to a Secret Service
compatible provider.

%files -f %{name}.lang
%{_bindir}/keepsecret
%{_datadir}/applications/org.kde.keepsecret.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.keepsecret.svg
%{_datadir}/metainfo/org.kde.keepsecret.metainfo.xml
%{_datadir}/qlogging-categories6/keepsecret.*
