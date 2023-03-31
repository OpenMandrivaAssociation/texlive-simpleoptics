Name:		texlive-simpleoptics
Version:	62977
Release:	2
Summary:	Drawing lenses and mirrors for optical diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simpleoptics
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleoptics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleoptics.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some of macros for drawing simple lenses
and mirrors for use in optical diagrams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simpleoptics
%doc %{_texmfdistdir}/doc/latex/simpleoptics

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
