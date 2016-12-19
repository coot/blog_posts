# Algebraic Data Types and Universal Algebra

[https://en.wikipedia.org/wiki/Universal_algebra](Universal algebra) is a field
of mathematics which deals with general algebraic structures.  Much of
classical algebra is about groups (like integers with addition, or rotations of
a plane), rings (like the ring of integers with addition and multiplication),
fields (like real numbers, or complex numbers, where one can find inverses of
non 0 elements).  Universal algebra deals with more general structures like
that.  Every algebra has the underlying universum - a set of `numbers` and
a set of operations.  The operations can have different arity, i.e. number of
arguments.  Examples include constants - operations of arity 0, or or
multiplication, addition of integers - artity 2, or inverse - artiy 1.

Let's take as an example the algebra of natural numbers using [Peano
axioms](https://en.wikipedia.org/wiki/Peano_axioms). It has one constant
- let's call it `0` and one operation of arity 1 - the successor function `s`.
In Universal Algebra one can consider all of the algebras which has this set
of operations and satisfies the Peano axioms, but let us skip two of them:

* the injectivity axiom of `s`:
  ```
    s(m) = s(n) ⇒ m = n
  ```
* the axiom that 0 is not a successor of any element:
  ```
    for every n: s(n) = 0 is false
  ```

Otherwise there would be only one algebra to consider.

Let us call algebras which satisfy these axiom **Peano algebras**.  One examle
is the set of *natural numbers* ℕ, where the successor `s(n)` is `n+1`.  This
is a *free algebra* with one generator, what it really means that all elements
can be generated from `0` and the operation `s`, and that there is no
relation/equations between elements.  A non free example would be the set of
ℕ/2ℕ ≅ {0,1}, where `s(0) = 1` and `s(1) = 0` (this breaks the two Peano axiom
that that we excluded - just to have more non trivial examples).

Let's take haskells `Maybe a` [type](https://wiki.haskell.org/Maybe).  It has
two constructors `Nothing` and `Just`.  And it actually forms a [Peano
Algebra](https://en.wikipedia.org/wiki/Peano_axioms), for any type `a`. It's
elements are:
```
  Nothing, Just a, Just (Just a), ...
```

This algebra is free, there are no relations (or equalities of types) among all
algebras of this type.  But relations are very useful, and it turns out that
Haskell provides them using monads. For example for the `Maybe` type we have
```
  Just (Just x) >>= id == Just x
```
for every `x :: a`.

This way when you use `Maybe` in a monadic context you use it as ℕ/2ℕ rather
than the free algebra ℕ.  Knowing these relations is the essence of knowing how
a given monad works.

There are other examples of a Peano algebra in Haskell.  The `Either a`
[monad](https://hackage.haskell.org/package/base-4.9.0.0/docs/Data-Either.html)
provides an example with two generators - or two data constructors `Left a` and
`Right a`.  As a Peano algebra it represented as a binary tree where the
successor of `Right a` is `Right (Right a)` and the successor of `Left a` is
`Left (Left a)` (for some type `a`).  Then the `Either` monad provides only one
relation:
```
  Right (Right x) >>= id === Right x
```
and there is no relation for the `Left` constructor:
```
  Left (x :: Either a) >>= id == Left x
```
for any `x :: a`.
