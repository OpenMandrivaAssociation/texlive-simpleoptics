%global tl_name simpleoptics
%global tl_revision 62977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Drawing lenses and mirrors for optical diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/simpleoptics
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleoptics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleoptics.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some of macros for drawing simple lenses and
mirrors for use in optical diagrams.

