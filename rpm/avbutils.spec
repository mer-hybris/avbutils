# SPDX-FileCopyrightText: 2026 Jolla Mobile Ltd
#
# SPDX-License-Identifier: BSD-3-Clause

Name: avbutils
Version: 0.1.0
Release: 0
Summary: Android Verified Boot build utilities

License: BSD-3-Clause
URL: https://github.com/mer-hybris/avbutils
Source0: %{name}-%{version}.tar.bz2

Requires: android-tools
# android-tools should probably require openssl as it is used by avbtool
Requires: openssl
Requires: python3-base

BuildArch: noarch

%undefine _enable_debug_packages
%define disable_docs_package 1

%description
%{summary}.

%prep
%autosetup

%build

%install
install -D -m 755 genvbmeta -t %{buildroot}/%{_bindir}
install -D -m 755 avbpubkey2c -t %{buildroot}/%{_bindir}

%files
%doc README.md
%doc images_example.toml
%license LICENSES/BSD-3-Clause.txt
%{_bindir}/genvbmeta
%{_bindir}/avbpubkey2c
