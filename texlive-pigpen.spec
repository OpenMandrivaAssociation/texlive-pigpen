%global tl_name pigpen
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	A font for the pigpen (or masonic) cipher
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/pigpen
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pigpen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pigpen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Pigpen cipher package provides the font and the necessary wrappers
(style file, etc.) in order to write Pigpen ciphers, a simple
substitution cipher. The package provides a font (available both as
Metafont source, and as an Adobe Type 1 file), and macros for its use.

