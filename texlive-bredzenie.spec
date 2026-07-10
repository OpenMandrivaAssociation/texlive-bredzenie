%global tl_name bredzenie
%global tl_revision 44371

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A Polish version of lorem ipsum... in the form of a LaTeX package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bredzenie
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bredzenie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bredzenie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a polish version of the classic pseudo-Latin "lorem ipsum dolor
sit amet...". It provides access to several paragraphs of pseudo-Polish
generated with Hidden Markov Models and Recurrent Neural Networks
trained on a corpus of Polish.

