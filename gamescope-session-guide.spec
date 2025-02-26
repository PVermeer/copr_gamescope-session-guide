%global author shahnawazshahin
%global repository steam-using-gamescope-guide
%global maincommit 41095240664afd9672b9861cd6892ae7133dbba6
%global mainversioncommit %(echo -n %{maincommit} | head -c 8)

Name: gamescope-session-guide
Version: 0.0.2
Release: %{mainversioncommit}%{?dist}
License: MIT
Summary: RPM package to add a gamescope-session to login session options.
Url: https://github.com/%{author}/%{repository}

BuildRequires: git

Requires: gamescope
Requires: mangohud
Requires: steam

# Autopatch does not work because reasons....
Source1: add-enviroment-variable-for-prefer-output.patch

%define workdir %{_builddir}/%{repository}

%description
Personal RPM package to install a gamescope-session on Fedora (bazzite).

This packages requires steam to be preinstalled. If steam is not installed it will fail to install.

The configuration is provided by https://github.com/%{author}/%{repository}.

%prep
# Get the repo
git clone https://github.com/%{author}/%{repository} %{workdir}
cd %{workdir}
git reset --hard %{maincommit}

# Autopatch does not work because reasons....
git apply %{SOURCE1}

rm -rf .git

%build

%install
mkdir -p %{buildroot}/usr
cp -r %{workdir}/usr/* %{buildroot}/usr/

%check

%files
%{_bindir}/*
%{_datadir}/*

%post
