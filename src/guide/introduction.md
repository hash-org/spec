# Introduction

**Hash** is a general-purpose programming language suitable for writing high-level
as well as low-level code.

It supports functional and imperative programming paradigms, and can either be compiled or
interpreted.

Hash features a powerful static type system with inference, first-class memory management with effects,
dependent types with automatic constraint solving, and a context system.

Below is a taste of what it is like to write programs in Hash:

```rust
{ Map } := import("@std/map.hash")

Name := struct(name: &own str)

Num := struct(value: i32)

Expr := enum(
  Var(Name),
  Add(&own Expr, &own Expr),
  Lit(Num),
)

Context := struct(map: Map<Name, Num>)

Expr += mod {
  eval := #rt <context: Context> => (expr: Self) -> Option<Num> => {
    match expr {
      Var(name) => context.get(name),
      Add(left, right) => {
        Num(left) := eval(*left)
        Num(right) := eval(*right)
        Num(left + right)
      },
      Lit(num) => num,
    }
  }
}

Context += mod {
  new := () -> Self => {
    Context(map = Map())
  }

  get := (&self, name: &Name) -> Option<Num> => {
    self.map.get(name)
  }
}

main := () with IO => {
  #use Context::new()

  match Expr::eval(Add(Lit(1), Lit(2))) {
    Some(Num(value)) => println(f"result: {value}"),
    None => println("error"),
  }
}
```
