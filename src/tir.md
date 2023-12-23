# TIR

This section describes the Hash Typed Intermediate Representation. This is
an intermediate language which is used to perform type checking.

The TIR has a formal description as a sub-structural type theory, which is
described in this section.

$$
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Set}{\mathbf{Set}}
\newcommand{\Prop}{\mathbf{Prop}}
\newcommand{\Fin}[1]{\mathbb{N}_{#1}}
\newcommand{\inf}[3][]{\frac{\displaystyle #2}{\displaystyle #3}\;\small{\text{#1}}}
\newcommand{\hMeta}[1]{\mathsf{#1}}
\newcommand{\hSpecial}[1]{\mathrm{#1}}
\newcommand{\hCtx}{\hMeta{Ctx}}
\newcommand{\hEmptyCtx}{\varnothing}
\newcommand{\hConsCtx}[2]{(#1; #2)}
\newcommand{\hEmptyCtx}{\varnothing}
\newcommand{\hTy}{\hMeta{Ty}}
\newcommand{\hTerm}{\hMeta{Term}}
\newcommand{\hVar}{\hMeta{Var}}
\newcommand{\hLookup}{\hMeta{lookup}}
\newcommand{\hType}{\hSpecial{Type}}
\newcommand{\hParams}{\hMeta{Params}}
\newcommand{\hParamMod}{\hMeta{ParamMod}}
\newcommand{\hSub}{\hMeta{sub}}
\newcommand{\hInfer}{\hMeta{infer}}
\newcommand{\hThis}{\hMeta{this}}
\newcommand{\hArgs}{\hMeta{Args}}
\newcommand{\hIdent}{\hMeta{Ident}}
\newcommand{\hEnter}{\hMeta{enter}}
\newcommand{\hEmptyParams}{(\,)}
\newcommand{\hConsParams}[4]{(#1; \; #2 \; #3 : #4)}
\newcommand{\hEmptyArgs}{(\,)}
\newcommand{\hConsArgs}[4]{(#1; \; #2 \; #3 = #4)}
\newcommand{\hFnTy}[2]{{#1}\to{#2}}
\newcommand{\hFn}[2]{{#1}\Rightarrow{#2}}
\newcommand{\hApp}[2]{{#1}\,{#2}}
\newcommand{\hMatchMeta}{\mathrm{match}}
\newcommand{\hMatch}[2]{\hMatchMeta{} \; #1 \; \{\; #2 \;\}}
\newcommand{\hCase}[2]{#1 \Rightarrow #2}
\newcommand{\hIsTy}{\;\hMeta{type}}
\newcommand{\hIsParams}{\;\hMeta{params}}
\newcommand{\hTermIsPat}{\hMeta{IsPat}}
\newcommand{\hIsPat}{\;\hMeta{pat}}
\newcommand{\hBinds}{\hMeta{binds}}
\newcommand{\hExtract}{\hMeta{extract}}
\newcommand{\hNames}{\hMeta{names}}
\newcommand{\hLength}{\hMeta{length}}
\newcommand{\and}{,\ }
$$

## Contexts

$$
\inf{}{\hCtx \in \Set}
$$

$$
\inf{}{\hEmptyCtx \in \hCtx}
$$

$$
\inf{\Gamma \in \hCtx \quad T \in \hTy(\Gamma)}{\hConsCtx{\Gamma}{T} \in \hCtx}
$$

$$
\inf{}{\cup \in \hCtx \times \hCtx \to \hCtx}
$$

## Variables

$$
\inf{}{\hVar \in \hCtx \to \Set}
$$

$$
\inf{}{0 \in \hVar(\hConsCtx{\Gamma}{T})}
$$

$$
\inf{n \in \hVar(\Gamma) \quad T \in \hTy(\Gamma)}{(n + 1) \in \hVar(\hConsCtx{\Gamma}{T})}
$$


$$
\inf{\Gamma \in \hCtx}{\hLookup_\Gamma \in \hVar(\Gamma) \to \hTy(\Gamma)}
$$

## Identifiers

$$
\inf{}{\hIdent \in \Set}
$$

$$
\inf{n \in \Nat}{n \in \hIdent}
$$

$$
\inf{s \in S}{s \in \hIdent}
$$

Here, $S$ is some suitable set of string identifiers.

## Parameters

$$
\inf{}{\hParamMod \in \Set}
$$

$$
\inf{}{\hInfer \in \hParamMod \quad \hThis \in \hParamMod}
$$

$$
\inf{}{\hParams \in \hCtx \to \Set}
$$

$$
\inf{\Gamma \in \hCtx}{\hEmptyParams \in \hParams(\Gamma)}
$$

$$
\inf{\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma) \quad x \in \hIdent \quad T \in \hTy(\hEnter_\Gamma (\Delta)) \quad M \subseteq \hParamMod}
{\hConsParams{\Delta}{M}{x}{T} \in \hParams(\Gamma)}
$$

$$
\inf{\Gamma \in \hCtx}{\hEnter_\Gamma \in \hParams(\Gamma) \to \hCtx}
$$

$$
\inf{\Gamma \in \hCtx}{\hEnter_\Gamma (\hEmptyParams) = \Gamma}
$$

$$
\inf{\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma) \quad x \in \hIdent \quad T \in \hTy(\hEnter_\Gamma (\Delta)) \quad M \subseteq \hParamMod}
{\hEnter_\Gamma (\hConsParams{\Delta}{M}{x}{T}) = \hConsCtx{\hEnter_\Gamma (\Delta)}{T}}
$$

$$
\inf{\Gamma \in \hCtx}{\hLength \in \hParams(\Gamma) \to \Nat}
$$

$$
\inf{\Gamma \in \hCtx}{\hNames \in \prod _{\Delta \in \hParams(\Gamma)} \hIdent^{\hLength(\Delta)}}
$$


## Arguments

$$
\inf{}{\hArgs \in \sum _{\Gamma \in \hCtx} \hParams(\Gamma) \to \Set}
$$

$$
\inf{\Gamma \in \hCtx}{\hEmptyArgs \in \hArgs(\Gamma, \hEmptyParams)}
$$

$$
\inf{\begin{gather*}
\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma) \quad \delta \in \hArgs(\Gamma, \Delta) \quad x \in \hIdent \\
T \in \hTy(\hEnter_\Gamma (\Delta)) \quad t \in \hTerm(\hEnter_\Gamma (\Delta), T) \quad M \subseteq \hParamMod
\end{gather*}}
{\hConsArgs{\delta}{M}{x}{t} \in \hArgs(\Gamma, \hConsParams{\Delta}{M}{x}{T})}
$$

$$
\inf{\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma)}{\hSub_\hTy \in \hTy(\hEnter_\Gamma(\Delta)) \times \hArgs(\Gamma, \Delta) \to \hTy(\Gamma)}
$$

$$
\inf{\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma) \quad T \in \hTy(\hEnter_\Gamma(\Delta))}
{\hSub_\hTerm \in \hTerm(\hEnter_\Gamma(\Delta), T) \to \prod _{\delta \in \hArgs(\Gamma, \Delta)} \hTerm(\Gamma, \hSub_\hTy(T, \delta))}
$$

## Terms

$$
\inf{}{\hTy \in \hCtx \to \Set}
$$

$$
\inf{}{\hTerm \in \sum _{\Gamma \in \hCtx} \hTy(\Gamma) \to \Set}
$$

$$
\inf{\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma)}{\hTermIsPat_{\Gamma, \Delta} \in \sum _{T \in \hTy(\Gamma)} \hTerm(\Gamma + \Delta, T) \to \Prop}
$$

$$
\inf{\Gamma \in \hCtx \quad \Delta \in \hParams(\Gamma)}{
\begin{gather*}
  \hExtract _{\Gamma, \Delta} \in \sum _{T \in \hTy(\Gamma)} \sum _{t \in \hTerm(\Gamma, T)} \sum _{p \in \hTerm(\Gamma + \Delta, T)} \hTermIsPat_{\Gamma, \Delta}(T, p) \to \hArgs(\Gamma, \Delta) \\
\end{gather*}
}
$$

We write $\Gamma \vdash t : T$ as sugar for $t \in \hTerm(\Gamma, T)$, and
$\Gamma \vdash T\hIsTy$ as sugar for $T \in \hTy(\Gamma)$ (though this is equivalent to $\Gamma \vdash T : \hType$).

Similarly, we write $\Gamma \vdash \delta :: \Delta$ as sugar for $\delta \in \hArgs(\Gamma, \Delta)$ and
$\Gamma \vdash \Delta\hIsParams$ as sugar for $\Delta \in \hParams(\Gamma)$.

We write $\Gamma + B \vdash p\hIsPat$ as sugar for $\hTermIsPat_{\Gamma, B}(P, p)$ where $P$ is inferred from $p$.

We implicitly quantify $\Gamma \in \hCtx$.
We write $(n : T) \in \Gamma$ for $n \in \hVar(\Gamma)$ and $\hLookup(n) = T$.

We write $T[\delta]$ for $\hSub_\hTy(T, \delta)$.
and similarly $t[\delta]$ for $\hSub_\hTerm(t, \delta)$.

We write $\Gamma + \Delta$ for $\hEnter_\Gamma(\Delta)$

Below we inductively define $\hTerm$ and $\hTermIsPat$ using this sugar:

## Types

$$
\inf{\Gamma \vdash T : \hType}{\Gamma \vdash T\hIsTy}
$$

## Type of types

$$
\inf[$\hType$-form]{}{\Gamma \vdash \hType : \hType}
$$

## Variables

$$
\inf[$n$-intro]{(n : T) \in \Gamma}{\Gamma \vdash n : T}
$$

## Functions

$$
\inf[$\to$-form]{\Gamma \vdash \Delta\hIsParams \quad \Gamma + \Delta \vdash R : \hType}{\Gamma \vdash \hFnTy{\Delta}{R} : \hType }
$$

$$
\inf[$\to$-intro]{\Gamma \vdash \Delta\hIsParams \quad
\Gamma + \Delta \vdash R : \hType \quad \Gamma + \Delta \vdash r : R}{\Gamma \vdash \hFn{\Delta}{r} : \hFnTy{\Delta}{R} }
$$

$$
\inf[$\to$-elim]{\Gamma \vdash \Delta\hIsParams
\quad \Gamma + \Delta \vdash R : \hType \quad \Gamma \vdash f : \hFnTy{\Delta}{R}
\quad \Gamma \vdash \delta :: \Delta}
{\Gamma \vdash \hApp{f}{\delta} : R[\delta]}
$$

## Tuples

$$
\inf[$\hEmptyArgs$-form]{
  \Gamma \vdash \Delta\hIsParams \quad \hLength(\Delta) \neq 1
}{\Gamma \vdash (\Delta) : \hType }
$$


$$
\inf[$\hEmptyArgs$-intro]{
  \Gamma \vdash \Delta\hIsParams \quad \Gamma \vdash (\Delta): \hType \quad \Gamma \vdash \delta :: \Delta
}{\Gamma \vdash (\delta) : (\Delta) }
$$


$$
\inf[$\hEmptyArgs$-elim]{
\begin{gather*}
  \Gamma \vdash \Delta\hIsParams \and B\hIsParams \and (\Delta): \hType \and \delta :: \Delta \\
  \Gamma + B \vdash \epsilon :: \Delta \and (\epsilon) \hIsPat \and Q : \hType \and q : Q
\end{gather*}
}{
  \Gamma \vdash \hMatch{(\delta)}{\hCase{(\epsilon)}{q}} : Q[\hExtract_{\Gamma, B}((\Delta), (\delta), (\epsilon))]
}
$$
