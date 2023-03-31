Name:		texlive-bredzenie
Version:	44371
Release:	2
Summary:	A Polish version of "lorem ipsum..." in the form of a LaTeX package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bredzenie
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bredzenie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bredzenie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a polish version of the classic pseudo-Latin "lorem
ipsum dolor sit amet...". It provides access to several
paragraphs of pseudo-Polish generated with Hidden Markov Models
and Recurrent Neural Networks trained on a corpus of Polish.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bredzenie
%doc %{_texmfdistdir}/doc/latex/bredzenie

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
