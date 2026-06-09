# Evaluation Framework

Methodological record for the metrics used in the zero-shot image-to-PlantUML
benchmark. Scope: class and sequence diagrams.

## 1. Compilation Success Rate

Compilation Success Rate (CSR) is the fraction of predictions that constitute
valid, renderable PlantUML. Each prediction's PlantUML block is isolated — the
span from the first `@startuml` to the last `@enduml` — and submitted to the
official PlantUML renderer. A prediction succeeds when the renderer produces a
non-empty diagram image and fails otherwise; syntactic acceptance alone is
insufficient, so a prediction that parses but renders nothing counts as a
failure. CSR is computed over the full set of test-set keys, so a prediction that
is absent — for example an inference timeout that produced no output — counts as
a failure rather than being excluded.

## 2. Structural extraction (typed graph)

Structural metrics operate on a typed graph extracted from PlantUML source by a
custom tool (`DiagramStatsExtractor`), a fork of the official PlantUML renderer
that reuses its internal parser. The same extractor is applied to both
ground-truth and predicted code, so the two are compared on identical terms. For
each diagram the extractor emits one JSON record containing `nodes` and `edges`
alongside the diagram type.

### 2.1 Nodes

A node is a first-class diagram entity: a class-like leaf (class, interface,
enum, abstract, ...) for class diagrams, or a participant (participant, actor,
boundary, ...) for sequence diagrams. Each node carries its entity type and a
name. A grouping container that holds at least one child entity (a package or
namespace wrapping classes) is not a node; its children are the nodes.

A childless grouping container — a box written with empty braces, such as
`rectangle "Application" {}`, an empty `package`, or a `database X {}` — is a
node. PlantUML models any braced box as a group, so a box with no contents would
otherwise be dropped from the graph even though it is a single visible element
that a model reproduces as a class. Counting it as a node keeps the graph
consistent with the image: a prediction that renders the box matches it instead
of scoring a false positive (e.g. an empty-box endpoint that would otherwise
leave its incident edge pointing at a non-existent node).

Node identity is the entity's **visible display name** — the label rendered in
the image — rather than any source-level alias or code identifier. Because the
task is image-to-code, a model can reproduce only what is visible; an entity
declared `class "ApplicationTemplate" as Model` is identified as
`ApplicationTemplate`. Names are compared after lowercasing and trimming.

### 2.2 Edges

An edge is a directed relation between two entities, identified by their display
names, with a canonical relation type and an optional label. Relation types are
canonicalized from PlantUML link decorations and line style to a fixed
vocabulary:

| Relation | Source construct |
|---|---|
| inheritance | generalization or realization (triangle head; solid or dashed) |
| composition | filled-diamond decoration |
| aggregation | hollow-diamond decoration |
| dependency | dashed line carrying an arrow head |
| association | any other plain line (solid, with or without a plain arrow) |
| message | any sequence-diagram message |

Realization is folded into inheritance. Every sequence message is typed
`message`; a message whose counterpart lies outside the diagram is recorded with
an empty external endpoint on the side the external participant occupies: the
source is empty for an inbound message, whose external participant is the sender,
and the target is empty for an outbound message, whose external participant is
the receiver.

### 2.3 Accounting for unparseable predictions

Every input file yields exactly one record. A prediction that does not parse to a
complete diagram — for example a truncated model output lacking `@enduml` — is
recorded as an error with an empty graph (zero nodes, zero edges), so that such
cases are counted rather than silently dropped.

## 3. Element F1

Element F1 measures recovery of the diagram's first-class entities — the nodes of
the typed graph (classes for class diagrams, participants for sequence diagrams).
A predicted node matches a ground-truth node when their display names are equal
after lowercasing and trimming. Matching is multiset: a name occurring k times in
the ground truth is credited at most k times. For one diagram, true positives are
the matched names, precision is true positives over the predicted node count, and
recall is true positives over the ground-truth node count; F1 is their harmonic
mean. A diagram with no nodes on either side scores 1; a prediction whose graph is
empty against a non-empty ground truth scores 0.

Scores are aggregated over the set in two ways. The micro average pools true
positives, false positives, and false negatives across diagrams before forming
precision, recall, and F1, weighting each diagram by its node count. The macro
average is the mean of the per-diagram scores, weighting each diagram equally.

Element F1 is reported under two diagram populations. The compiled-only
population restricts scoring to predictions that pass Compilation Success Rate.
The zeros-for-failed population spans every test-set key, with a missing or
non-compiling prediction contributing an empty graph and therefore F1 zero. Both
sides of every comparison have their PlantUML block isolated identically (the
span from the first `@startuml` to the last `@enduml`), so any repository header
preceding the diagram is removed symmetrically before extraction.

## 4. Relationship F1

Relationship F1 measures recovery of the diagram's typed relations — the edges of
the typed graph. The matching unit is an edge; the construction otherwise follows
Element F1. A predicted edge matches a ground-truth edge when their match keys are
equal, where the match key is the triple of source endpoint, target endpoint, and
canonical relation type. Endpoints are display names compared after lowercasing
and trimming, the same normalization applied to nodes. Matching is multiset, so an
edge occurring k times — including parallel edges between the same pair — is
credited at most k times. The edge label is excluded from the key, as it is
free text recovered from the image and not part of the relation's structure.

Edge direction enters the match key by relation type. Inheritance, composition,
aggregation, dependency, and message are directional: their endpoints carry an
inherent orientation (child to parent, whole to part, sender to receiver), so a
reversed edge is a mismatch. Association is undirected: a plain line between two
entities has no inherent orientation, so its two endpoints are placed in a
canonical order before forming the key, and an association drawn in either
direction matches. Self-loops, whose source and target coincide, are scored as
ordinary edges.

For one diagram, true positives are the matched edges, precision is true positives
over the predicted edge count, and recall is true positives over the ground-truth
edge count; F1 is their harmonic mean. A diagram with no edges on either side
scores 1; a prediction whose edge set is empty against a non-empty ground truth
scores 0. The overall score, computed over all relation types jointly, is
aggregated over the set as a micro average that pools true positives, false
positives, and false negatives across diagrams, and a macro average that means the
per-diagram scores.

The score is additionally stratified by relation type. For each relation, both the
ground-truth and predicted edge sets are restricted to that relation and scored,
yielding a per-relation micro precision, recall, and F1 together with the
ground-truth and predicted edge counts that form its support. Because a diagram
that does not use a relation contributes no pooled counts to that relation's
stratum, a relation absent from a diagram neither helps nor harms its
per-relation score. This stratification reports which relation kinds models
recover well — for example inheritance versus dependency in class diagrams, and
messages in sequence diagrams.

Relationship F1 is reported under the same two diagram populations as Element F1,
the compiled-only and zeros-for-failed populations, and both sides of every
comparison have their PlantUML block isolated identically before extraction.
