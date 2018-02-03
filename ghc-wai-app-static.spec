# generated by cabal-rpm-0.12.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name wai-app-static
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        3.1.6.1
Release:        5%{?dist}
Summary:        WAI application for static serving

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  chrpath
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-date-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mime-types-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-zlib-devel
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mockery-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-temporary-devel
%endif
# End cabal-rpm deps

%description
WAI application for static serving. Also provides some helper functions and
datatypes for use outside of WAI.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install
%ghc_fix_rpath %{pkgver}


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md
%{_bindir}/warp


%changelog
* Thu Feb  1 2018 Jens Petersen <petersen@redhat.com> - 3.1.6.1-5
- rebuild

* Fri Oct 20 2017 Jens Petersen <petersen@fedoraproject.org> - 3.1.6.1-3
- rebuild

* Wed Sep 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.1.6.1-2
- Update to latest spec template.
- Fix description.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.1.6.1-1
- Update to latest release.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.1.5-5
- Bump for Fedora 26.

* Fri Dec 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.5-4
- Update release to be newer than previous builds

* Fri Dec 16 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 3.1.5-1
- spec file generated by cabal-rpm-0.10.0
