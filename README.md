# PoC ariadne server-side codegen

This repository contains a PoC for dynamically checking the types of ariadne resolvers.

The current version is able to dynamically detect the return types of parent resolvers and ensures that they match the
expected parent type of the field resolvers.

The key is to create an artificial function for every `ObjectType`, that takes all resolvers related to the object and
tries to coerce the return type of every parent resolver to the same `TypeVar` `T`, which must also be the same as the
parent object (first argument) expected by all field resolvers of the object.

The function doesn't require a body, but only a typed signature. It can then be called with the actual resolver
functions that are imported from a custom module. If this function call is wrapped inside a `if TYPE_CHECKING:` clause,
it will never be executed but only evaluated by a type checker (hence no need for a body).

This PoC contains two approaches to define the signature of this artificial function:

* `generated/resolver_type_check_protocols:validate_issue` defines the signature as `Protocol`'s (inspired
  by [graphql-codegen-ariadne](https://github.com/enra-GmbH/graphql-codegen-ariadne/blob/main/tests/04_resolver.py).
  This has the advantage, that it can be reused when assigning the resolvers to the objects
  fields. This approach is recognized by both `mypy` and `pyright`.
* Unfortunately not all type checkers support this `Protocol`-based approach. E.g. pyCharms integrated type check
  doesn't recognize the errors. To provide type-checking support inside pyCharm (without running a separate type
  checker) the artificial function signature can be typed with complete `Callable`'s (
  see `generated/resolver_type_check_protocols:validate_issue`).

## Coverage

Example schema:

```gql
type Query {
  issue(id: ID!): Issue
}

type Issue {
  id: ID!
  text: String!
  parent: Issue
}
```

Test cases:

- [X] Resolver returns object type (`Query.issue`, `Issue.parent`)
- [X] Resolver returns scalar type (`Issue.id`, `Issue.text`)
- [X] Multiple resolvers return the same return type (`Query.issue`, `Issue.parent`)
- [X] Multiple resolvers require the same parent type (`Issue.*`)

## Tasks

- [X] Base types for resolvers (sync, async, callable, iterable).
- [X] Example schema (based
  on [this issue](https://github.com/mirumee/ariadne-codegen/issues/122#issuecomment-1499207518)).
- [X] Basic resolver implementation with at least one non-default resolver.
- [X] Create typed resolver signatures.
- [X] Validate that return type of parent resolvers match expected parent type of child resolver.
- [X] Confirm validation with mypy and pyright.
- [ ] Create bindables based on schema and assign custom resolvers to fields.
- [ ] Create schema from generated bindables.
- [ ] Create basic tests for generated schema.

## Dev-Setup

Install dependencies via poetry `poetry install` or use provided Makefile `make install`.

Run the type checks with `make -k check` (`-k` to continue after mypy fails at the expected positions).

In the current version, this should flag the validation functions
in `tests/generated/check_wrong_resolver_type_check_*.py`.
