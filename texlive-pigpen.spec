Name:		texlive-pigpen
Version:	15878
Release:	2
Summary:	A font for the pigpen (or masonic) cipher
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/pigpen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pigpen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pigpen.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Pigpen cipher package provides the font and the necessary
wrappers (style file, etc.) in order to write Pigpen ciphers, a
simple substitution cipher. The package provides a font
(available both as MetaFont source, and as an Adobe Type 1
file), and macros for its use.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/pigpen/pigpen.map
%{_texmfdistdir}/fonts/source/public/pigpen/pigpen.mf
%{_texmfdistdir}/fonts/tfm/public/pigpen/pigpen.tfm
%{_texmfdistdir}/fonts/type1/public/pigpen/pigpen.pfa
%{_texmfdistdir}/tex/latex/pigpen/pigpen.sty
%{_texmfdistdir}/tex/latex/pigpen/pigpen.tex
%doc %{_texmfdistdir}/doc/latex/pigpen/README
%doc %{_texmfdistdir}/doc/latex/pigpen/pigpendoc.pdf
%doc %{_texmfdistdir}/doc/latex/pigpen/pigpendoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
