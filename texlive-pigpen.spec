Name:		texlive-pigpen
Version:	0.2
Release:	1
Summary:	A font for the pigpen (or masonic) cipher
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/pigpen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pigpen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pigpen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The Pigpen cipher package provides the font and the necessary
wrappers (style file, etc.) in order to write Pigpen ciphers, a
simple substitution cipher. The package provides a font
(available both as MetaFont source, and as an Adobe Type 1
file), and macros for its use.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
