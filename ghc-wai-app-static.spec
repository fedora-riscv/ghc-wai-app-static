# generated by cabal-rpm-2.1.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name wai-app-static
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        3.1.7.4
Release:        1%{?dist}
Summary:        WAI application for static serving

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
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
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-http-date-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-mime-types-prof
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-zlib-prof
%endif
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
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files
%{_bindir}/warp


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sun Jan 22 2023 Jens Petersen <petersen@redhat.com> - 3.1.7.4-1
- https://hackage.haskell.org/package/wai-app-static-3.1.7.4/changelog
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Jens Petersen <petersen@redhat.com> - 3.1.7.3-1
- https://hackage.haskell.org/package/wai-app-static-3.1.7.3/changelog

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 3.1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 3.1.7.2-1
- update to 3.1.7.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 3.1.7.1-2
- refresh to cabal-rpm-2.0.6

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 3.1.7.1-1
- update to 3.1.7.1
- move warp tool to the base package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 3.1.6.3-1
- update to 3.1.6.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 3.1.6.2-5
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 3.1.6.2-3
- rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.6.2-1
- update to 3.1.6.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

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
