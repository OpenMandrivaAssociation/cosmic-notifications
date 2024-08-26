
%define         appname com.system76.CosmicNotifications
Name:           cosmic-notifications
Version:        1.0.0
Release:        0.alpha1.0
Summary:        Layer for COSMIC Notifications
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/cosmic-notifications
Source0:        https://github.com/pop-os/cosmic-notifications/archive/epoch-%{version}-alpha.1/%{name}-epoch-%{version}-alpha.1.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  appstream-util
BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
Layer Shell notifications daemon which integrates with COSMIC.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.1 -a1 -p1
rm -rf .cargo
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml