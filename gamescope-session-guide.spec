# Create an option to build locally without fetchting own repo
# for sourcing and patching
%bcond local 0

# Source repo
%global author shahnawazshahin
%global source steam-using-gamescope-guide
%global sourcerepo https://github.com/shahnawazshahin/steam-using-gamescope-guide
%global commit e6b2c408480dbf4af9c4d947ff399abd07b66341
%global versioncommit %(echo -n %{commit} | head -c 8)

# Own copr repo
%global coprrepo https://github.com/PVermeer/copr_gamescope-session-guide
%global coprsource copr_gamescope-session-guide

Name: gamescope-session-guide
Version: 0.0.4
Release: 3.%{versioncommit}%{?dist}
License: MIT
Summary: RPM package to add a gamescope-session to login session options.
Url: %{coprrepo}

BuildRequires: git

Requires: gamescope
Requires: mangohud
Requires: steam

%define workdir %{_builddir}/%{name}
%define coprdir %{workdir}/%{coprsource}
%define sourcedir %{workdir}/%{source}

%description
RPM package to install a gamescope-session on Fedora (bazzite).

This packages requires steam to be preinstalled. If steam is not installed it will fail to install.

The configuration is provided by %{source}.

%prep
# To apply working changes handle sources / patches locally
# COPR should clone the commited changes
%if %{with local}
  # Get sources / patches - local build
  mkdir -p %{coprdir}
  cp -r %{_topdir}/SOURCES/* %{coprdir}
%else
  # Get sources / patches - COPR build
  git clone %{coprrepo} %{coprdir}
  cd %{coprdir}
  rm -rf .git
  cd %{workdir}
%endif

# Get source repo
git clone %{sourcerepo} %{sourcedir}
cd %{sourcedir}
git reset --hard %{commit}

# Apply patches
git apply %{coprdir}/patches/add-enviroment-variable-for-prefer-output.patch

rm -rf .git
cd %{workdir}

%build

%install
mkdir -p %{buildroot}/usr
cp -r %{sourcedir}/usr/* %{buildroot}/usr/

%check

%post

%files
%{_bindir}/*
%{_datadir}/*
