# Failure-case index — zero-shot image→PlantUML benchmark

**Models included: 1/1** (panel label: supplementary) — 30 sampled cases.

Stratified sample of failures: up to **2 case(s) per (model × diagram type × tier × outcome class)** over the failure classes `provider_drop`, `compile_fail`, `compiled_low_structural`. `compiled_low_structural` = rendered but Element or Relationship F1 < 0.5. Selection is a seeded shuffle (seed=20260614) over key-sorted rows — deterministic and per-cell independent. A missing prediction/render file is itself signal (a provider drop or a non-rendering prediction).

## Coverage (available → sampled)

| Model | provider_drop | compile_fail | compiled_low_structural |
|---|---|---|---|
| Claude Sonnet 4.6 | — | 32→14 | 122→16 |

_13 cell(s) capped at 2 (full list in the JSON `capped_cells`) — the sample is a subset of those cells, not the complete failure set._

## Cases

### Claude Sonnet 4.6

#### outcome: compile_fail

#### `09ba2de07109b08b037d680246f10d2d5832b75f` — compile_fail (class, tier 1)

- CSR: `Error line 9 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/09ba2de07109b08b037d680246f10d2d5832b75f.puml`
- Element: tp=0 fp=0 fn=2 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=2 F1=0.000; missed: inheritance, association
- chrF++: 66.69
- Files: GT `data/puml_files/09ba2de07109b08b037d680246f10d2d5832b75f.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/09ba2de07109b08b037d680246f10d2d5832b75f.puml` (yes) · input `data/puml_images_1568/09ba2de07109b08b037d680246f10d2d5832b75f.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/09ba2de07109b08b037d680246f10d2d5832b75f.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: 09ba2de07109b08b037d680246f10d2d5832b75f
' Original Path: /examples/namespaces2.example.puml
' Source: World of Code

@startuml
class pkg_1.ClassDefinition
class pkg_2.ClassDefinition
pkg_1.ClassDefinition --> pkg_2.ClassDefinition 
pkg_1.ClassDefinition <|-- pkg_2.ClassDefinition 
@enduml 
```

Prediction PlantUML:
```plantuml
@startuml

package pkg_1 {
  class ClassDefinition {
  }
}

package pkg_2 {
  class ClassDefinition as ClassDefinition2 {
  }
}

pkg_1.ClassDefinition <|-- ClassDefinition2
ClassDefinition2 --> pkg_1.ClassDefinition

@enduml
```

#### `0ea5f288ee82befc3545dcfdd93bd701054ddf27` — compile_fail (sequence, tier 2)

- CSR: `Error line 13 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/0ea5f288ee82befc3545dcfdd93bd701054ddf27.puml`
- Element: tp=0 fp=0 fn=3 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=8 F1=0.000; missed: message
- chrF++: 86.16
- Files: GT `data/puml_files/0ea5f288ee82befc3545dcfdd93bd701054ddf27.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/0ea5f288ee82befc3545dcfdd93bd701054ddf27.puml` (yes) · input `data/puml_images_1568/0ea5f288ee82befc3545dcfdd93bd701054ddf27.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/0ea5f288ee82befc3545dcfdd93bd701054ddf27.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: 0ea5f288ee82befc3545dcfdd93bd701054ddf27
' Original Path: /specs/workload_expiration.plantuml
' Source: World of Code

@startuml

title Deploy workload

actor User as user
database tfexplorer
boundary node

autonumber
user -> tfexplorer: send workloads definition
tfexplorer -> tfexplorer: ensure enough capacity is available in the pool.
tfexplorer -> tfexplorer: decrease remaining pool capacity
tfexplorer -> node: sends workloads definition
alt workload deployed sucesfully
node --> tfexplorer: result success
user -> node: user access its workload
else failed to deploy workload or provision timeout reached
tfexplorer -> node: cancel full reservation
tfexplorer -> tfexplorer: increase remaining pool capacity
end
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
title Deploy workload

actor User
database tfexplorer
node node

User -> tfexplorer : **1** send workloads definition
tfexplorer -> tfexplorer : **2** ensure enough capacity is available in the pool.
tfexplorer -> tfexplorer : **3** decrease remaining pool capacity
tfexplorer -> node : **4** sends workloads definition

alt [workload deployed sucesfully]
    node --> tfexplorer : **5** result success
    User -> node : **6** user access its workload
else [failed to deploy workload or provision timeout reached]
    tfexplorer -> node : **7** cancel full reservation
    tfexplorer -> tfexplorer : **8** increase remaining pool capacity
end

@enduml
```

#### `13f02fcb3ac51bd86cbae3cd6980af31cbedc521` — compile_fail (sequence, tier 3)

- CSR: `Error line 4 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/13f02fcb3ac51bd86cbae3cd6980af31cbedc521.puml`
- Element: tp=0 fp=0 fn=5 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=9 F1=0.000; missed: message
- chrF++: 24.72
- Files: GT `data/puml_files/13f02fcb3ac51bd86cbae3cd6980af31cbedc521.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/13f02fcb3ac51bd86cbae3cd6980af31cbedc521.puml` (yes) · input `data/puml_images_1568/13f02fcb3ac51bd86cbae3cd6980af31cbedc521.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/13f02fcb3ac51bd86cbae3cd6980af31cbedc521.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: 13f02fcb3ac51bd86cbae3cd6980af31cbedc521
' Original Path: /test4/sequence4_5.puml
' Source: World of Code

@startuml

actor ":读者"
actor ":图书管理员"
loop
":读者"->":图书管理员" :1.取消预定
activate ":读者"
activate ":图书管理员"
":图书管理员" ->"还书界面" :2.处理图书
activate "还书界面"

"还书界面"->":还书信息" :3.获取图书信息
activate ":还书信息"
":还书信息"->"还书界面" :4.图书信息
deactivate ":还书信息"
deactivate "还书界面"

":系统"<-"还书界面" :5.删除预定记录
activate "还书界面"
activate ":系统"
":系统" -> ":系统" : 6.删除预定记录
":系统"-> "还书界面" : 7.删除预定成功
deactivate ":系统"
"还书界面"->":图书管理员" :8.处理图成功
deactivate "还书界面"
":图书管理员"->":读者" :9.取消预定成功
deactivate ":图书管理员"
deactivate ":读者"
end


@enduml
```

Prediction PlantUML:
```plantuml
@startuml
actor :读者 as reader
actor :图书管理员 as librarian
boundary 还书界面 as ui
entity :还书信息 as info
control :系统 as system

loop
    reader -> librarian : 1.取消预定
    librarian -> ui : 2.处理图书
    ui -> info : 3.获取图书信息
    info --> ui : 4.图书信息
    ui -> system : 5.删除预定记录
    system --> ui : 6.删除预定记录
    ui --> librarian : 7.删除预定成功
    librarian --> reader : 8.处理图成功
    reader <-- librarian : 9.取消预定成功
end

@enduml
```

#### `1bca4778a2b1752ff82d4954b38bd9f6f92cdcda_02` — compile_fail (class, tier 4)

- CSR: `Error line 72 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/1bca4778a2b1752ff82d4954b38bd9f6f92cdcda_02.puml`
- Element: tp=0 fp=0 fn=9 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=11 F1=0.000; missed: inheritance, composition, aggregation, association
- chrF++: 74.17
- Files: GT `data/puml_files/1bca4778a2b1752ff82d4954b38bd9f6f92cdcda_02.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/1bca4778a2b1752ff82d4954b38bd9f6f92cdcda_02.puml` (yes) · input `data/puml_images_1568/1bca4778a2b1752ff82d4954b38bd9f6f92cdcda_02.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/1bca4778a2b1752ff82d4954b38bd9f6f92cdcda_02.png` (MISSING)

GT PlantUML (truncated):
```plantuml
' Blob ID: 1bca4778a2b1752ff82d4954b38bd9f6f92cdcda
' Original Path: /docs/diagrams/src/Ski Championship Management.wsd
' Source: World of Code

@startuml
hide empty members
caption Ski Championships Management\nClass Diagram
footer Bertrand C
header Last updated 15/10/2020
title Ski Championships\nManagement

namespace Scm {
    'note "This is a floating note\n<b>in case I need it</b>" as N1

    class Event
    {
        -id: int
        -location: string
        -startDate: Date
        -endDate: Date
        +create(): Event
        +update()
        +delete(): bool
        +{static}list(): Event[]
        +export(): bool
        +import(): bool
    }

    class Competitor
    {
        -id: int
        -lastName: string
        -firstName: string
        -birthDate: Date
        -bibNumber: int
        -email: string
        -photo: resource
        +create(): Competitor
        +update()
        +delete(): bool
        +{static}list(): Competitor[]
    }

    class Run
    {
        -number: int
        -time: Time
        --
        ..Getters and setters..
        +getId()
        ..Other methods..
        +create(): Run
        +delete(): bool
    }

    class Result
    {
        -time: Time
        +create(): Result
        +delete(): bool
        +{static}list(): Result[]
    }

    abstract Metadata
    {
        #id: int
        #name: string
        #description: string
        #create()
        #update()
        #delete(): bool
        #list(): Metadata
    }

    class Category
    {
    }

    class Profile
    {
```

Prediction PlantUML (truncated):
```plantuml
@startuml
title Ski Championships\nManagement

package "Scm" {

class Event {
  -id: int
  -location: string
  -startDate: Date
  -endDate: Date
  --
  +create(): Event
  +update()
  +delete(): bool
  +<u>list(): Event[]</u>
  +export(): bool
  +import(): bool
}

class Result {
  -time: Time
  --
  +create(): Result
  +delete(): bool
  +<u>list(): Result[]</u>
}

class Run {
  -number: int
  -time: Time
  --
  Getters and setters
  +getId()
  ....Other methods....
  +create(): Run
  +delete(): bool
}

class Competitor {
  -id: int
  -lastName: string
  -firstName: string
  -birthDate: Date
  -bibNumber: int
  -email: string
  -photo: resource
  --
  +create(): Competitor
  +update()
  +delete(): bool
  +<u>list(): Competitor[]</u>
}

abstract class Metadata {
  #id: int
  #name: string
  #description: string
  --
  #create()
  #update()
  #delete(): bool
  #list(): Metadata
}

class Category {
}

class Profile {
}

Event "1" --o "0..n" Competitor : takes part
Result "obtains" o-- o "runs" Run
Competitor "0..n" -- "0..n" Metadata
Competitor "0..n" --> "1" Category : belongs to
Competitor "0..n" --> "1" Profile : has
Category --|> Metadata
Profile --|> Metadata

}

```

#### `203d4c04005b1eae83942531402f3edcf8c0409e_03` — compile_fail (sequence, tier 3)

- CSR: `Error line 31 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/203d4c04005b1eae83942531402f3edcf8c0409e_03.puml`
- Element: tp=0 fp=0 fn=5 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=10 F1=0.000; missed: message
- chrF++: 59.39
- Files: GT `data/puml_files/203d4c04005b1eae83942531402f3edcf8c0409e_03.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/203d4c04005b1eae83942531402f3edcf8c0409e_03.puml` (yes) · input `data/puml_images_1568/203d4c04005b1eae83942531402f3edcf8c0409e_03.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/203d4c04005b1eae83942531402f3edcf8c0409e_03.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: 203d4c04005b1eae83942531402f3edcf8c0409e
' Original Path: /spec/Standing Order System Diagrams.wsd
' Source: World of Code

@startuml

skinparam defaultFontName "Helvetica Neue"
skinparam sequenceTitleFontSize 24
title Request Order Change\n\n

actor Buyer
actor Grower
actor Manager
control System
database db

Buyer -> System: Make <b>Order Change Request</b>
System -> db: Insert <b>Order</b>\n<b>Change Request</b>
System -> Manager: Email <b>Order</b>\n<b>Change Request</b>
group Confirmation process
Manager -> Buyer: Confirm details of <b>Order</b>\n<b>Change Request</b> over email
Manager -> Grower: Confirm details of <b>Order</b>\n<b>Change Request</b> over email
else All agreed?
Manager -> System: Edit <b>Order</b>
System -> db: Update <b>Order</b>
System -> db: Update <b>Order</b>\n<b>Change Request</b>
System -> Grower: Email details <b>Order Change</b>
System -> Buyer: Email details <b>Order Change</b>
else Not agreed to?
note over System, db
Nothing to do here unless we add a
<b>Change Request</b> editing function
end note
end

legend right
    1. <i>Email</i> could also mean text message,
       phone call or face to face
end legend

@enduml
```

Prediction PlantUML:
```plantuml
@startuml
title **Request Order Change**

actor Buyer
actor Grower
actor Manager
boundary System
database db

Buyer -> Manager : Make **Order Change Request**
Manager -> db : Insert **Order\nChange Request**
Manager <- System : Email **Order\nChange Request**

box "**Confirmation process**"
Manager -> Buyer : Confirm details of **Order\nChange Request** over email
Manager -> Grower : Confirm details of **Order\nChange Request** over email
end box

group [All agreed?]
  Manager -> System : Edit **Order**
  System -> db : Update **Order**
  System -> db : Update **Order\nChange Request**
  Manager <- System : Email details **Order Change**
  Buyer <- System : Email details **Order Change**
end

group [Not agreed to?]
  note over System, db : Nothing to do here unless we add a\n**Change Request** editing function
end

note bottom of System
  1. //Email// could also mean text message,\nphone call or face to face
end note

@enduml
```

#### `3bded5fefc8b422479111e7bdf517358f0584f46` — compile_fail (class, tier 3)

- CSR: `Error line 44 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/3bded5fefc8b422479111e7bdf517358f0584f46.puml`
- Element: tp=0 fp=0 fn=5 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=4 F1=0.000; missed: inheritance, composition, dependency, association
- chrF++: 54.92
- Files: GT `data/puml_files/3bded5fefc8b422479111e7bdf517358f0584f46.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/3bded5fefc8b422479111e7bdf517358f0584f46.puml` (yes) · input `data/puml_images_1568/3bded5fefc8b422479111e7bdf517358f0584f46.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/3bded5fefc8b422479111e7bdf517358f0584f46.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: 3bded5fefc8b422479111e7bdf517358f0584f46
' Original Path: /E-R/_diagrams/reference-data/SeismicAttributeType.1.0.0.puml
' Source: World of Code

@startuml
hide methods
skinparam groupInheritance 2
skinparam class {
    ArrowColor Black
    BorderColor Black
    BackgroundColor<<master-data>> LightSalmon
    BackgroundColor<<work-product-component>> Gold
    BackgroundColor<<abstract>> LightSteelBlue
    BackgroundColor<<dataset>> Ivory
    BackgroundColor<<reference-data>> Turquoise
    BackgroundColor<<Abstraction>> LightSkyBlue
    BackgroundColor<<error>> Red
    BackgroundColor<<Activity>> LightSkyBlue
    BackgroundColor<<ReferenceType>> LightSkyBlue
    BackgroundColor<<WorkProductComponent>> LightSkyBlue
    BackgroundColor<<Project>> LightSkyBlue
    BackgroundColor<<File>> LightSkyBlue
    BackgroundColor<<FileCollection>> LightSkyBlue
    BackgroundColor<<MasterData>> LightSkyBlue
    BackgroundColor<<nested array>> WhiteSmoke
    BackgroundColor<<nested>> WhiteSmoke
    packageStyle rectangle
}
package "SeismicAttributeType Outgoing Relationships View" <<rectangle>>
{
class "<size:16>SeismicAttributeType</size>" as SeismicAttributeType <<reference-data>>
class "Organisation" <<master-data>>
abstract "NameAlias[]" <<nested array>>
"SeismicAttributeType" *-- "*" "NameAlias[]"
"NameAlias[]" --> "1" "Organisation" : "DefinitionOrganisationID"

class "Reference Data Relationships" <<reference-data>> {
==
"data.NameAlias[].AliasNameTypeID" → AliasNameType
"data.NameAlias[].DefinitionOrganisationID" → StandardsOrganisation
}
"SeismicAttributeType" .up.> "Reference Data Relationships"
abstract "AbstractReferenceType" <<Abstraction>>
"SeismicAttributeType" -right-|>  "AbstractReferenceType"
}
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
title SeismicAttributeType Outgoing Relationships View

skinparam classFontStyle bold
skinparam classAttributeIconSize 0

skinparam class {
  BackgroundColor<<reference-data>> #00BCD4
  BorderColor<<reference-data>> #00BCD4
  BackgroundColor<<master-data>> #FF8C69
  BorderColor<<master-data>> #FF8C69
  BackgroundColor<<Abstraction>> #AED6F1
  BorderColor<<Abstraction>> #AED6F1
  BackgroundColor<<nested-array>> #FFFFFF
  BorderColor<<nested-array>> #888888
}

class "Reference Data Relationships" <<reference-data>> {
  "data.NameAlias[].AliasNameTypeID" → AliasNameType
  "data.NameAlias[].DefinitionOrganisationID" → StandardsOrganisation
}

class "SeismicAttributeType" <<reference-data>> {
}

class "AbstractReferenceType" <<Abstraction>> {
}

class "NameAlias[]" <<nested-array>> {
}

class "Organisation" <<master-data>> {
}

"SeismicAttributeType" .up.> "Reference Data Relationships" : " "

"SeismicAttributeType" --> "AbstractReferenceType" : " "

"SeismicAttributeType" *-- "NameAlias[]" : "*"

"NameAlias[]" --> "Organisation" : "DefinitionOrganisationID\n1"

note on link
end note

@enduml
```

#### `836fc1be71c455412e94cfec349f181ac525ab0f` — compile_fail (class, tier 2)

- CSR: `Error line 26 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/836fc1be71c455412e94cfec349f181ac525ab0f.puml`
- Element: tp=0 fp=0 fn=8 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=4 F1=0.000; missed: dependency, association
- chrF++: 66.37
- Files: GT `data/puml_files/836fc1be71c455412e94cfec349f181ac525ab0f.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/836fc1be71c455412e94cfec349f181ac525ab0f.puml` (yes) · input `data/puml_images_1568/836fc1be71c455412e94cfec349f181ac525ab0f.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/836fc1be71c455412e94cfec349f181ac525ab0f.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: 836fc1be71c455412e94cfec349f181ac525ab0f
' Original Path: /figure/chap1/frontend_pascal.uml
' Source: World of Code

@startuml



package "frontend" #DDDDDD {
  Parser .[hidden]r Scanner
}

class "Parser" as Parser {
+ paser ()
+ getDErrorCount () : int
}

class "Scanner" as Scanner {
# ExactToken ()
}

package "frontend.pascal" #DDDDDD {
  PascalParserTd .[hidden]r PascalScanner
}

class "PascalParserTd" as PascalParserTd {
+ paser ()
+ getDErrorCount () : int
}

class "PascalScanner" as PascalScanner {
# ExactToken ()
}

PascalParserTd -u-> Parser
PascalScanner -u-> Scanner

@enduml
```

Prediction PlantUML:
```plantuml
@startuml

class Scanner {
  {field} ◇ ExactToken ()
}

class Parser {
  + paser ()
  + getDErrorCount () : int
}

class PascalScanner {
  {field} ◇ ExactToken ()
}

class PascalParserTd {
  + paser ()
  + getDErrorCount () : int
}

Scanner <|-- PascalScanner
Parser <|-- PascalParserTd

package "frontend" {
  package "pascal" {
    class PascalParserTd as PascalParserTd2 {
    }
    class PascalScanner as PascalScanner2 {
    }
  }
  class Parser as Parser2 {
  }
  class Scanner as Scanner2 {
  }
}

@enduml
```

#### `a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d` — compile_fail (sequence, tier 4)

- CSR: `Error line 36 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d.puml`
- Element: tp=0 fp=0 fn=4 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=16 F1=0.000; missed: message
- chrF++: 83.07
- Files: GT `data/puml_files/a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d.puml` (yes) · input `data/puml_images_1568/a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: a675645b1b9dbe715ceb1dfdbed3eb8b44734f5d
' Original Path: /oauth/login.puml
' Source: World of Code

@startuml
' https://www.ory.sh/hydra/docs/concepts/login
hide footbox
participant "Client" as client
participant "Oauth" as oauth
participant "Login Endpoint" as login
participant "Consent Endpoint" as consent

' Open page
== Open page ==
client -> oauth : Initiate authorize code or implicit flow
oauth -> oauth : No user session (not authenticated)
oauth -> login : Redirect to login endpoint with <login_challenge>
note right
GET https://<LOGIN_ENDPOINT>/login?login_challenge=7bb518c4eec2454dbb289f5fdb4c0ee2
end note


== Login ==
' Login
client -> login : Input user/password
login -> login : Verify user/password
login <--> oauth : Fetch login request info with <login_challenge>
note right
GET http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/login?login_challenge=<challenge>
end note
login -> oauth : Accept login
note right
PUT http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/login/accept?login_challenge=<challenge>
{
    "acr": "string",
    "context": {},
    "force_subject_identifier": "string",
    "remember": true,
    "remember_for": 3600,
    "subject": "string"
}
end note
oauth --> login : Return redirect url
login -> oauth : Redirect


== Consent ==
' Consent
oauth -> oauth : First time that client asks user for permission
oauth -> consent : Redirect with <consent_challenge>
consent -> consent : Asking users permission to grant application access
consent <--> oauth : Fetch consent info
note right
GET http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/consent?consent_challenge=<challenge>
end note
consent -> oauth : Accept
note right
PUT http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/consent/accept?consent_challenge=<challenge>
{
    "grant_scope": ["openid", "offline_access"],
    "handled_at": "2019-08-24T14:15:22Z",
    "session": {
        "access_token": {
            "foo": "This field will be available when introspecting the Access Token"
        },
        "id_token": {
            "bar": "This field will be available as a claim in the ID Token"
        }
    }
}
end note
oauth --> consent : Return redirect url
consent --> oauth : Redirect page

@enduml



```

Prediction PlantUML:
```plantuml
@startuml
participant "Client" as Client
participant "Oauth" as Oauth
participant "Login Endpoint" as LoginEndpoint
participant "Consent Endpoint" as ConsentEndpoint

== Open page ==

Client -> Oauth: Initiate authorize code or implicit flow
Oauth -> Client: No user session (not authenticated)
Oauth -> LoginEndpoint: Redirect to login endpoint with <login_challenge>
note right of LoginEndpoint
  GET https://<LOGIN_ENDPOINT>/login?login_challenge=7bb518c4eec2454dbb289f5fdb4c0ee2
end note

== Login ==

Client -> LoginEndpoint: Input user/password
LoginEndpoint -> Oauth: Verify user/password
Oauth --> LoginEndpoint: Fetch login request info with <login_challenge>
note right of LoginEndpoint
  GET http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/login?login_challenge=<challenge>
end note
LoginEndpoint -> Oauth: Accept login
note right of LoginEndpoint
  PUT http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/login/accept?login_challenge=<challenge>
  {
    "acr": "string",
    "context": {},
    "force_subject_identifier": "string",
    "remember": true,
    "remember_for": 3600,
    "subject": "string"
  }
end note
Oauth ..> LoginEndpoint: Return redirect url
LoginEndpoint ..> Oauth: Redirect

== Consent ==

ConsentEndpoint -> Oauth: First time that client asks user for permission
Oauth -> ConsentEndpoint: Redirect with <consent_challenge>
ConsentEndpoint -> Oauth: Asking users permission to grant application access
Oauth --> ConsentEndpoint: Fetch consent info
note right of ConsentEndpoint
  GET http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/consent?consent_challenge=<challenge>
end note
ConsentEndpoint -> Oauth: Accept
note right of ConsentEndpoint
  PUT http(s)://<OAUTH_ADMIN_URL>/oauth2/auth/requests/consent/accept?consent_challenge=<challenge>
  {
    "grant_scope": ["openid", "offline_access"],
    "handled_at": "2019-08-24T14:15:22Z",
    "session": {
      "access_token": {
        "foo": "This field will be available when introspecting the Access Token"
      },
      "id_token": {
        "bar": "This field will be available as a claim in the ID Token"
      }
    }
  }
end note
Oauth ..> ConsentEndpoint: Return redirect url
ConsentEndpoint ..> Oauth: Redirect page

@enduml
```

#### `a87c8d584bf40e45101b8425d63c9ac5fb06c7d6` — compile_fail (class, tier 3)

- CSR: `Error line 12 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/a87c8d584bf40e45101b8425d63c9ac5fb06c7d6.puml`
- Element: tp=0 fp=0 fn=3 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=2 F1=0.000; missed: inheritance, dependency
- chrF++: 61.19
- Files: GT `data/puml_files/a87c8d584bf40e45101b8425d63c9ac5fb06c7d6.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/a87c8d584bf40e45101b8425d63c9ac5fb06c7d6.puml` (yes) · input `data/puml_images_1568/a87c8d584bf40e45101b8425d63c9ac5fb06c7d6.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/a87c8d584bf40e45101b8425d63c9ac5fb06c7d6.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: a87c8d584bf40e45101b8425d63c9ac5fb06c7d6
' Original Path: /uml/booknote-class.plantuml
' Source: World of Code

@startuml
scale 2
page 1x1
title
    在键盘上添加输入框的实现方式
    创建时间: <2019-09-11 21:17>
    endtitle
    left header
        设计到两个知识点
        1. 半遮罩层
        2. 键盘监听事件
        3. 自动布局实现动态控制TextView的高度
    endheader
    class "SuperAlertBgView" as baseView {
        --属性组 --
        NSString *placeholder;
        void(^ComfirmHandler)(NSString *);
        UIView *bgView;

        __ 函数组__
        -(void)show;
        -(void)hide;
    }
    note left of baseView 
        封装半透明遮罩层,和展示隐藏逻辑实现
    end note
    class "KeyBoardFieldView" as keyBoardField {
        --属性组 --
        __ 函数组__
    }
    baseView <|-- keyBoardField:继承<
    @enduml
```

Prediction PlantUML:
```plantuml
@startuml

title 在键盘上添加输入框的实现方式\n创建时间: <2019-09-11 21:17>

note top of SuperAlertBgView
  设计到两个知识点
  1. 半遮罩层
  2. 键盘监听事件
  3. 自动布局实现动态控制TextView的高度
end note

class SuperAlertBgView {
  ==属性组==
  NSString *placeholder;
  void(^ComfirmHandler)(NSString *);
  UIView *bgView;
  ==函数组==
  -{method} (void)show;
  -{method} (void)hide;
}

class KeyBoardFieldView {
  ==属性组==
  ==函数组==
}

note left of SuperAlertBgView : 封装半透明遮罩层,和展示隐藏逻辑实现

KeyBoardFieldView --|> SuperAlertBgView : 继承<

@enduml
```

#### `b21a6faaf6a180c501e0aba4b0056672ede1ea2d` — compile_fail (class, tier 2)

- CSR: `Error line 35 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/b21a6faaf6a180c501e0aba4b0056672ede1ea2d.puml`
- Element: tp=0 fp=0 fn=4 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=4 F1=0.000; missed: inheritance, aggregation, association
- chrF++: 73.47
- Files: GT `data/puml_files/b21a6faaf6a180c501e0aba4b0056672ede1ea2d.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/b21a6faaf6a180c501e0aba4b0056672ede1ea2d.puml` (yes) · input `data/puml_images_1568/b21a6faaf6a180c501e0aba4b0056672ede1ea2d.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/b21a6faaf6a180c501e0aba4b0056672ede1ea2d.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: b21a6faaf6a180c501e0aba4b0056672ede1ea2d
' Original Path: /Documentation/plantuml/Grid/BuildingTile.puml
' Source: World of Code

@startuml
class BuildingTile {
    + IsLocationValid : bool <<get>>
    + BuildingTile(type:StructureType, facing:Facing)
    + <<override>> ToString() : string
}
class "Dictionary`2"<T1,T2> {
}
enum StructureType {
    House= 0,
    Office= 1,
    TestStruct= 2,
}
Tile <|-- BuildingTile
BuildingTile o-> "ModelLookup<StructureType,string>" "Dictionary`2"
BuildingTile --> "structure" StructureType
BuildingTile +-- StructureType
@enduml
```

Prediction PlantUML:
```plantuml
@startuml

class Tile {
}

class BuildingTile {
  o IsLocationValid : bool «get»
  --
  o BuildingTile(type:StructureType, facing:Facing)
  o «override» ToString() : string
}

class "Dictionary`2" as Dictionary {
}

enum StructureType {
  House= 0,
  Office= 1,
  TestStruct= 2,
}

note as N1
  ModelLookup<StructureType,string>
end note

class "Dictionary`2" as Dictionary {
}

Tile <|-- BuildingTile

BuildingTile o--> Dictionary : " "

BuildingTile +--> StructureType : structure

note "T1,T2" as TNote #white ##dashed
Dictionary .. TNote

@enduml
```

#### `b98c5fc6649e2bb3ceff143dbc060d141396ff62` — compile_fail (sequence, tier 4)

- CSR: `no PNG produced`
- Element: tp=0 fp=0 fn=15 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=98 F1=0.000; missed: message
- chrF++: 34.00
- Files: GT `data/puml_files/b98c5fc6649e2bb3ceff143dbc060d141396ff62.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/b98c5fc6649e2bb3ceff143dbc060d141396ff62.puml` (yes) · input `data/puml_images_1568/b98c5fc6649e2bb3ceff143dbc060d141396ff62.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/b98c5fc6649e2bb3ceff143dbc060d141396ff62.png` (MISSING)

GT PlantUML (truncated):
```plantuml
' Blob ID: b98c5fc6649e2bb3ceff143dbc060d141396ff62
' Original Path: /src/main/java/com/leetcode/按本点播.puml
' Source: World of Code


@startuml
用户 -> "ms-trade": wapPurchase 点播图书
"ms-trade" -> "subscribe-service": purchaseObj 点播图书

"subscribe-service" -> ctu: purchaseObj 点播图书
alt 连续阅读
    ctu -> "payment-service": queryContinuousTokensMemCache 查询连续订购token
    "payment-service" -> ctu: queryContinuousTokensMemCache 返回查询连续订购token的响应
 alt token不存在或者已失效
        ctu -> "payment-service": updateContinuousTokensMemCache 保存连续订购token
        "payment-service" -> ctu: updateContinuousTokensMemCache 返回保存连续订购token的响应
 end
end
ctu -> cgw : paymentServices.getPaymentAccountInfo 查询支付号
cgw -> payment : paymentService.getPaymentAccountInfo 查询支付号
payment --> cgw: paymentService.getPaymentAccountInfo 返回查询支付号的响应
cgw --> ctu: paymentServices.getPaymentAccountInfo 返回查询支付号的响应
alt 支付账号不存在
    ctu -> upm : iUserService.getAccountInfo 查询账号的手机号
    upm --> ctu: iUserService.getAccountInfo 返回查询账号的手机号的响应
    ctu -> "public-service": matchNumberSegment 查询手机号运营商
    "public-service" -> ctu: matchNumberSegment 返回查询手机号运营商的响应
    ctu -> cgw : paymentServices.paymentAccountManagement 注册支付号
    cgw -> payment : paymentService.getPaymentAccountInfo 查询支付号
    payment --> cgw: paymentService.getPaymentAccountInfo 返回查询支付号的响应
    cgw -> payment : paymentService.createPaymentAccount 创建支付号
    payment --> cgw: paymentService.createPaymentAccount 返回创建支付号的响应
    cgw --> ctu: paymentServices.paymentAccountManagement 返回注册支付号的响应
end
ctu -> "public-service": isUserWhiteList 查询用户是否是白名单用户
"public-service" -> ctu: isUserWhiteList 返回查询用户是否是白名单用户的响应
alt 用户是白名单用户
    ctu -->"subscribe-service":  purchaseObj 点播图书返回null
end
ctu -> "public-service": matchNumberSegment 查询手机号省份id和城市id
"public-service" -> ctu: matchNumberSegment 返回查询手机号省份id和城市id的响应
ctu -> product: ereadItemQueryService.fetchItemInfo 查询产品信息
product -->ctu: ereadItemQueryService.fetchItemInfo 返回查询产品信息的响应
alt 图书来源是喜马拉雅且在有效期且折扣价是0元
    ctu -->"subscribe-service":  purchaseObj 点播图书返回24900
end
alt 多种点播方式
 alt 按本订购
 alt 赠送
            ctu -> subscribe: itemService.fetchItemSubscription 查询已有订购信息
            subscribe -->ctu: itemService.fetchItemSubscription 返回已有订购信息
 alt 上一个借阅有效期内续借
                ctu -> subscribe: itemService.subscribe 更新已有订购信息结束时间
                subscribe -->ctu: 返回响应
                ctu -->"subscribe-service":  purchaseObj 点播图书返回null
            end
            ctu -> subscribe: itemservice.authenticate 内容鉴权(按本鉴权)
            subscribe -->ctu: itemservice.authenticate 返回鉴权信息
 alt 按本鉴权通过
                ctu -->"subscribe-service":  purchaseObj 点播图书返回24900
            end
            ctu -> charging: eventCalculatorService.calculatePrice 取图书进行批价
            charging -->ctu: eventCalculatorService.calculatePrice 返回批价结果
 alt 图书来源是喜马拉雅
                ctu -> ctu: 最终价格取喜马拉雅折扣价格
                ctu -> cgw : paymentServices.autoAdaptedPayChannels 适配支付方式
                cgw --> ctu: paymentServices.autoAdaptedPayChannels 返回适配支付方式的响应
 end
 alt 图书来源不是喜马拉雅
                ctu -> cgw : paymentServices.autoAdaptedPayChannels 适配支付方式
                cgw --> ctu: paymentServices.autoAdaptedPayChannels 返回适配支付方式的响应
                ctu -> ctu: 根据系统配置项与支付方式是支付宝,微信,咪咕币客户端,咪咕币wap时折扣, \r 在原最终价格上再计算一次折扣
 end
            ctu -> order: orderManagementService.createOrder 创建订单
 order -->ctu: orderManagementService.createOrder 返回创建订单的响应
 end
 alt 非赠送
            ctu -> subscribe: itemservice.authenticate 内容鉴权(按本鉴权)
            subscribe -->ctu: itemservice.authenticate 返回鉴权信息
 alt 按本鉴权通过
```

Prediction PlantUML (truncated):
```plantuml
@startuml
skinparam sequenceMessageAlign left
skinparam maxMessageSize 200

actor "用户" as user
participant "mc-trade" as mc_trade
participant "subscribe-service" as subscribe_service
participant "ots" as ots
participant "payment-service" as payment_service
participant "cpe" as cpe
participant "payment" as payment
participant "opm" as opm
participant "public-service" as public_service
participant "product" as product
participant "subscribe" as subscribe
participant "charging" as charging
participant "order" as order
participant "proxy" as proxy
participant "campaign" as campaign

user -> mc_trade: eapPurchase 点播用户
mc_trade -> mc_trade: purchaseOtp 点播用户

group 连续包月
  mc_trade -> mc_trade: isContinuousTokenFromCache 查询缓存订购Token/Status
  mc_trade -> mc_trade: isContinuousTokenFromCache 查询缓存订购Token/Status(失败时)
  mc_trade -> mc_trade: insertContinuousTokenIntoCache 查询缓存订购Token/Status
  mc_trade -> mc_trade: updateContinuousTokenIntoCache 查询缓存订购Token/Status(失败时)
  mc_trade -> payment_service: paymentService.getPaymentAccountInfo 查询支付方
  payment_service --> mc_trade: paymentService.getPaymentAccountInfo 查询支付方式
  payment_service --> mc_trade: paymentService.getPaymentAccountInfo 查询支付方式(失败时)
  mc_trade -> payment_service: paymentService.getPaymentAccountInfo 返回支付方式可用性验证
end

group 订购(用户账号验证)
  mc_trade -> mc_trade: iOrderService.getAccountInfo 查询账号信息及状态
  mc_trade -> ots: iUserService.getAccountInfo 查询账号信息及状态
  mc_trade -> mc_trade: matchMemberSegment 查询支持支付方式匹配规则
  mc_trade -> payment_service: paymentService.paymentAccountManagement 返回支付方
  payment_service --> mc_trade: paymentService.getPaymentAccountInfo 查询支付方式
  payment_service --> mc_trade: paymentService.getPaymentAccountInfo 查询支付方式(失败时)
  payment_service --> mc_trade: paymentService.createPaymentAccount 返回是否支付账号创建
  mc_trade -> mc_trade: paymentService.paymentAccountManagement 返回支付方
  mc_trade -> mc_trade: iUserWhitelist 返回账号产品是否是高产用户组
  mc_trade -> mc_trade: iUserWhitelist 返回账号产品是否是高产用户组
end

group 获取用户是否是连续包月订购(订购前校验)
  mc_trade -> mc_trade: matchMemberSegment 查询支持支付方式匹配规则
  mc_trade -> mc_trade: matchMemberSegment 查询支持支付方式匹配规则(失败时)
  mc_trade -> mc_trade: emailFromQueryService.batchSends 返回是否产品发送
  mc_trade -> mc_trade: emailFromQueryService.batchSends 返回是否产品发送(失败时)
end

group 获取连续包月订购及连续包月订购前校验(订购前校验)
  mc_trade -> mc_trade: purchaseOtp 点播用户订购(4000)
end

group 订购(订购)
  mc_trade -> subscribe_service: ioemService.fetchMemberSubscription 查询订购订阅数据
  mc_trade -> subscribe_service: ioemService.subscribe 查询订购订阅数据
  mc_trade -> mc_trade: 初始化
  mc_trade -> mc_trade: purchaseOtp 点播用户订购(Null)
  mc_trade -> cpe: iemService.authenticate 内容验证授权查询(订购)
  cpe --> mc_trade: iemService.authenticate 返回授权数据
end

group 连续包月(订购前校验)
  mc_trade -> mc_trade: purchaseOtp 点播用户订购(4000)
  mc_trade -> mc_trade: iventCalculatorService.calculatePrice 查询支持订购价
  mc_trade -> mc_trade: iventCalculatorService.calculatePrice 返回订购价格
  group 连续包月支付渠道验证
    mc_trade -> mc_trade: 查询可用支付渠道及状态
    mc_trade -> payment_service: paymentServices.autoAdaptedPayChannels 返回支付方式
    mc_trade -> mc_trade: ←订购
  end
  group 连续包月支付渠道验证(失败)
    mc_trade -> payment_service: paymentServices.autoAdaptedPayChannels 返回支付方式
    mc_trade -> mc_trade: 根据账号和数据支持支付方式及状态,根据,用户支付方式与PayPageId对比,完成数据支持上面只有一次订购
    mc_trade -> mc_trade: ←订购
```

#### `bf0e4a69eec206028b6fbd8dfc1e9905986d987d` — compile_fail (class, tier 4)

- CSR: `Error line 40 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/bf0e4a69eec206028b6fbd8dfc1e9905986d987d.puml`
- Element: tp=0 fp=0 fn=27 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=33 F1=0.000; missed: inheritance, composition, dependency, association
- chrF++: 85.87
- Files: GT `data/puml_files/bf0e4a69eec206028b6fbd8dfc1e9905986d987d.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/bf0e4a69eec206028b6fbd8dfc1e9905986d987d.puml` (yes) · input `data/puml_images_1568/bf0e4a69eec206028b6fbd8dfc1e9905986d987d.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/bf0e4a69eec206028b6fbd8dfc1e9905986d987d.png` (MISSING)

GT PlantUML (truncated):
```plantuml
' Blob ID: bf0e4a69eec206028b6fbd8dfc1e9905986d987d
' Original Path: /old/mcd.uml
' Source: World of Code

@startuml
skinparam dpi 500
skinparam monochrome true
skinparam linetype ortho
hide circle

class Membre {
	numeroMembre : int{key}
	nom : string
	prenom : string
	adresse : string
	dateDeNaissance : date
	{field} tel : int(10)
    	createNumMembre()
	membreActif()
}
class Inscription {
	date : timestamp
	fraisIns()
	montantPayé : int
	statutInscription : {a,p}
	solde()
	setMontantPayé()
}
class Activité {
	numéroActivité : string {key}
	titre : string
    
}

class Financement {
	date : timestamp
	adresse : string
    
}
class Compétition {
	heure : timestamp
	adresse : string
}

class Epreuve {
	date : timestamp
    
}

class Discipline {
	nom : string {key}
    
}

class Spécialité {
	nom : string {key}
    
}

class Comité {
	nom : string {key}
    
    
}

class Participant {
	numéro : int {local key}
	nom : string
	prénom : string
	createNuméro()
}

class CompétitionExterne {
	nomClub : varchar
	responsableClub : varchar
	{field} tel : int(10)
}

class RésultatInterne {
	résultat : int
```

Prediction PlantUML (truncated):
```plantuml
```plantuml
@startuml

skinparam classAttributeIconSize 0
skinparam linetype ortho

note top of Membre
  La méthode membreActif fonctionnera
  comme suit :
  - si le membre est actif en tant
  que professionnel, alors la méthode
  retournera "p" ;

  - si le membre est actif en tant
  qu'amateur, alors la méthode
  retournera "a" ;

  - sinon, si le membre n'est pas
  actif, la méthode retournera NULL.

  Un membre est considéré comme actif
  s'il existe une inscription datant
  de moins d'un an rattachée à ce
  membre, et pour laquelle
  Inscription.solde = 0.
end note

note right of Inscription
  Sauf indication contraire, les héritages de cette MLD sont
  exclusifs, et les attributs doivent tous être non nuls.
end note

note left of Amateur
  L'héritage n'est pas exclusif,
  un membre ayant pu être
  professionnel par le passé
  peut ensuite être
  amateur, et vice-versa.
end note

class Membre {
  numeroMembre : int{key}
  nom : string
  prenom : string
  adresse : string
  dateDeNaissance : date
  tel : int(10)
  --
  createNumMembre()
  membreActif()
}

class Inscription {
  date : timestamp
  montantPayé : int
  statutInscription : {a,p}
  --
  fraisIns()
  solde()
  setMontantPayé()
}

class Comité {
  nom : string {key}
}

class Activité {
  numéroActivité : string {key}
  titre : string
}

class Amateur {
}

class Professionnel {
}

class Financement {
  date : timestamp
  adresse : string
```

#### `e9a06725c4d85ec28ca9d343c1f23ab41d0e398f` — compile_fail (sequence, tier 1)

- CSR: `Error line 2 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/e9a06725c4d85ec28ca9d343c1f23ab41d0e398f.puml`
- Element: tp=0 fp=0 fn=3 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=3 F1=0.000; missed: message
- chrF++: 64.84
- Files: GT `data/puml_files/e9a06725c4d85ec28ca9d343c1f23ab41d0e398f.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/e9a06725c4d85ec28ca9d343c1f23ab41d0e398f.puml` (yes) · input `data/puml_images_1568/e9a06725c4d85ec28ca9d343c1f23ab41d0e398f.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/e9a06725c4d85ec28ca9d343c1f23ab41d0e398f.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: e9a06725c4d85ec28ca9d343c1f23ab41d0e398f
' Original Path: /60030041/sequence diagram1.puml
' Source: World of Code

@startuml
actor "พนักงาน"
participant "ตรวจสอบสินค้า"
participant "จัดการข้อมูลสินค้า"
"พนักงาน" -> "ตรวจสอบสินค้า":สินค้ามาใหม่
"ตรวจสอบสินค้า" --> "จัดการข้อมูลสินค้า":เพิ่มสินค้า
 "จัดการข้อมูลสินค้า" --> "ตรวจสอบสินค้า":เพิ่มสินค้าเรียบร้อย
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
actor พนักงาน
participant ตรวจสอบสินค้า
participant จัดการข้อมูลสินค้า

พนักงาน -> ตรวจสอบสินค้า : สินค้ามาใหม่
ตรวจสอบสินค้า --> จัดการข้อมูลสินค้า : เพิ่มสินค้า
จัดการข้อมูลสินค้า --> ตรวจสอบสินค้า : เพิ่มสินค้าเรียบร้อย
@enduml
```

#### `eca2ab48326da689cc54d0efa9b678ae317e1272` — compile_fail (sequence, tier 2)

- CSR: `Error line 11 in file: data/csr/claude-sonnet-4-6_20260613T154151Z/extracted/eca2ab48326da689cc54d0efa9b678ae317e1272.puml`
- Element: tp=0 fp=0 fn=5 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=8 F1=0.000; missed: message
- chrF++: 42.89
- Files: GT `data/puml_files/eca2ab48326da689cc54d0efa9b678ae317e1272.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/eca2ab48326da689cc54d0efa9b678ae317e1272.puml` (yes) · input `data/puml_images_1568/eca2ab48326da689cc54d0efa9b678ae317e1272.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/eca2ab48326da689cc54d0efa9b678ae317e1272.png` (MISSING)

GT PlantUML:
```plantuml
' Blob ID: eca2ab48326da689cc54d0efa9b678ae317e1272
' Original Path: /starter-auth/docs/puml/tenant_create.puml
' Source: World of Code

@startuml

participant "starter-admin(超管平台服务)"
participant "starter-auth(权限中心)"
database "auth数据库"
queue "NSQ"
collections "其他业务中台服务"

"starter-admin(超管平台服务)" -> "starter-auth(权限中心)" : \
创建租户接口

"starter-auth(权限中心)" -> "auth数据库" : \
生成租户密钥，向数据库保存租户信息

"starter-auth(权限中心)" <- "auth数据库" : \
返回新增的租户ID

"starter-auth(权限中心)" --> "NSQ" : \
异步通知其他业务中台服务，进行租户初始化

"starter-admin(超管平台服务)" <- "starter-auth(权限中心)" : \
响应：租户ID及密钥信息

"NSQ" --> "其他业务中台服务" : \
异步通知，租户初始化

"starter-auth(权限中心)" <-- "NSQ" : \
异步通知，租户初始化

"starter-auth(权限中心)" -> "auth数据库" : \
创建租户下级的相关表，如：用户表，角色表

@enduml
```

Prediction PlantUML:
```plantuml
@startuml
participant "starter-admin(超管平台服务)" as admin
participant "starter-auth(权限中心)" as auth
database "auth数据库" as db
participant "NSQ" as nsq
participant "其他业务中台服务" as other

admin -> auth : 创建租户接口
auth -> db : 生成租户密钥，向数据库保存租户信息
db --> auth : 返回新增的租户ID
auth ..> nsq : 异步通知其他业务中台服务，进行租户初始化
auth --> admin : 响应：租户ID及密钥信息
nsq ..> other : 异步通知，租户初始化
nsq ..> auth : 异步通知，租户初始化
auth -> db : 创建租户下级的相关表，如：用户表，角色表

@enduml
```

#### outcome: compiled_low_structural

#### `035a538b1f737e40683b939a076334f5845e2d75` — compiled_low_structural (sequence, tier 3)

- Element: tp=6 fp=0 fn=0 F1=1.000; type-acc matched=6 correct=1 excluded=0
- Relationship: tp=6 fp=8 fn=8 F1=0.429; missed: message; extra: message
- chrF++: 66.06
- Files: GT `data/puml_files/035a538b1f737e40683b939a076334f5845e2d75.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/035a538b1f737e40683b939a076334f5845e2d75.puml` (yes) · input `data/puml_images_1568/035a538b1f737e40683b939a076334f5845e2d75.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/035a538b1f737e40683b939a076334f5845e2d75.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 035a538b1f737e40683b939a076334f5845e2d75
' Original Path: /SELAIN SISTEM/UML/SEQUENCE/administrator tu/VerifikasiSPTBKA.puml
' Source: World of Code

@startuml

autonumber
hide footbox
title Memverifikasi SPT BKA

Actor AdministratorTU
boundary Dashboard_V
boundary KontrolSPTBKA_V
control Admin_C
control KontroSPT_C
Entity SuratPerintahTugas_E

Admin_C --> Dashboard_V: load->view()
Dashboard_V --> AdministratorTU: Halaman Dashboard
AdministratorTU --> Dashboard_V: klik menu SPT BKA
Dashboard_V --> KontroSPT_C: kontrolsptbka()
KontroSPT_C --> SuratPerintahTugas_E:
    
    SuratPerintahTugas_E --> KontroSPT_C:
    KontroSPT_C --> KontrolSPTBKA_V: load->view()
    KontrolSPTBKA_V --> AdministratorTU: Halaman SPT BKA

AdministratorTU --> KontrolSPTBKA_V: klik tombol Accept SPT BKA
KontrolSPTBKA_V --> KontroSPT_C: acceptsptbkalengkap()
KontroSPT_C --> SuratPerintahTugas_E:
   
    SuratPerintahTugas_E --> KontroSPT_C:
    KontroSPT_C --> KontrolSPTBKA_V: load->view()
    KontrolSPTBKA_V --> AdministratorTU: Halaman SPT BKA

@enduml
```

Prediction PlantUML:
```plantuml
@startuml
title **Memverifikasi SPT BKA**

actor AdministratorTU

participant Dashboard_V
participant KontrolSPTBKA_V
participant Admin_C
participant KontroSPT_C
participant SuratPerintahTugas_E

Admin_C -> Dashboard_V : **1** load->view()
Dashboard_V --> AdministratorTU : **2** Halaman Dashboard
AdministratorTU -> Dashboard_V : **3** klik menu SPT BKA
Dashboard_V -> Admin_C : **4** kontrolsptbka()
Admin_C -> KontroSPT_C : **5**
KontroSPT_C --> Admin_C : **6**
Admin_C -> KontrolSPTBKA_V : **7** load->view()
KontrolSPTBKA_V --> AdministratorTU : **8** Halaman SPT BKA
AdministratorTU -> KontrolSPTBKA_V : **9** klik tombol Accept SPT BKA
KontrolSPTBKA_V -> Admin_C : **10** acceptsptbkalengkap()
Admin_C -> KontroSPT_C : **11**
KontroSPT_C --> Admin_C : **12**
Admin_C -> KontrolSPTBKA_V : **13** load->view()
KontrolSPTBKA_V --> AdministratorTU : **14** Halaman SPT BKA

@enduml
```

#### `0c347826efa0a235f71c95b3d79310d14e6bcf57` — compiled_low_structural (class, tier 2)

- Element: tp=5 fp=0 fn=0 F1=1.000; type-acc matched=5 correct=3 excluded=2
- Relationship: tp=2 fp=4 fn=4 F1=0.333; missed: dependency; extra: dependency
- chrF++: 86.18
- Files: GT `data/puml_files/0c347826efa0a235f71c95b3d79310d14e6bcf57.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/0c347826efa0a235f71c95b3d79310d14e6bcf57.puml` (yes) · input `data/puml_images_1568/0c347826efa0a235f71c95b3d79310d14e6bcf57.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/0c347826efa0a235f71c95b3d79310d14e6bcf57.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 0c347826efa0a235f71c95b3d79310d14e6bcf57
' Original Path: /src/main/java/com/shengsiyuan/dp/principle/segregation/泛化-实现关系.puml
' Source: World of Code

@startuml




abstract class DaoSupport {

  + void save(Object e)
  + void delete(Integer id)
}

class PersonServiceBean {
    + void delete(Integer id)
}

DaoSupport <|-- PersonServiceBean

note "泛化即继承关系" as N1
DaoSupport ..N1
N1 ..PersonServiceBean

interface PersonService {
  + void delete(Integer id)
}

PersonService <|.. PersonServiceBean

note "实现关系" as N2
PersonService ..N2
N2 ..PersonServiceBean


@enduml
```

Prediction PlantUML:
```plantuml
@startuml

abstract class DaoSupport {
  + void save(Object e)
  + void delete(Integer id)
}

interface PersonService {
  + void delete(Integer id)
}

class PersonServiceBean {
  + void delete(Integer id)
}

note "泛化即继承关系" as N1
note "实现关系" as N2

PersonServiceBean --|> DaoSupport
PersonServiceBean ..|> PersonService

PersonServiceBean .. N1
N1 .. DaoSupport

PersonServiceBean .. N2
N2 .. PersonService

@enduml
```

#### `133bc403688003f3e7d81702cb1901b970760b62` — compiled_low_structural (class, tier 1)

- Element: tp=0 fp=2 fn=1 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=1 fn=0 F1=0.000; extra: dependency
- chrF++: 30.41
- Files: GT `data/puml_files/133bc403688003f3e7d81702cb1901b970760b62.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/133bc403688003f3e7d81702cb1901b970760b62.puml` (yes) · input `data/puml_images_1568/133bc403688003f3e7d81702cb1901b970760b62.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/133bc403688003f3e7d81702cb1901b970760b62.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 133bc403688003f3e7d81702cb1901b970760b62
' Original Path: /bluehour/1.0-ALPHA-7/apidocs/it/tidalwave/accounting/ui/projectexplorer/ProjectExplorerPresentationControl.puml
' Source: World of Code

@startuml
    set namespaceSeparator none
    hide empty fields
    hide empty methods

    interface "<size:14>ProjectExplorerPresentationControl\n<size:10>it.tidalwave.accounting.ui.projectexplorer" as it.tidalwave.accounting.ui.projectexplorer.ProjectExplorerPresentationControl [[ProjectExplorerPresentationControl.html]] {
        {abstract} +initialize(): void
    }

    center footer UMLDoclet 2.0.12, PlantUML 1.2020.16
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
class "ProjectExplorerPresentationControl" <<Interface>> {
  + initialize(): void
}

note bottom : it.tidalwave.accounting.ui.projectexplorer
@enduml
```

#### `13535b2cbd8a085a55557cd59dee9ac4e2096202_20` — compiled_low_structural (sequence, tier 1)

- Element: tp=5 fp=0 fn=0 F1=1.000; type-acc matched=5 correct=5 excluded=0
- Relationship: tp=0 fp=4 fn=0 F1=0.000; extra: message
- chrF++: 69.64
- Files: GT `data/puml_files/13535b2cbd8a085a55557cd59dee9ac4e2096202_20.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/13535b2cbd8a085a55557cd59dee9ac4e2096202_20.puml` (yes) · input `data/puml_images_1568/13535b2cbd8a085a55557cd59dee9ac4e2096202_20.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/13535b2cbd8a085a55557cd59dee9ac4e2096202_20.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 13535b2cbd8a085a55557cd59dee9ac4e2096202
' Original Path: /apex-Walle钱包系统.wsd
' Source: World of Code

@startuml
scale 3
title uc2_6活动执行时序图
actor 管理员 as adm
participant web 
participant sever as se 
database 活动快照表 as kz
database 活动结果表 as jg
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
title uc2_6活动执行时序图

actor 管理员 as admin
participant web as web
participant sever as sever
database 活动快照表 as snapshot
database 活动结果表 as result

admin -> web
web -> sever
sever -> snapshot
sever -> result

@enduml
```

#### `45d18b21343a19f3e362cc2bfe16b2b072dda3ce` — compiled_low_structural (class, tier 4)

- Element: tp=18 fp=5 fn=5 F1=0.783; type-acc matched=18 correct=18 excluded=0
- Relationship: tp=4 fp=22 fn=20 F1=0.160; missed: inheritance, composition, dependency, association; extra: inheritance, dependency, association
- chrF++: 82.91
- Files: GT `data/puml_files/45d18b21343a19f3e362cc2bfe16b2b072dda3ce.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/45d18b21343a19f3e362cc2bfe16b2b072dda3ce.puml` (yes) · input `data/puml_images_1568/45d18b21343a19f3e362cc2bfe16b2b072dda3ce.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/45d18b21343a19f3e362cc2bfe16b2b072dda3ce.png` (yes)

#### `4788cbabec3c97afb5ecc1f2ea825d8e9bcd1461` — compiled_low_structural (sequence, tier 2)

- Element: tp=1 fp=3 fn=3 F1=0.250; type-acc matched=1 correct=1 excluded=0
- Relationship: tp=0 fp=10 fn=9 F1=0.000; missed: message; extra: message
- chrF++: 41.54
- Files: GT `data/puml_files/4788cbabec3c97afb5ecc1f2ea825d8e9bcd1461.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/4788cbabec3c97afb5ecc1f2ea825d8e9bcd1461.puml` (yes) · input `data/puml_images_1568/4788cbabec3c97afb5ecc1f2ea825d8e9bcd1461.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/4788cbabec3c97afb5ecc1f2ea825d8e9bcd1461.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 4788cbabec3c97afb5ecc1f2ea825d8e9bcd1461
' Original Path: /WebPult/WebZulu/documents/UML/Validation_Tocken.puml
' Source: World of Code

@startuml

title <b><size:45>Validation Tocken</size></b>

participant "RemoteServiceServlet" as rss << (C, #ADD1B2) >>
participant "HttpSessionCollector" as hsc << (C, #ADD1B2) >>
participant "SysLog" as sl << (L, Orange) >>

[-[#Green]> rss: Data Request
activate rss
	
	rss -[#Green]> rss: Get Session ID_client
	
        rss -[#Green]> hsc: Get Session by ID_client
	activate hsc
	hsc -[#Green]> rss: Session
	deactivate hsc
	
	rss -[#Green]> rss: <b><color:#777777> Validation Tockens </color></b> \n <b><color:#Green> True </color></b>
	activate rss #Green
		create Validation_User
		rss -[#Green]> Validation_User : Access success
	deactivate rss
	
	rss -[#Red]> rss: <b><color:#777777> Validation Tockens </color></b> \n <b><color:#Red> False </color></b>
	activate rss #Red
		rss -[#Orange]> sl : Tocken Failure (Name, Time)
		[<[#Red]- rss: Access denied
	deactivate rss
	
deactivate rss

@enduml
```

Prediction PlantUML:
```plantuml
@startuml
title **Validation Tocken**

participant "**C** RemoteServiceServlet" as RSS
participant "**C** HttpSessionCollector" as HSC
participant "**L** SysLog" as SL
participant "Validation_User" as VU

[-> RSS : Data Request

activate RSS

RSS -> RSS : Get Session ID_client
RSS <-- RSS

RSS -> HSC : Get Session by ID_client
activate HSC
RSS <-- HSC : Session
deactivate HSC

note over RSS : Validation Tockens\n**True**

activate RSS #darkgreen
RSS <-- RSS
deactivate RSS

RSS -> VU : Access success

note over RSS : Validation Tockens\n**False**

activate RSS #red
RSS <-- RSS
deactivate RSS

RSS -> SL : Tocken Failure (Name, Time)

[<-- RSS : Access denied
deactivate RSS

@enduml
```

#### `4d55d9c17b48517f603b4236d9eea9bb07d7ab17` — compiled_low_structural (sequence, tier 3)

- Element: tp=5 fp=0 fn=0 F1=1.000; type-acc matched=5 correct=5 excluded=0
- Relationship: tp=6 fp=10 fn=10 F1=0.375; missed: message; extra: message
- chrF++: 76.70
- Files: GT `data/puml_files/4d55d9c17b48517f603b4236d9eea9bb07d7ab17.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/4d55d9c17b48517f603b4236d9eea9bb07d7ab17.puml` (yes) · input `data/puml_images_1568/4d55d9c17b48517f603b4236d9eea9bb07d7ab17.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/4d55d9c17b48517f603b4236d9eea9bb07d7ab17.png` (yes)

#### `6c7324c7eaeb23cd5644654ea022ca212ecd24ea` — compiled_low_structural (sequence, tier 1)

- Element: tp=1 fp=1 fn=1 F1=0.500; type-acc matched=1 correct=1 excluded=0
- Relationship: tp=0 fp=4 fn=4 F1=0.000; missed: message; extra: message
- chrF++: 54.13
- Files: GT `data/puml_files/6c7324c7eaeb23cd5644654ea022ca212ecd24ea.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/6c7324c7eaeb23cd5644654ea022ca212ecd24ea.puml` (yes) · input `data/puml_images_1568/6c7324c7eaeb23cd5644654ea022ca212ecd24ea.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/6c7324c7eaeb23cd5644654ea022ca212ecd24ea.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 6c7324c7eaeb23cd5644654ea022ca212ecd24ea
' Original Path: /Documentação/1201384/US1005/US1005_SSD.puml
' Source: World of Code

@startuml
actor SalesClerk as adm
participant "//<<presentation>>//\nDefineNewCategoryUI" as ui

autonumber

adm-->ui: Define new category

activate ui

ui-->adm: asks user information

adm-->ui: Code, Description

ui-->adm: displayCategoryInfo

deactivate ui
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
actor SalesClerk

participant "«presentation»\nDefineNewCategoryUI" as UI

SalesClerk ->  UI : **1** Define new category
SalesClerk <-- UI : **2** asks user information
SalesClerk ->  UI : **3** Code, Description
SalesClerk <-- UI : **4** displayCategoryInfo

@enduml
```

#### `75d17323e3f57e506be51b5455aa97ae89d8c5cc` — compiled_low_structural (sequence, tier 2)

- Element: tp=1 fp=3 fn=3 F1=0.250; type-acc matched=1 correct=1 excluded=0
- Relationship: tp=0 fp=6 fn=6 F1=0.000; missed: message; extra: message
- chrF++: 59.60
- Files: GT `data/puml_files/75d17323e3f57e506be51b5455aa97ae89d8c5cc.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/75d17323e3f57e506be51b5455aa97ae89d8c5cc.puml` (yes) · input `data/puml_images_1568/75d17323e3f57e506be51b5455aa97ae89d8c5cc.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/75d17323e3f57e506be51b5455aa97ae89d8c5cc.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: 75d17323e3f57e506be51b5455aa97ae89d8c5cc
' Original Path: /input/images-source/Implementing-PDQm-as-a-gateway.plantuml
' Source: World of Code

@startuml
hide footbox

Participant "Patient\nDemographics\nConsumer" as Client1
box "PDQm Implementation\ngrouped as a façade "
    Participant "Patient\n Demographics\nSupplier" as Server1
    Participant "Patient\n Demographics\nConsumer" as Client2
endbox
Participant "Patient\n Demographics\nSupplier" as Server2

Client1 -> Server1: Mobile Patient\nDemographics\nQuery [ITI-78]
activate Client1
activate Server1
Server1 --> Client2: Internal processing
activate Client2
activate Server2
Client2 -> Server2: Patient Demographics\nQuery [ITI-21]\nor Patient Demographics\nQuery for HL7v3 [ITI-47]
Client2 <- Server2: [ITI-21] or [ITI-47] Response
Server1 <-- Client2: Internal processing
deactivate Client2
deactivate Server2
Client1 <- Server1: [ITI-78] Response
deactivate Client2
deactivate Server1

@enduml
```

Prediction PlantUML:
```plantuml
@startuml
participant "Patient\nDemographics\nConsumer" as PDC1
box "PDQm Implementation\ngrouped as a façade" #LightGray
participant "Patient\nDemographics\nSupplier" as PDS1
participant "Patient\nDemographics\nConsumer" as PDC2
end box
participant "Patient\nDemographics\nSupplier" as PDS2

PDC1 -> PDS1 : Mobile Patient\nDemographics\nQuery [ITI-78]
PDS1 --> PDC2 : Internal processing
PDC2 -> PDS2 : Patient Demographics\nQuery [ITI-21]\nor Patient Demographics\nQuery for HL7v3 [ITI-47]
PDS2 -> PDC2 : [ITI-21] or [ITI-47] Response
PDC2 --> PDS1 : Internal processing
PDS1 -> PDC1 : [ITI-78] Response

@enduml
```

#### `7da506b516de210ee3d054915942c3d0f7a2160f` — compiled_low_structural (class, tier 3)

- Element: tp=5 fp=0 fn=0 F1=1.000; type-acc matched=5 correct=5 excluded=0
- Relationship: tp=1 fp=3 fn=2 F1=0.286; missed: inheritance, aggregation; extra: inheritance, aggregation, dependency
- chrF++: 82.23
- Files: GT `data/puml_files/7da506b516de210ee3d054915942c3d0f7a2160f.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/7da506b516de210ee3d054915942c3d0f7a2160f.puml` (yes) · input `data/puml_images_1568/7da506b516de210ee3d054915942c3d0f7a2160f.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/7da506b516de210ee3d054915942c3d0f7a2160f.png` (yes)

#### `9f191261deed646fe29bfdbe79135b223f66136e` — compiled_low_structural (class, tier 3)

- Element: tp=5 fp=0 fn=0 F1=1.000; type-acc matched=5 correct=5 excluded=0
- Relationship: tp=2 fp=5 fn=4 F1=0.308; missed: aggregation, association; extra: aggregation, dependency, association
- chrF++: 86.66
- Files: GT `data/puml_files/9f191261deed646fe29bfdbe79135b223f66136e.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/9f191261deed646fe29bfdbe79135b223f66136e.puml` (yes) · input `data/puml_images_1568/9f191261deed646fe29bfdbe79135b223f66136e.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/9f191261deed646fe29bfdbe79135b223f66136e.png` (yes)

#### `a33039e4fbdeb76d8d991f13075eb6aabf979e31` — compiled_low_structural (class, tier 2)

- Element: tp=0 fp=1 fn=1 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=0 fn=0 F1=1.000
- chrF++: 72.33
- Files: GT `data/puml_files/a33039e4fbdeb76d8d991f13075eb6aabf979e31.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/a33039e4fbdeb76d8d991f13075eb6aabf979e31.puml` (yes) · input `data/puml_images_1568/a33039e4fbdeb76d8d991f13075eb6aabf979e31.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/a33039e4fbdeb76d8d991f13075eb6aabf979e31.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: a33039e4fbdeb76d8d991f13075eb6aabf979e31
' Original Path: /northernwind/1.2-ALPHA-10/apidocs/it/tidalwave/northernwind/frontend/ui/component/gallery/spi/GalleryAdapter.puml
' Source: World of Code

@startuml
    set namespaceSeparator none
    hide empty fields
    hide empty methods

    interface "<size:14>GalleryAdapter\n<size:10>it.tidalwave.northernwind.frontend.ui.component.gallery.spi" as it.tidalwave.northernwind.frontend.ui.component.gallery.spi.GalleryAdapter [[GalleryAdapter.html]] {
        {abstract} +getExtraViewProperties(Id): ResourceProperties
        {abstract} +getInlinedScript(): String
        {abstract} +prepareCatalog(List<? extends GalleryItem>): void
        {abstract} +prepareGallery(GalleryItem, List<? extends GalleryItem>): void
        {abstract} +prepareFallbackGallery(GalleryItem, List<? extends GalleryItem>): void
        {abstract} +prepareFallbackLightbox(List<? extends GalleryItem>): void
        {abstract} +render(RenderContext): void
    }

    center footer UMLDoclet 2.0.12, PlantUML 1.2020.16
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
interface GalleryAdapter <<it.tidalwave.northernwind.frontend.ui.component.gallery.spi>> {
  {abstract} +getExtraViewProperties(Id): ResourceProperties
  {abstract} +getInlinedScript(): String
  {abstract} +prepareCatalog(List<? extends GalleryItem>): void
  {abstract} +prepareGallery(GalleryItem, List<? extends GalleryItem>): void
  {abstract} +prepareFallbackGallery(GalleryItem, List<? extends GalleryItem>): void
  {abstract} +prepareFallbackLightbox(List<? extends GalleryItem>): void
  {abstract} +render(RenderContext): void
}
@enduml
```

#### `ac0a357b6bbc8318261c4a48de6b6dbbfab1e58e` — compiled_low_structural (class, tier 4)

- Element: tp=9 fp=1 fn=1 F1=0.900; type-acc matched=9 correct=7 excluded=1
- Relationship: tp=6 fp=8 fn=8 F1=0.429; missed: inheritance, association; extra: inheritance, dependency
- chrF++: 84.38
- Files: GT `data/puml_files/ac0a357b6bbc8318261c4a48de6b6dbbfab1e58e.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/ac0a357b6bbc8318261c4a48de6b6dbbfab1e58e.puml` (yes) · input `data/puml_images_1568/ac0a357b6bbc8318261c4a48de6b6dbbfab1e58e.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/ac0a357b6bbc8318261c4a48de6b6dbbfab1e58e.png` (yes)

#### `bb081e2cfe075702e0a7c3b354ad0d566c4fee11` — compiled_low_structural (class, tier 1)

- Element: tp=0 fp=4 fn=2 F1=0.000; type-acc matched=0 correct=0 excluded=0
- Relationship: tp=0 fp=3 fn=1 F1=0.000; missed: inheritance; extra: inheritance, dependency
- chrF++: 38.99
- Files: GT `data/puml_files/bb081e2cfe075702e0a7c3b354ad0d566c4fee11.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/bb081e2cfe075702e0a7c3b354ad0d566c4fee11.puml` (yes) · input `data/puml_images_1568/bb081e2cfe075702e0a7c3b354ad0d566c4fee11.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/bb081e2cfe075702e0a7c3b354ad0d566c4fee11.png` (yes)

GT PlantUML:
```plantuml
' Blob ID: bb081e2cfe075702e0a7c3b354ad0d566c4fee11
' Original Path: /northernwind/1.2-ALPHA-10/it-tidalwave-northernwind-modules/it-tidalwave-northernwind-frontend-media/apidocs/it/tidalwave/northernwind/frontend/media/impl/interpolator/XmpDcTitleInterpolator.puml
' Source: World of Code

@startuml
    set namespaceSeparator none
    hide empty fields
    hide empty methods

    class "<size:14>XmpDcTitleInterpolator\n<size:10>it.tidalwave.northernwind.frontend.media.impl.interpolator" as it.tidalwave.northernwind.frontend.media.impl.interpolator.XmpDcTitleInterpolator [[XmpDcTitleInterpolator.html]] {
        +interpolate(String, Context): String
    }

    abstract class "<size:14>MetadataInterpolatorSupport\n<size:10>it.tidalwave.northernwind.frontend.media.impl.interpolator" as it.tidalwave.northernwind.frontend.media.impl.interpolator.MetadataInterpolatorSupport [[MetadataInterpolatorSupport.html]]

    it.tidalwave.northernwind.frontend.media.impl.interpolator.MetadataInterpolatorSupport <|-- it.tidalwave.northernwind.frontend.media.impl.interpolator.XmpDcTitleInterpolator

    center footer UMLDoclet 2.0.12, PlantUML 1.2020.16
@enduml
```

Prediction PlantUML:
```plantuml
@startuml
abstract class MetadataInterpolatorSupport <<A>> {
}
note top of MetadataInterpolatorSupport : it.tidalwave.northernwind.frontend.media.impl.interpolator

class XmpDcTitleInterpolator <<C>> {
  + interpolate(String, Context): String
}
note bottom of XmpDcTitleInterpolator : it.tidalwave.northernwind.frontend.media.impl.interpolator

XmpDcTitleInterpolator --|> MetadataInterpolatorSupport

@enduml
```

#### `c8c2c241aac85edf063c91907252641d60d12c1e` — compiled_low_structural (sequence, tier 4)

- Element: tp=6 fp=0 fn=0 F1=1.000; type-acc matched=6 correct=6 excluded=0
- Relationship: tp=5 fp=12 fn=12 F1=0.294; missed: message; extra: message
- chrF++: 79.86
- Files: GT `data/puml_files/c8c2c241aac85edf063c91907252641d60d12c1e.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/c8c2c241aac85edf063c91907252641d60d12c1e.puml` (yes) · input `data/puml_images_1568/c8c2c241aac85edf063c91907252641d60d12c1e.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/c8c2c241aac85edf063c91907252641d60d12c1e.png` (yes)

#### `d88ff3fb6aa3f88e69a804beac0eb19ed5b0d639` — compiled_low_structural (sequence, tier 4)

- Element: tp=1 fp=16 fn=16 F1=0.059; type-acc matched=1 correct=1 excluded=0
- Relationship: tp=0 fp=68 fn=62 F1=0.000; missed: message; extra: message
- chrF++: 76.12
- Files: GT `data/puml_files/d88ff3fb6aa3f88e69a804beac0eb19ed5b0d639.puml` (yes) · pred `data/runs/claude-sonnet-4-6_20260613T154151Z/d88ff3fb6aa3f88e69a804beac0eb19ed5b0d639.puml` (yes) · input `data/puml_images_1568/d88ff3fb6aa3f88e69a804beac0eb19ed5b0d639.png` (yes) · render `data/csr/claude-sonnet-4-6_20260613T154151Z/png/d88ff3fb6aa3f88e69a804beac0eb19ed5b0d639.png` (yes)

