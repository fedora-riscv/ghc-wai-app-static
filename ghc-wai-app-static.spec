# generated by cabal-rpm-0.10.0
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name wai-app-static

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        3.1.6.1
Release:        1.git.0.b4bf0cd%{?dist}
Summary:        WAI application for static serving

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

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
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-temporary-devel
%endif
# End cabal-rpm deps

%description
API docs and the README are available at
<http://www.stackage.org/package/wai-app-static>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install

%ghc_fix_dynamic_rpath warp


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
* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.1.6.1-1
- Update to latest release.

* Fri Jul 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.1.5-5
- Bump for Fedora 26.

* Fri Dec 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.5-4
- Update release to be newer than previous builds

* Fri Dec 16 2016 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 3.1.5-1
- spec file generated by cabal-rpm-0.10.0
