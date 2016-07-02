%define debug_package %{nil}
%global release_name Ulyaoth
%global dist_version 20160702

Summary: Ulyaoth release files
Name: ulyaoth-release
Version: 20160702
Release: 1%{?dist}
License: GPLv3
Group: System Environment/Base
URL: https://www.ulyaoth.net
Source0: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/LICENSE
Source1: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/README.developers
Source2: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/README.Ulyaoth-Release-Notes
Source3: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/README.license
Source4: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/85-display-manager.preset
Source5: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/90-default.preset
Source6: https://raw.githubusercontent.com/ulyaoth/ulyaothos/master/Packages/u/ulyaoth-release/SOURCE/99-default-disable.preset
Provides: ulyaoth-release
Provides: redhat-release
Provides: fedora-release
Provides: system-release
Requires: ulyaoth-repos
BuildArch: x86_64

%description
Ulyaoth release files such as yum configs and various /etc/ files that define the release.

%package notes
Summary:	Release Notes
License:	Open Publication
Group:		System Environment/Base
Provides:	system-release-notes
Provides:	ulyaoth-release-notes

%description notes
Ulyaoth release notes package.

%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .

%build

%install
install -d %{buildroot}/etc
echo "Ulyaoth" > %{buildroot}/etc/ulyaoth-release
echo "cpe:/o:ulyaoth:ulyaoth:%{version}" > %{buildroot}/etc/system-release-cpe
cp -p %{buildroot}/etc/ulyaoth-release %{buildroot}/etc/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}/etc/issue
cp -p %{buildroot}/etc/issue %{buildroot}/etc/issue.net
echo >> %{buildroot}/etc/issue
ln -s ulyaoth-release %{buildroot}/etc/redhat-release
ln -s ulyaoth-release %{buildroot}/etc/system-release
ln -s ulyaoth-release %{buildroot}/etc/fedora-release

mkdir -p %{buildroot}/usr/lib/systemd/system-preset/

cat << EOF >>%{buildroot}/usr/lib/os-release
NAME=Ulyaoth
VERSION="%{version} (%{release_name})"
ID=generic
VERSION_ID=%{version}
PRETTY_NAME="Ulyaoth %{version} (%{release_name})"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:ulyaoth:ulyaoth:%{version}"
EOF
# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}/etc/os-release

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%ulyaoth		%{dist_version}
%%dist		.uly%{dist_version}
%%uly%{dist_version}		1
EOF

# Add presets
# Default system wide
install -m 0644 85-display-manager.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 90-default.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 99-default-disable.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE README.license
%config %attr(0644,root,root) /usr/lib/os-release
/etc/os-release
%config %attr(0644,root,root) /etc/ulyaoth-release
/etc/fedora-release
/etc/redhat-release
/etc/system-release
%config %attr(0644,root,root) /etc/system-release-cpe
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset

%files notes
%defattr(-,root,root,-)
%doc README.Ulyaoth-Release-Notes

%changelog
* Sat Jul 2 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> - 20160702-1
- Initial Release based on Fedora 24 spec file.