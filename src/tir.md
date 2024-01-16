# TIR

This section describes the Hash Typed Intermediate Representation. This is
an intermediate language which is used to perform type checking.

The TIR has a formal description as a sub-structural type theory, which is
described in this section.

Specifically, TIR is described by a variant of two-level dependent Hoare type theory
with inductive constructions and pattern matching.

$$
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Set}{\mathbf{Set}}
\newcommand{\P}{\mathcal{P}}
\newcommand{\Prop}{\mathbf{Prop}}
\newcommand{\Fin}[1]{\mathbb{N}_{#1}}
\newcommand{\inf}[3][]{\frac{\displaystyle #2}{\displaystyle #3}\;\small{\text{#1}}}
\newcommand{\hMeta}[1]{\mathsf{#1}}
\newcommand{\hSpecial}[1]{\mathrm{#1}}
\newcommand{\hCtx}{\hMeta{Ctx}}
\newcommand{\hEffect}{\hMeta{Effect}}
\newcommand{\hLt}{\hMeta{Lt}}
\newcommand{\hRef}[2]{\hMeta{\&}{#1}\,{#2}}
\newcommand{\hDeref}[1]{\hMeta{*}{#1}}
\newcommand{\hAddr}[1]{\hMeta{\&}{#1}}
\newcommand{\hlt}{\hMeta{'}}
\newcommand{\hStage}{\hMeta{Stage}}
\newcommand{\hPure}{\hMeta{pure}}
\newcommand{\hRead}{\hMeta{read}}
\newcommand{\hWrite}{\hMeta{write}}
\newcommand{\hImpure}{\hMeta{impure}}
\newcommand{\hCt}{\hMeta{ct}}
\newcommand{\hRt}{\hMeta{rt}}
\newcommand{\hEmptyCtx}{\varnothing}
\newcommand{\hConsCtx}[2]{(#1; #2)}
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
\newcommand{\hBlock}[3]{\{\; #1 := #2\,;\; #3 \;\}}
\newcommand{\hConsArgs}[4]{(#1; \; #2 \; #3 = #4)}
\newcommand{\hFnTy}[3]{{#1}\to_{#2}{#3}}
\newcommand{\hFn}[2]{{#1}\Rightarrow{#2}}
\newcommand{\hApp}[2]{{#1}\,{#2}}
\newcommand{\hMatchMeta}{\mathrm{match}}
\newcommand{\hMatch}[2]{\hMatchMeta{} \; #1 \; \{\; #2 \;\}}
\newcommand{\hCase}[2]{#1 \Rightarrow #2}
\newcommand{\hIsTy}{\;\hMeta{type}}
\newcommand{\hIsLt}{\;\hMeta{lt}}
\newcommand{\hIsCond}{\;\hMeta{cond}}
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
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad T \in \hTy(\Gamma, s)}{\hConsCtx{\Gamma}{T} \in \hCtx}
$$

$$
\inf{}{\cup \in \hCtx \times \hCtx \to \hCtx}
$$

## Variables

$$
\inf{}{\hVar \in \hCtx \times \hStage \to \Set}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage}{0 \in \hVar(\hConsCtx{\Gamma}{T}, s)}
$$

$$
\inf{\Gamma \in \hCtx \quad s_1, s_2 \in \hStage \quad n \in \hVar(\Gamma, s_1) \quad T \in \hTy(\Gamma, s_2)}{(n + 1) \in \hVar(\hConsCtx{\Gamma}{T}, s_1)}
$$


$$
\inf{\Gamma \in \hCtx \quad s \in \hStage}{\hLookup_\Gamma \in \hVar(\Gamma, s) \to \hTy(\Gamma, s)}
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
\inf{}{\hParams \in \hCtx \times \hStage \to \Set}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage}{\hEmptyParams \in \hParams(\Gamma, s)}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad \Delta \in \hParams(\Gamma, s) \quad x \in \hIdent \quad T \in \hTy(\hEnter_\Gamma (\Delta), s) \quad M \subseteq \hParamMod}
{\hConsParams{\Delta}{M}{x}{T} \in \hParams(\Gamma, s)}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage}{\hEnter_\Gamma \in \hParams(\Gamma, s) \to \hCtx}
$$

$$
\inf{\Gamma \in \hCtx}{\hEnter_\Gamma (\hEmptyParams) = \Gamma}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad \Delta \in \hParams(\Gamma, s) \quad x \in \hIdent \quad T \in \hTy(\hEnter_\Gamma (\Delta), s) \quad M \subseteq \hParamMod}
{\hEnter_\Gamma (\hConsParams{\Delta}{M}{x}{T}) = \hConsCtx{\hEnter_\Gamma (\Delta)}{T}}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage}{\hLength \in \hParams(\Gamma, s) \to \Nat}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage}{\hNames \in \prod _{\Delta \in \hParams(\Gamma, s)} \hIdent^{\hLength(\Delta)}}
$$


## Arguments

$$
\inf{}{\hArgs \in \sum _{(\Gamma, s) \in \hCtx \times \hStage} \hParams(\Gamma, s) \times \P(\hEffect(\Gamma, s)) \to \Set}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad e \subseteq \hEffect(\Gamma, s)}{\hEmptyArgs \in \hArgs(\Gamma, s, \hEmptyParams, e)}
$$

Notice effects are not dependent in arguments!

$$
\inf{\begin{gather*}
\Gamma \in \hCtx \quad s \in \hStage \quad e_1, e_2 \subseteq \hEffect(\Gamma, s) \quad \Delta \in \hParams(\Gamma, s) \quad \delta \in \hArgs(\Gamma, s, \Delta, e_1) \quad x \in \hIdent \\
T \in \hTy(\hEnter_\Gamma (\Delta), s) \quad t \in \hTerm(\hEnter_\Gamma (\Delta), s, T, e_2) \quad M \subseteq \hParamMod
\end{gather*}}
{\hConsArgs{\delta}{M}{x}{t} \in \hArgs(\Gamma, s, \hConsParams{\Delta}{M}{x}{T}, e_1 + e_2)}
$$

Substitution is only for pure terms!
We need *execution* for impure terms, and the type cannot be dependent in that case.

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad \Delta \in \hParams(\Gamma, s)}{\hSub_\hTy \in \hTy(\hEnter_\Gamma(\Delta), s) \times \hArgs(\Gamma, s, \Delta, \hPure) \to \hTy(\Gamma, s)}
$$

Effects cannot be on the extended context!
Also $p$ needs to be weakened here.

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage  \quad \Delta \in \hParams(\Gamma, s) \quad T \in \hTy(\hEnter_\Gamma(\Delta), s) \quad e \subseteq \hEffect(\Gamma, s)}
{\hSub_\hTerm \in \hTerm(\hEnter_\Gamma(\Delta), s, T, e) \to \prod _{\delta \in \hArgs(\Gamma, s, \Delta, \hPure)} \hTerm(\Gamma, s, \hSub_\hTy(T, \delta), e)}
$$

## Terms

For $A : T \to \Set$, we write $\Sigma A$ to mean $\sum _{t \in T} A(t)$ and $\Pi A$ to mean $\prod _{t \in T} A(t)$.

$$
\inf{}{\hTy \in \hCtx \times \hStage \to \Set}
$$

$$
\inf{}{\hTerm \in \sum _{(\Gamma, s) \in \hCtx \times \hStage} \hTy(\Gamma, s) \times \P(\hEffect(\Gamma, s)) \to \Set}
$$

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad \Delta \in \hParams(\Gamma, s)}{\hTermIsPat_{\Gamma, \Delta} \in \sum _{T \in \hTy(\Gamma, s)} \hTerm(\Gamma + \Delta, s, T, \hPure) \to \Prop}
$$

Not sure about some of the purity indices here:

$$
\inf{\Gamma \in \hCtx \quad s \in \hStage \quad \Delta \in \hParams(\Gamma, s) \quad e \subseteq \hEffect(\Gamma, s)}{
\begin{gather*}
  \hExtract _{\Gamma, \Delta} \in \sum _{T \in \hTy(\Gamma, s)} \sum _{t \in \hTerm(\Gamma, s, T, e)} \sum _{p \in \hTerm(\Gamma + \Delta, s, T, \hPure)} \hTermIsPat_{\Gamma, \Delta}(T, p) \to \hArgs(\Gamma, s, \Delta, e) \\
\end{gather*}
}
$$

We write $\Gamma \vdash t :_e T$ as sugar for $t \in \hTerm(\Gamma, s, T, e)$ where $s$ is inferred from $T$, and
$\Gamma \vdash T\hIsTy _s$ as sugar for $T \in \hTy(\Gamma, s)$ (though this is equivalent to $\Gamma \vdash T :_\hPure \hType_s$).

Similarly, we write $\Gamma \vdash \delta ::_e \Delta$ as sugar for $\delta \in \hArgs(\Gamma, s, \Delta, p)$ and
$\Gamma \vdash \Delta\hIsParams_s$ as sugar for $\Delta \in \hParams(\Gamma, s)$.

We write $\Gamma + B \vdash p\hIsPat$ as sugar for $\hTermIsPat_{\Gamma, B}(P, p)$ where $P$ is inferred from $p$.

We implicitly quantify $\Gamma \in \hCtx$, $s \in \hStage$ and $p \subseteq \hEffect$.
We write $(n : T)_s \in \Gamma$ for $n \in \hVar(\Gamma, s)$ and $\hLookup(n) = T$.

We write $T[\delta]$ for $\hSub_\hTy(T, \delta)$.
and similarly $t[\delta]$ for $\hSub_\hTerm(t, \delta)$.

We write $\Gamma + \Delta$ for $\hEnter_\Gamma(\Delta)$

Below we inductively define $\hTerm$ and $\hTermIsPat$ using this sugar:

## Effects

$$
\inf{}{\hEffect \in \hCtx \times \hStage \to \Set}
$$

$$
\inf{}{\hImpure \in \hEffect(\Gamma, s)}
$$

$$
\inf{(n : T)_s \in \Gamma}{\hRead(n) \in \hEffect(\Gamma, s) \quad \hWrite(n) \in \hEffect(\Gamma, s)}
$$

We usually write $e$ to mean the subset of $\hEffect(\Gamma, s)$ containing $e$.
We write $e_1 + e_2$ to mean $\{ e_1, e_2 \}$ and $e_1 - e_2$ to mean $e_1 \setminus e_2$.
We write $\hPure$ to mean $\varnothing$.

For $N \subseteq \hVar(\Gamma, s)$, we write e.g. $\hRead(N)$ to mean $\{\hRead(n) \mid n \in N\}$.

## Stage

$$
\inf{}{\hStage := \{\;\hCt > \hRt\;\}}
$$

## Lifetime

$$
\inf{}{\hLt \in \hCtx \times \hStage \to \Set}
$$

$$
\inf{(n : T)_s \in \Gamma}{\hlt{n} \in \hLt (\Gamma, s)}
$$

## Types

$$
\inf{\Gamma \vdash T :_\hPure \hType_s}{\Gamma \vdash T\hIsTy_s}
$$

## Type of types

$$
\inf[$\hType$-form]{}{\Gamma \vdash \hType_s :_\hPure \hType_s}
$$


## Variables

$$
\inf[$n$-intro]{(n : T)_s \in \Gamma}{\Gamma \vdash n :_\hPure T}
$$

## Functions

$$
\inf[$\to$-form]{\Gamma \vdash \Delta\hIsParams_s \quad \Gamma + \Delta \vdash R \hIsTy_s}{\Gamma \vdash \hFnTy{\Delta}{p}{R} \hIsTy_s }
$$

$$
\inf[$\to$-intro]{\Gamma \vdash \Delta\hIsParams_s \quad
\Gamma + \Delta \vdash R \hIsTy_s \quad \Gamma + \Delta \vdash r :_e R}{\Gamma \vdash \hFn{\Delta}{r} :_\hPure \hFnTy{\Delta}{p}{R} }
$$

$$
\inf[$\to$-elim]{\Gamma \vdash \Delta\hIsParams_s
\quad \Gamma + \Delta \vdash R \hIsTy_s \quad \Gamma \vdash f :_{p_1} \hFnTy{\Delta}{p_2}{R}
\quad \Gamma \vdash \delta ::_{p_3} \Delta}
{\Gamma \vdash \hApp{f}{\delta} :_{p_1 + p_2 + p_3} R[\delta]}
$$

## Tuples

$$
\inf[$\hEmptyArgs$-form]{
  \Gamma \vdash \Delta\hIsParams_s \quad \hLength(\Delta) \neq 1
}{\Gamma \vdash (\Delta) \hIsTy_s }
$$


$$
\inf[$\hEmptyArgs$-intro]{
  \Gamma \vdash \Delta\hIsParams_s \quad \Gamma \vdash (\Delta) \hIsTy_s \quad \Gamma \vdash \delta ::_e \Delta
}{\Gamma \vdash (\delta) :_e (\Delta) }
$$


$$
\inf[$\hEmptyArgs$-elim]{
\begin{gather*}
  \Gamma \vdash \Delta\hIsParams_{s} \and B\hIsParams_{s} \and (\Delta) \hIsTy_{s} \and \delta ::_{p_1} \Delta \\
  \Gamma + B \vdash \epsilon ::_{\hPure} \Delta \and (\epsilon) \hIsPat \and Q \hIsTy_{s} \and q :_{p_2} Q
\end{gather*}
}{
  \Gamma \vdash \hMatch{(\delta)}{\hCase{(\epsilon)}{q}} :_{p_1 + p_2 - \hRead(\hBinds((\epsilon))) - \hWrite(\hBinds((\epsilon)))} Q[\hExtract_{\Gamma, B}((\Delta), (\delta), (\epsilon))]
}
$$

What happens if $\hExtract{}$ fails?

Generalise to all patterns and with exhaustiveness check.

## Blocks

$$
\inf[$\{\,\}$-intro]{
\begin{gather*}
  \Gamma \vdash T \hIsTy_s \and B \hIsParams_s \and t :_{p_1} T \\
  \Gamma + B \vdash p :_\hPure T \and p \hIsPat \and Q \hIsTy_s \and q _{p_2}: Q
\end{gather*}
}{\Gamma \vdash \hBlock{p}{t}{q} :_{p_1 + p_2 - \hRead(\hBinds(p)) - \hWrite(\hBinds(p))} Q[\hExtract_{\Gamma, B}(T, t, p)] }
$$

## References

$$
\inf{
\begin{gather*}
  \Gamma \vdash a\hIsLt_s \and T\hIsTy_s \\
\end{gather*}
}{\Gamma \vdash \hRef{a}{T} \hIsTy_s }
$$

$$
\inf{
\begin{gather*}
  (n : T)_s \in \Gamma \\
  \Gamma \vdash T\hIsTy_s \\
\end{gather*}
}{\Gamma \vdash \hAddr{n} :_\hPure \hRef{\hlt{n}}{T}}
$$

$$
\inf{
\begin{gather*}
  (n : T)_s \in \Gamma \\
  \Gamma \vdash T\hIsTy_s \and t :_e \hRef{\hlt{n}}{T}
\end{gather*}
}{\Gamma \vdash \hDeref{t} :_{e + \hRead(n)} \hRef{\hlt{n}}{T}}
$$

$$
\inf{
\begin{gather*}
  \Gamma \vdash a\hIsLt_s \and T\hIsTy_s \and t :_e \hRef{a}{T} \\
\end{gather*}
}{\Gamma \vdash \hDeref{t} :_\hImpure T}
$$

## Commands






